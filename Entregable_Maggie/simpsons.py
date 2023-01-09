import requests
import time 
import csv

while True :
    url = "https://thesimpsonsquoteapi.glitch.me/quotes" 
    data = requests.get(url) #este comando nos permite hacerle las peticiones a la API (URL de arriba)
    quotes1 = data.json() #en este caso le indicamos que los datos que previamente hemos conseguido con las peticiones son en formato (.json)
    
    personaje:str = quotes1[0]['character'] #aqui lo que le marcamos es que la API nos da la informacion en forma de una lista compuesta por un diccionario, pero como solo existe UN UNICO diccionario por esto le marcamos la posicion 0, porque es el unico elemento de la lista, y despues con lo de charachter lo que le decimos es que la variable personaje debe ser igual al elemento del charachter dentro del diccionario, el cual su vez se encuentra dentro de la ÚNICA lista que existe.
    frase:str = quotes1[0]['quote'] #en este caso hacemos lo mismo que la de arriba pero con las frases de los personajes
    
    my_dict0 = {"frase": frase, "personaje": personaje} #creamos un diccionario para almacenar las frases con el nombre de los personajes dentro del csv
    with open('General/general.csv', 'a') as f:  #en este caso le damos el comando de que nos abra el csv
        a = csv.DictWriter(f, my_dict0.keys())
        a.writerow(my_dict0)#aqui le decimos que en el csv general se escriban las frases de todos los personajes 

    if personaje == 'Homer Simpson':
        my_dict1 = {"frase": frase, "personaje": personaje}
        with open('Homer/homer.csv', 'a') as g: #en estos casos si hacemos un a+ a parte de hacer un append nos lo crea, en caso de que no esté.
            a = csv.DictWriter(g, my_dict1.keys())
            a.writerow(my_dict1)#en este caso solo se guardan las frases de homer en su csv propio

    if personaje == 'Lisa Simpson':
        my_dict2 = {"frase": frase, "personaje": personaje}
        with open('Lisa/lisa.csv', 'a') as h: 
            a = csv.DictWriter(h, my_dict2.keys()) #en este caso la variable de a, es asi pone lo reconoce como un append y se añaden las frases en orden de una en una, pero si fuese una w, la sobrescribiria y solo apareceria una frase en el csv, es decir la ultima frase que se haya impreso, mientras que con la a se almacenan todas.
            a.writerow(my_dict2) #aqui lo mismo que en el de homer, pero solo con lisa

    time.sleep(30) #con este comando le decimos que nos provea de la frase, pero cada 30 segundos, no de forma constante