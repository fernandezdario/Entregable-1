import requests
import json
import time 
import csv
import string
import os
import errno

lista_general = [] 
lista_lisa = []
lista_homer = []
frecuencia = {}
url = "https://thesimpsonsquoteapi.glitch.me/quotes" 
contador_palabras = {}

while True :
    peticiones = requests.get(url) 
    datos = peticiones.json() 
    
    personaje:str = datos[0]['character'] 
    frase:str = datos[0]['quote'] 
    imagen = datos[0]['image']
    URL_imagen = requests.get(imagen).content #antes estaba en el if, el elif y el de lista general

    if personaje == 'Homer Simpson':
        lista_homer.append((personaje, frase))
        lista_general.append((personaje,frase)) 

    elif personaje == 'Lisa Simpson':
        lista_general.append((personaje, frase))
        lista_lisa.append((personaje, frase))

    lista_general.append((personaje, frase)) 
    
    try:
        os.mkdir(f"C:\\Users\\dario\\OneDrive\\Documentos\\GitHub\\Entregable-1\\Entregable_Lisa\\{personaje}")
        imagen_local = f"C:\\Users\dario\OneDrive\\Documentos\\GitHub\\Entregable-1\\Entregable_Lisa\\{personaje}\{personaje}.png" 
    
        if personaje == 'Homer Simpson':
            my_dict1 = {"personaje": personaje,"frase": frase}
            with open(f'C:\\Users\dario\OneDrive\\Documentos\\GitHub\\Entregable-1\\Entregable_Lisa\\{personaje}\{personaje}.csv', 'a') as g: 
                a = csv.DictWriter(g, my_dict1.keys())
                a.writerow(my_dict1)

        elif personaje == 'Lisa Simpson':
            my_dict2 = {"personaje": personaje, "frase": frase}
            with open(f'C:\\Users\dario\OneDrive\\Documentos\\GitHub\\Entregable-1\\Entregable_Lisa\\{personaje}\{personaje}.csv', 'a') as h: 
                a = csv.DictWriter(h, my_dict2.keys()) 
                a.writerow(my_dict2) 

        my_dict0 = {"personaje": personaje, "frase": frase}
        with open(f'C:\\Users\dario\OneDrive\\Documentos\\GitHub\\Entregable-1\\Entregable_Lisa\\general_1.csv', 'a') as f: 
            a = csv.DictWriter(f, my_dict0.keys())
            a.writerow(my_dict0)
    
        with open(imagen_local, 'wb') as handler:
            handler.write(URL_imagen) 
    
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    
    separador = frase.split()
    for palabra in separador:
        palabra = palabra.translate(str.maketrans('', '', string.punctuation))
        if palabra in contador_palabras:
            primera_aparicion = contador_palabras[palabra]
            contador_palabras[palabra] = primera_aparicion + 1
        else:
            contador_palabras[palabra] = 1
    
    with open ('CuentaPalabras.txt', 'w') as contador:
      for clave, valor in contador_palabras.items():
        contador.write(f"\n{clave}: {valor}")
        
    time.sleep(1)


