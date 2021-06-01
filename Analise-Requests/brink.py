from numpy.lib.shape_base import column_stack
import requests  
import pandas as pd
import csv
import json
from bs4 import BeautifulSoup  
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# 1. Pegar conteudo HTML a partir da URL
url = "https://www.resultadofacil.com.br/resultado-do-jogo-do-bicho/PB" 
html = requests.get(url)  

if html.status_code != 200: 
        print(">> Falha na requisição! <<")
else:
    # content passa o conteúdo da página
    html_content = html.content

    # Parsear o conteúdo HTML buscado, para poder ficar mais estruturado de acordo com as tags HTML
    soup = BeautifulSoup(html_content, 'html.parser')

cabecario = soup.find('tr', )
title = soup.find_all('h3', class_='g')
#print(title)  
tabela = soup.find_all('div', class_="col-sm-12 col-md-6 col-lg-4") 
print(tabela) 