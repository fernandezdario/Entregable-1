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
    imagen:str = quotes1[0]['image']
    if personaje == 'Homer Simpson':
        lista_homer.append((personaje, frase, imagen))
        lista_general.append((personaje,frase, imagen)) 

    elif personaje == 'Lisa Simpson':
        lista_general.append((personaje, frase, imagen))
        lista_lisa.append((personaje, frase, imagen))


    lista_general.append((personaje, frase, imagen)) 
    
    
    my_dict0 = {"personaje": personaje, "frase": frase,  "imagen": imagen}
    with open('general_1.csv', 'a') as f: 
        a = csv.DictWriter(f, my_dict0.keys())
        a.writerow(my_dict0)

    if personaje == 'Homer Simpson':
        my_dict1 = {"personaje": personaje,"frase": frase, "imagen": imagen}
        with open('homer_1.csv', 'a') as g: 
            a = csv.DictWriter(g, my_dict1.keys())
            a.writerow(my_dict1)

    if personaje == 'Lisa Simpson':
        my_dict2 = {"personaje": personaje, "frase": frase, "imagen": imagen}
        with open('lisa_1.csv', 'a') as h: 
            a = csv.DictWriter(h, my_dict2.keys()) 
            a.writerow(my_dict2) 

    time.sleep(5) 

