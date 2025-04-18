import sys
import os

# Adiciona a pasta raiz do projeto ao caminho de busca do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Tools.WikipediaTool import WikipediaTool