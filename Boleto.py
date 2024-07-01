from random import choice

class Boleto:
    def __init__(self,nombre,partido,precio,cedula,edad,tipo,valido,id,restaurante,carrito):
        self.nombre = nombre
        self.partido = partido
        self.precio = precio
        self.cedula = cedula
        self.edad = edad
        self.tipo = tipo
        self.valido = valido
        self.id = id
        self.restaurante = restaurante
        self.carrito = carrito

    def generar_codigo():
            longitud = 5
            caracteres = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            p = ""
            p = p.join([choice(caracteres) for i in range(longitud)])
            return p

    def tablero(fila, columna,  ocupado): 
            var = 'X' #LAS FILAS Y COLUMNAS ESTAN INVERTIDAS
            estadio = []
            abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            cont1 = 0
            cont2 = 0
            
            while cont1 < columna: #crear listas en estadios
                estadio.append([])
                cont1 += 1
                
            while cont2 < fila: #crear asientos en las listas (espacios en blanco)
                for i in estadio:
                    i.append(' ')
                cont2 += 1
        
            print_columna = "     "
            cont2 = 0
            while cont2<fila:
                print_columna += abecedario[cont2]
                print_columna += " -- "
                cont2 += 1
            print_columna = list(print_columna)
            cont = 0
            while cont <4:
                print_columna.pop(-1)
                cont += 1
            print_columna = "".join(print_columna)
            
            cont3 = 1


            for i in ocupado: #Reemplazar X por vacio
                letra = i[0]
                numero = list(i)
                numero.pop(0)
                num = int("".join(numero))  
                valor = abecedario.index(letra)
                estadio[num-1][valor] = var
        
            print(print_columna)   
            for i in estadio:
                if cont3<10:
                    print(f" {cont3} {i}")
                else:
                    print(f"{cont3} {i}")
                cont3 += 1

    def value(boletos):
        id = input("Bienvenido al partido! Ingrese el id de su boleto para confirmar si es valido: ")
        while not len(id) == 5:
            id = input("El id que ha colocado no es valido, porfavor vuelva a intentarlo: ")
        found = False
        for i in boletos:
            if id == i.id:
                found = True
                break
        if found == True:
            if i.valido == False:
                i.valido = True
                print("El boleto es valido y esta disponible!")
            else:
                print("Ya un usuario compro este boleto y ya ingreso al estadio, compra un boleto que no este ocupado.")
        else:
            print("No se encotro el boleto, porfavor coloque un boleto que este disponible o uno que no este ocupado, gracias.")
        return boletos