import streamlit as st
import requests


def atualizar_sessao(selic: float):
    """
    Atualiza a sessão com os valores da SELIC e CDI.

    :param selic: Valor da SELIC.
    """
    st.session_state['selic'] = selic
    st.session_state['cdi'] = selic - 0.1


st.title("Configuração")

col1, col2 = st.columns([7, 3])

vlr_selic_session = st.session_state.get('selic', 1.0)
vlr_selic = col1.number_input('Valor da SELIC', value=vlr_selic_session, step=0.25, format="%.2f")
atualizar_sessao(vlr_selic)

col2.number_input('CDI calculado', value=vlr_selic - 0.1, format="%.2f", disabled=True)

btn_atualizar_selic = st.button('Atualizar a SELIC automaticamente',
                                icon=":material/refresh:",
                                type="primary",
                                use_container_width=True)

st.markdown("***Fonte:** [Banco Central](https://www.bcb.gov.br/controleinflacao/historicotaxasjuros)")

if btn_atualizar_selic:
    url = "https://www.bcb.gov.br/api/servico/sitebcb/historicotaxasjuros";

    headers = {
        "Host": "www.bcb.gov.br",
        "Accept": "application/json, text/plain, */*",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        st.warning("Erro ao tentar atualizar a SELIC automaticamente")
        st.stop()

    data = response.json()
    atualizar_sessao(data['conteudo'][0]['MetaSelic'])
    st.success("SELIC atualizada com sucesso!")
