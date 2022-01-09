'''
Una manera de realizar la extraccion de datos es a traves
del Web Scraping.
El web scraping es una manera de extraer informacion de 
una web . Este usa el protocolo HTTP.

Este ejemplo es extraido de la pagina:
https://datascienceplus.com/zomato-web-scraping-with-beautifulsoup-in-python/

Version Actualizada.

'''

#!Se necesita manera de ingresar a la Web desde Python
#!Enviando un HTTP request

import requests
from bs4 import BeautifulSoup

#*Request permite enviar peticiones HTTP/1.1 usando Python
#*BeutifulSoup permite extraer datos de archivos HTML y XML.

#Intentamos ingresar a la web del ejemplo

#Used headers/agent because the request was timed out and asking for an agent. 
#Using following code we can fake the agent.

url = 'https://www.zomato.com/bangalore/top-restaurants'

headers = {
    'User-Agent': 'Mozilla/5.0'
    
}
response = requests.get(url, headers=headers)

#Se intenta ver el contenido de la web
content = response.content

#print(content)
''''''

soup = BeautifulSoup(content,"html.parser")

#soup1 = str(soup)
#print(soup1)
'''
f = open("paginaBonita.txt","w") 
f.write(soup1)
f.close()
'''

#print(type(soup1))
print("Hecho")

#!Hay que buscar una manera de que sea leible
'''
Para este ejercicio en particular, estamos interesados en 
extraer el nombre del restaurante, la dirección del restaurante y 
el tipo de cocina. Para empezar a buscar estos detalles, necesitaríamos
encontrar las etiquetas HTML que almacenan esta información.
Si te detienes y miras el contenido de BeautifulSoup arriba o puedes usar 
la inspección en tu navegador web Chrome, podrás ver qué etiqueta guarda la 
colección de los mejores restaurantes y otras etiquetas que tienen más detalles.

'''


top_rest = soup.find_all("div",attrs={"class":"sc-bke1zw-1"})
#top_rest = soup.find_all("div",attrs={"class":"sc-kVIJgn"})
print(top_rest)

















'''
top_rest = soup.find_all("div",attrs={"class": "bb0 collections-grid col-l-16"})
list_tr = top_rest[0].find_all("div",attrs={"class": "col-s-8 col-l-1by3"})
'''

'''
The above code will try to find all HTML div tags containing class equals to “col-s-8 col-l-1by3” and will 
return the collection/list of restaurants data. In order to extract the further information, we will need to access 
the list elements i.e. one restaurant information one by one using a loop.


list_rest =[]
for tr in list_tr:
    dataframe ={}
    dataframe["rest_name"] = (tr.find("div",attrs={"class": "res_title zblack bold nowrap"})).text.replace('\n', ' ')
    dataframe["rest_address"] = (tr.find("div",attrs={"class": "nowrap grey-text fontsize5 ttupper"})).text.replace('\n', ' ')
    dataframe["cuisine_type"] = (tr.find("div",attrs={"class":"nowrap grey-text"})).text.replace('\n', ' ')
    list_rest.append(dataframe)
print(list_rest) 
'''

'''
import pandas
df = pandas.DataFrame(list_rest)
df.to_csv("zomato_res.csv",index=False)
'''