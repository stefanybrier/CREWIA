# Importações relativas, que trazem as classes dos módulos 'researcher' e 'writer' localizados no mesmo diretório
from .researcher import ResearcherAgent  # Importa a classe 'ResearcherAgent' do módulo 'researcher' no mesmo pacote
from .writer import WriterAgent        # Importa a classe 'WriterAgent' do módulo 'writer' no mesmo pacote

# Definindo o que será exportado quando alguém utilizar 'from <module> import *'
__all__ = ['ResearcherAgent', 'WriterAgent']  # Apenas as classes 'ResearcherAgent' e 'WriterAgent' serão importadas

# Explicação:
# Quando alguém fizer 'from Agents import *', apenas as classes listadas em '__all__' serão importadas,
# ou seja, neste caso, apenas 'ResearcherAgent' e 'WriterAgent' estarão disponíveis para uso.
#
# Caso alguém queira importar explicitamente essas classes, pode fazer da seguinte maneira:
# from Agents import ResearcherAgent, WriterAgent
