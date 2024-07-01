import requests
import json

class Cliente:
    def __init__(self,nombre,cedula,edad,partido,tipo):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.partido = partido
        self.tipo = tipo