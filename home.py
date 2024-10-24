import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import streamlit as st

from calc import *

st.title("InvestCompare - Renda Fixa")

if 'cdi' not in st.session_state:
    st.stop()

col1, col2, col3 = st.columns(3)

perc_cdi_oferecido = col1.number_input('% do CDI oferecido', value=121, step=1)
cdi_inicial = col1.number_input('CDI inicial', value=st.session_state['cdi'], step=0.25, format="%.2f")

perc_prefixado_oferecido = col2.number_input('Pré-fixado oferecido (% a.a.)', value=13.9, step=0.1, format="%.2f")
cdi_final_estimado = col2.number_input('CDI final estimado', value=st.session_state['cdi'], step=0.1, format="%.2f")

perc_cdi_lcilca_oferecido = col3.number_input('(LCI/LCA) % do CDI oferecido', value=90, step=1)
perc_prefixado_lcilca_oferecido = col3.number_input('(LCI/LCA) Pré-fixado oferecido (% a.a.)', value=10.5, step=0.1,
                                                    format="%.2f")

colE1, colE2 = st.columns([8, 2])
graficos_selecionados = colE1.multiselect('Selecione os gráficos para exibição',
                                       ['Pré-fixado', 'Pós-fixado', 'Pré-fixado (LCI/LCA)', 'Pós-fixado (LCI/LCA)'],
                                       ['Pré-fixado', 'Pós-fixado', 'Pré-fixado (LCI/LCA)', 'Pós-fixado (LCI/LCA)'])
periodo_meses = colE2.selectbox('Período de 12 ou 24 meses?', [12, 24], index=1)

# CALCULANDO -------------------------------------------------------------------------
vlr_investido = 1_000.0
imposto_renda_periodo = calcular_imposto_renda((periodo_meses * 30) + 1)

vlr_cdi_ano_inicial = cdi_inicial / 100.0 * perc_cdi_oferecido
vlr_cdi_mes_inicial = converter(vlr_cdi_ano_inicial, 1 / 12.0)
vlr_cdi_ano_final = cdi_final_estimado / 100.0 * perc_cdi_oferecido
vlr_cdi_mes_final = converter(vlr_cdi_ano_final, 1 / 12.0)
cdi_ao_mes_futuro = calcular_curva_alteracao_cdi(vlr_cdi_ano_inicial, vlr_cdi_ano_final, periodo_meses, True)

# PRÉ-FIXADO -------------------------------------------------------------------------
vlr_prefixado_aa = perc_prefixado_oferecido
vlr_prefixado_am = converter(vlr_prefixado_aa, 1 / 12.0)

dados_prefixado = []
for i in range(periodo_meses):
    v = fv(vlr_prefixado_am, i, vlr_investido)
    if i == periodo_meses - 1:
        desconto_ir = (v - vlr_investido) * imposto_renda_periodo / 100.0
        v = v - desconto_ir
    dados_prefixado.append(v)

# PÓS-FIXADO  -------------------------------------------------------------------------
dados_posfixado = []
vlr_acumulado = vlr_investido
for i in range(periodo_meses):
    v = fv(cdi_ao_mes_futuro[i], 0 if i == 0 else 1, vlr_acumulado)
    vlr_acumulado = v
    if i == periodo_meses - 1:
        desconto_ir = (v - vlr_investido) * imposto_renda_periodo / 100.0
        v = v - desconto_ir
    dados_posfixado.append(v)

# PRÉ-FIXADO (LCI/LCA)  -------------------------------------------------------------------------
vlr_prefixado_lcilca_aa = perc_prefixado_lcilca_oferecido
vlr_prefixado_lcilca_am = converter(vlr_prefixado_lcilca_aa, 1 / 12.0)

dados_prefixado_lcilca = []
for i in range(periodo_meses):
    v = fv(vlr_prefixado_lcilca_am, i, vlr_investido)
    dados_prefixado_lcilca.append(v)

# PÓS-FIXADO (LCI/LCA)  -------------------------------------------------------------------------
vlr_cdi_ano_inicial = cdi_inicial / 100.0 * perc_cdi_lcilca_oferecido
vlr_cdi_mes_inicial = converter(vlr_cdi_ano_inicial, 1 / 12.0)
vlr_cdi_ano_final = cdi_final_estimado / 100.0 * perc_cdi_lcilca_oferecido
vlr_cdi_mes_final = converter(vlr_cdi_ano_final, 1 / 12.0)
cdi_ao_mes_futuro = calcular_curva_alteracao_cdi(vlr_cdi_ano_inicial, vlr_cdi_ano_final, periodo_meses, True)

dados_posfixado_lcilca = []
vlr_acumulado = vlr_investido
for i in range(periodo_meses):
    v = fv(cdi_ao_mes_futuro[i], 0 if i == 0 else 1, vlr_acumulado)
    vlr_acumulado = v
    dados_posfixado_lcilca.append(v)

# PLOTANDO GRÁFICO -------------------------------------------------------------------------
st.divider()
plt.clf()

if 'Pré-fixado' in graficos_selecionados:
    plt.plot(dados_prefixado, marker='o', linewidth=2, color='blue', label='Pré-fixado')

if 'Pós-fixado' in graficos_selecionados:
    plt.plot(dados_posfixado, marker='v', linewidth=2, color='orange', label='Pós-fixado')

if 'Pré-fixado (LCI/LCA)' in graficos_selecionados:
    plt.plot(dados_prefixado_lcilca, marker='s', linewidth=2, color='purple', label='Pré-fixado (LCI/LCA)')

if 'Pós-fixado (LCI/LCA)' in graficos_selecionados:
    plt.plot(dados_posfixado_lcilca, marker='X', linewidth=2, color='green', label='Pós-fixado (LCI/LCA)')

plt.xlabel('Meses')
plt.ylabel('Valor Acumulado')
plt.title('Valores LÍQUIDOS apresentados no ÚLTIMO período')
plt.legend()
plt.grid(True)
plt.gcf().set_size_inches(10, 6)

formatter = ticker.FuncFormatter(lambda x, _: f'R${x:,.2f}')
plt.gca().yaxis.set_major_formatter(formatter)

st.pyplot(plt)


@st.dialog("Tabela de Valores", width='large')
def visualizar_tabela_valores():
    df = pd.DataFrame({
        'Mês': [y + 1 for y in range(periodo_meses)],
        'Pré-fixado': dados_prefixado,
        'Pós-fixado': dados_posfixado,
        'Pré-fixado (LCI/LCA)': dados_prefixado_lcilca,
        'Pós-fixado (LCI/LCA)': dados_posfixado_lcilca
    })
    df['Pré-fixado'] = df['Pré-fixado'].apply(lambda x: f'R${x:,.2f}')
    df['Pós-fixado'] = df['Pós-fixado'].apply(lambda x: f'R${x:,.2f}')
    df['Pré-fixado (LCI/LCA)'] = df['Pré-fixado (LCI/LCA)'].apply(lambda x: f'R${x:,.2f}')
    df['Pós-fixado (LCI/LCA)'] = df['Pós-fixado (LCI/LCA)'].apply(lambda x: f'R${x:,.2f}')
    df = df.sort_values(by='Mês', ascending=False)
    st.dataframe(df, hide_index=True, use_container_width=True)


if colE2.button('Tabela de Valores', use_container_width=True, type='primary', icon=':material/table:'):
    visualizar_tabela_valores()
