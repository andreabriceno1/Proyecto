import requests
import json

class Restaurante:
    def __init__(self,name,restaurants):
        self.name = name
        self.restaurants = restaurants

    def buscarNombre(restaurantes):
        name = input("Ingrese el nombre del producto a buscar: ")  
        print("El producto esta en los siguientes restaurantes: ")
        for x in restaurantes:
            for y in x.restaurants:
                if y.name == name: 
                    print(f"Restaurante: {x.name}")
                    print(f"Nombre: {y.name}")
                    print(f"Cantidad: {y.quantity}")
                    print(f"Precio: {y.price}")
                    print(f"Stock: {y.stock}")
                    print(f"Tipo: {y.adicional}")
                    print(f"")

    def buscarTipo(restaurantes):
        adicional = input("Ingrese el tipo del producto a buscar: ")  
        print("Los productos de ese tipo estan en los siguientes restaurantes: ")
        for x in restaurantes:
            for y in x.restaurants:
                if y.adicional == adicional: 
                    print(f"Restaurante: {x.name}")
                    print(f"Nombre: {y.name}")
                    print(f"Cantidad: {y.quantity}")
                    print(f"Precio: {y.price}")
                    print(f"Stock: {y.stock}")
                    print(f"Tipo: {y.adicional}")
                    print(f"")

    def buscarPrecio(restaurantes):
        menor = input("Ingrese minimo costo: ") 
        while menor.isnumeric() == False:
            menor = input("Ingrese minimo costo valido: ") 
        mayor = input("Ingrese maximo costo: ") 
        while mayor.isnumeric() == False:
            mayor = input("Ingrese maximo costo valido: ") 
        print("Los productos de ese tipo estan en los siguientes restaurantes: ")
        for x in restaurantes:
            for y in x.restaurants:
                if float(y.price) >= int(menor) and float(y.price) <= int(mayor): 
                    print(f"Restaurante: {x.name}")
                    print(f"Nombre: {y.name}")
                    print(f"Cantidad: {y.quantity}")
                    print(f"Precio: {y.price}")
                    print(f"Stock: {y.stock}")
                    print(f"Tipo: {y.adicional}")
                    print(f"")
          