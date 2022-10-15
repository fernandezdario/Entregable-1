
#Estrucutura Entregable 1

#1: Conseguir los datos de la API cada 30 segundos

import requests
import json
import time 
import csv

lista_general = []
lista_lisa = []
lista_homer = []
while True :
    url = "https://thesimpsonsquoteapi.glitch.me/quotes"
    data = requests.get(url)
    quotes1 = data.json()
    
    personaje:str = quotes1[0]['character']
    frase:str = quotes1[0]['quote']
    if personaje == 'Homer Simpson':
        lista_homer.append((personaje, frase))
        lista_general.append((personaje,frase))

    elif personaje == 'Lisa Simpson':
        lista_general.append((personaje, frase))
        lista_lisa.append((personaje,frase))


    lista_general.append((personaje, frase))
    my_dict0 = {"frase": frase, "personaje": personaje}
    with open('general.csv', 'a') as f: 
        a = csv.DictWriter(f, my_dict0.keys())
        a.writerow(my_dict0)

    if personaje == 'Homer Simpson':
        my_dict1 = {"frase": frase, "personaje": personaje}
        with open('homer.csv', 'a') as g: 
            a = csv.DictWriter(g, my_dict1.keys())
            a.writerow(my_dict1)

    if personaje == 'Lisa Simpson':
        my_dict2 = {"frase": frase, "personaje": personaje}
        with open('lisa.csv', 'a') as h: 
            a = csv.DictWriter(h, my_dict2.keys())
            a.writerow(my_dict2)

    time.sleep(30)
