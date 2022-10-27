import requests
import time 
import csv
import string
import os
import errno
import matplotlib.pyplot as plt

url = "https://thesimpsonsquoteapi.glitch.me/quotes" 
contador_palabras = {}
iteraciones = 0

while True :
    peticiones = requests.get(url) 
    datos = peticiones.json() 
    
    personaje:str = datos[0]['character'] 
    frase:str = datos[0]['quote'] 
    imagen = datos[0]['image']
    URL_imagen = requests.get(imagen).content 

    my_dict0 = {"personaje": personaje, "frase": frase}
    with open(f'C:\\Users\dario\OneDrive\\Documentos\\GitHub\\Entregable-1\\Entregable_Bart\\general_1.csv', 'a') as f: 
        a = csv.DictWriter(f, my_dict0.keys())
        a.writerow(my_dict0)
        
    my_dict3 = {"Carpeta": personaje, "imagen": imagen}
    with open(f'C:\\Users\dario\OneDrive\\Documentos\\GitHub\\Entregable-1\\Entregable_Bart\\Listado.csv', 'a') as f: 
        a = csv.DictWriter(f, my_dict3.keys())
        a.writerow(my_dict3)
    

    try:
        os.mkdir(f"C:\\Users\\dario\\OneDrive\\Documentos\\GitHub\\Entregable-1\\Entregable_Bart\\{personaje}")
        imagen_local = (f"C:\\Users\dario\OneDrive\\Documentos\\GitHub\\Entregable-1\\Entregable_Bart\\{personaje}\{personaje}.png") 
        with open(imagen_local, 'wb') as handler:
            handler.write(URL_imagen) 
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
        
    if personaje == 'Homer Simpson':
        my_dict1 = {"personaje": personaje,"frase": frase}
        with open(f'C:\\Users\dario\OneDrive\\Documentos\\GitHub\\Entregable-1\\Entregable_Bart\\{personaje}\{personaje}.csv', 'a') as g: 
            a = csv.DictWriter(g, my_dict1.keys())
            a.writerow(my_dict1)

    elif personaje == 'Lisa Simpson':
        my_dict2 = {"personaje": personaje, "frase": frase}
        with open(f'C:\\Users\dario\OneDrive\\Documentos\\GitHub\\Entregable-1\\Entregable_Bart\\{personaje}\{personaje}.csv', 'a') as h: 
            a = csv.DictWriter(h, my_dict2.keys()) 
            a.writerow(my_dict2) 


    
    separador = frase.split()
    for palabra in separador:
        value = 1
        palabra = palabra.translate(str.maketrans('', '', string.punctuation))
        if palabra in contador_palabras:
            primera_aparicion = contador_palabras[palabra]
            contador_palabras[palabra] = primera_aparicion + 1
        else:
            contador_palabras[palabra] = 1
    
    with open ('C:\\Users\\dario\\OneDrive\\Documentos\\GitHub\\Entregable-1\\Entregable_Bart\\CuentaPalabras.txt', 'w') as contador:
      for clave, valor in contador_palabras.items():
        if valor > 3:
            contador.write(f"{clave} {valor}\n")
    
    palabras = []
    repetidas = []

    if iteraciones == 10:
        f = open('C:\\Users\\dario\\OneDrive\\Documentos\\GitHub\\Entregable-1\\Entregable_Bart\\CuentaPalabras.txt','r')
        for row in f:
            row = row.split(' ')
            palabras.append(row[0])
            repetidas.append(int(row[1]))
  
        plt.bar(palabras, repetidas, color = 'g', label = 'File Data')
  
        plt.xlabel('Repetición de Palabras', fontsize = 12)
        plt.ylabel('Número de veces repetidas', fontsize = 12)
  
        plt.title('Palabras repetidas que se repiten 3 o más veces', fontsize = 20)
        plt.legend()
        plt.show()
    iteraciones += 1
    time.sleep(0)