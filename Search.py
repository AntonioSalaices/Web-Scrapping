from googlesearch import search
from bs4 import BeautifulSoup
import requests
import urllib3


http = urllib3.PoolManager()
entrada = input("¿Que deseas buscar?")
resultados = search(entrada, num_results=0)
print(resultados)
r = http.request('GET', resultados[0])
soup = BeautifulSoup(r.data, 'lxml')
print(soup.html)