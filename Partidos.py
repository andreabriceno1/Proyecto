import requests
import json

from Equipos import Equipo

class Partido:
    def __init__(self,id,number,home,away,date,group,stadium_id):
        self.id = id
        self.number = number
        self.home = home
        self.away = away
        self.date = date
        self.group = group
        self.stadium_id = stadium_id

    def readPartido():
        listPartido = [] 

        try:
            partidos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json")
            partidos = partidos.json()
        except:
            with open("partidos.json", "r") as data: #Leer archivo
                partidos = data.read()
                partidos = json.loads(partidos)    
        
        for i in partidos:
            home = Equipo(i['home']['id'],i['home']['code'],i['home']['name'],i['home']['group'])
            away = Equipo(i['away']['id'],i['away']['code'],i['away']['name'],i['away']['group'])
            partido = Partido(i['id'],i['number'],home,away,i['date'],i['group'],i['stadium_id'])
            listPartido.append(partido)
        return listPartido