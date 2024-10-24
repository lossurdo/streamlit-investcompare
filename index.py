import streamlit as st

st.set_page_config(page_title='InvestCompare - Renda Fixa', page_icon=':chart_with_upwards_trend:',
                   layout='wide', initial_sidebar_state='auto')

pag_home = st.Page("home.py", title="Projeções", icon=":material/monitoring:", default=True)
pag_config = st.Page("config.py", title="Configuração", icon=":material/manufacturing:")
pag_docs = st.Page("info.py", title="Informações Adicionais", icon=":material/info:")

pg = st.navigation([pag_home, pag_config, pag_docs])
pg.run()
