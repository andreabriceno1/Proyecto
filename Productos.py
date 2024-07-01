import requests
import json

class Producto:
    def __init__(self,name,quantity,price,stock,adicional):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.adicional = adicional