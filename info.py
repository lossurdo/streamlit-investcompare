import streamlit as st

st.title("Informações Adicionais")

st.header("Índice")
"""
* [Sobre o InvestCompare](#sobre-o-investcompare)
* [Reuniões do Copom](#reunioes-do-copom)
* [Configuração](#configuracao)
* [Política de Privacidade](#politica-de-privacidade)
"""

st.divider()
st.header("Sobre o InvestCompare", anchor="sobre-o-investcompare")
"""
O InvestCompare - Renda Fixa é uma ferramenta que permite comparar diferentes tipos de investimentos de renda fixa,
como CDBs, LCIs, LCAs e o Tesouro Direto. Através de simulações e projeções, é possível avaliar o rendimento de cada 
tipo de investimento e tomar decisões mais informadas sobre onde investir seu dinheiro para buscar a maior 
rentabilidade.

Ao preencher os dados necessários, como o percentual do CDI oferecido, a taxa de juros prefixada, o prazo de
investimento e outros parâmetros, o InvestCompare calcula o rendimento esperado de cada tipo de investimento e
apresenta gráficos comparativos para facilitar a visualização das diferenças entre eles.

Ao final dos cálculos, o valor apresentado já considera o desconto do Imposto de Renda, permitindo uma análise mais
realista dos retornos de cada investimento.

**Atenção:** _O InvestCompare - Renda Fixa é uma ferramenta de simulação e projeção, e os resultados apresentados são
apenas estimativas. Recomenda-se consultar um especialista em investimentos antes de tomar decisões financeiras
importantes._
"""

st.divider()
st.header("Reuniões do Copom", anchor="reunioes-do-copom")
"""
As reuniões do Comitê de Política Monetária (Copom) no Brasil são eventos fundamentais para a definição da taxa Selic, 
que é a taxa básica de juros da economia. Essas reuniões ocorrem aproximadamente a cada 45 dias e são essenciais para a 
condução da política monetária do país.

### Estrutura e Funcionamento

1. **Composição do Copom**: O Copom é composto por membros do Banco Central do Brasil, incluindo o presidente e 
diretores. Essa equipe é responsável por analisar a conjuntura econômica e tomar decisões que visam controlar a inflação 
e promover 
a estabilidade econômica.

2. **Preparação**: Antes das reuniões, os membros do Copom revisam uma série de indicadores econômicos, como a inflação, 
crescimento do PIB, taxa de desemprego e cenários internacionais. Relatórios e estudos são elaborados para fornecer uma 
base sólida para a tomada de decisão.

3. **Reunião**: Durante a reunião, os membros discutem os dados coletados, as projeções econômicas e as possíveis ações 
a serem tomadas. O debate inclui diferentes perspectivas e visões sobre como a política monetária deve ser ajustada.

4. **Decisão**: Ao final da reunião, o Copom decide se irá aumentar, reduzir ou manter a taxa Selic. Essa decisão é 
tomada por maioria, e os detalhes sobre os votos dos membros são divulgados em um comunicado oficial.

5. **Comunicação**: Após a reunião, o Copom publica uma ata que explica as razões da decisão, o contexto econômico e as 
projeções futuras. Essa transparência é importante para que o mercado e a população entendam os motivos por trás das 
mudanças na taxa de juros.

### Impactos da Decisão

A taxa Selic influencia diretamente outras taxas de juros na economia, afetando o crédito, o consumo e o investimento. 
Uma Selic alta pode ajudar a conter a inflação, mas também pode desacelerar o crescimento econômico. Por outro lado, 
uma Selic baixa tende a estimular a economia, mas pode aumentar a pressão inflacionária.

### Importância das Reuniões

As reuniões do Copom são vitais não apenas para a política monetária, mas também para a confiança dos investidores e 
para a saúde da economia brasileira. A forma como o Copom comunica suas decisões e a clareza em suas estratégias são 
cruciais para a estabilidade econômica do país.

Em resumo, as reuniões do Copom são momentos estratégicos onde se decide o rumo da política monetária, impactando 
diretamente a economia e a vida dos brasileiros.
"""

st.divider()
st.header("Configuração", anchor="configuracao")
"""
Antes de utilizar o InvestCompare - Renda Fixa, é importante configurar o valor da Selic atual.
A página de configurações contém uma automação que busca o valor da Selic do Site do Banco Central.
Mas também há a possibilidade de inserir este valor manualmente.
"""

st.divider()
st.header("Política de Privacidade", anchor="politica-de-privacidade")
"""Nós levamos a sua privacidade a sério. Nossa política é simples: **não coletamos nenhuma informação pessoal sobre 
você**.

Isso significa que, ao usar nossos serviços, você pode navegar tranquilamente, sem se preocupar com o compartilhamento 
de dados pessoais. Não pedimos nome, e-mail ou qualquer outra informação que possa identificá-lo.

Estamos aqui para proporcionar uma experiência segura e agradável. Se você tiver alguma dúvida, fique à vontade para 
entrar em contato com lossurdo.app [at] gmail.com.
"""
