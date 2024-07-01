import requests 
import json

from Restaurantes import Restaurante
from Productos import Producto


class Estadio:
    def __init__(self,id,name,city,capacity,restaurants):
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurants = restaurants

    def readEstadio():
        listEstadio = [] 
        try:
            estadios = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")
            estadios = estadios.json()
        except:
            with open("estadios.json", "r") as data: #Leer archivo
                estadios = data.read()
                estadios = json.loads(estadios)    
        
        listarest = []
        for i in estadios:
            restaurantes = []
            for y in  i['restaurants']:
                productos = []
                for x in y['products']:
                    producto=Producto(x['name'],x['quantity'],x['price'],x['stock'],x['adicional'])
                    productos.append(producto)
                restaurante = Restaurante(y['name'],productos)
                restaurantes.append(restaurante)
                listarest.append(restaurante)
            estadio = Estadio(i['id'],i['name'],i['city'],i['capacity'],restaurantes)
            listEstadio.append(estadio)
        return listEstadio,listarest
    
