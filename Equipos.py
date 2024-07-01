import requests
import json

class Equipo:
    def __init__(self,id,code,name,group):
        self.id = id
        self.code = code
        self.name = name
        self.group = group

    def readEquipos():
        listEquipos = [] 
        try:
            equipos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json")
            equipos = equipos.json()
        except:
            with open("equipos.json", "r") as data: #Leer archivo
                equipos = data.read()
                equipos = json.loads(equipos)    

        
        for i in equipos:
            equipo = Equipo(i['id'],i['code'],i['name'],i['group'])
            listEquipos.append(equipo)
        return listEquipos