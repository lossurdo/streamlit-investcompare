import streamlit as st

st.set_page_config(page_title='InvestCompare - Renda Fixa', page_icon=':chart:', 
                   layout='wide', initial_sidebar_state='auto')

pag_home = st.Page("home.py", title="Home", icon=":material/home:", default=True)
pag_config = st.Page("config.py", title="Configuração", icon=":material/manufacturing:")

pg = st.navigation([pag_home, pag_config])
pg.run()