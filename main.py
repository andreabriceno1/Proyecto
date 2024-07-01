import json

from Equipos import Equipo
from Estadios import Estadio
from Partidos import Partido
from Cliente import Cliente
from Boleto import Boleto
from Productos import Producto
from Restaurantes import Restaurante

def crearData(ocupadoG,ocupadoVIP):
       
        boletos = []
       
        with open("boleto.json", "r") as data:
            data = data.read()
            datas = json.loads(data)
        if len(datas) > 0: 
            for j in datas:
                lista_res = []
                for k in j["restaurante"]:
                    lista_pro = []
                    for l in k["restaurants"]:
                        producto = Producto(l["name"],l["quantity"],l["price"],l["stock"],l["adicional"])
                        lista_pro.append(producto)
                    restautante = Restaurante(k['nombre'],lista_pro)
                    lista_res.append(restautante)
                boleto = Boleto(j['nombre'],j['partido'],j['precio'],j['cedula'],j['edad'],j['tipo'],j['valido'],j['id'],lista_res,j['carrito'])
                boletos.append(boleto)
        
       
        try:
            with open("ocupadosG.json", "r") as data:
                data = data.read()
                datas = json.loads(data)

            if len(datas) > 0:
                ocupadoG = datas
        except:
            ocupadoG = ocupadoG


        try:
            with open("ocupadosVIP.json", "r") as data: 
                data = data.read()
                datas = json.loads(data)

            if len(datas) > 0:
                ocupadoVIP = datas
        except:
            ocupadoVIP = ocupadoVIP
        
        return boletos, ocupadoG, ocupadoVIP

equipos = Equipo.readEquipos()
estadios,restaurantes = Estadio.readEstadio()
partidos = Partido.readPartido()
ocupadoG = [] 
cont = 0
while cont < len(partidos):
    ocupadoG.append([])
    cont += 1
ocupadoVIP = []
cont = 0
while cont < len(partidos):
    ocupadoVIP.append([])
    cont += 1
boletos = []
boletos, ocupadoG, ocupadoVIP = crearData(ocupadoG, ocupadoVIP)

while True:
    opcion = input("""Bienvenido al gestor de la Eurocopa 2024
    1. Buscar
    2. Comprar entrada
    3. Validar boleto
    4. Ver productos
    5. Comprar productos
    6. Gestion de estadisticas
    Pulse cualquier otra tecla para terminar el programas
    Elija el numero de la accion que desea realizar:   
    """)


    if opcion == "1":
        opcion = input("""1. Buscar por partidos de un pais
2. Buscar partidos por estadio
3. Buscar partido por fecha
Cualquier otra tecla para retroceder
Pulse el numero de la accion que desea realizar: """)
        if opcion == "1":
            cont = 1
            for x in equipos:
                print(f"{cont}. {x.name}")
                cont += 1
            opcion = input("Ingrese el numero del equipo de desea ver: ")
            while opcion.isnumeric() == False or int(opcion) > len(equipos):
                opcion = input("Ingrese un numero valido del equipo de desea ver: ")
            for x in partidos:
                if x.home.name == equipos[int(opcion)-1].name or x.away.name == equipos[int(opcion)-1].name:
                    print(f"""Numero: {x.number}
Local: {x.home.name}
Visitante: {x.away.name}
Fecha: {x.date}
Grupo: {x.group}

""")
        elif opcion == "2":
            cont = 1
            for x in estadios:
                print(f"{cont}. {x.name}")
                cont += 1
            opcion = input("Ingrese el numero del estadio de desea ver: ")
            while opcion.isnumeric() == False or int(opcion) > len(equipos):
                opcion = input("Ingrese un numero valido del estadio de desea ver: ")
            for x in partidos:
                if x.stadium_id == estadios[int(opcion)-1].id:
                    print(f"""Numero: {x.number}
Local: {x.home.name}
Visitante: {x.away.name}
Fecha: {x.date}
Grupo: {x.group}

""")
        elif opcion == "3":
            dia = input("Ingrese el dia del partido: ")
            while dia.isnumeric() == False or int(dia) > 31 or int(dia) < 1:
                dia = input("Ingrese el dia del partido valido entre 1 y 31: ")
            mes = input("Ingrese el mes del partido: ")
            while mes.isnumeric() == False or int(mes) > 12 or int(mes) < 1:
                mes = input("Ingrese el mes del partido valido entre 1 y 12: ")
            if int(dia) < 10:
                dia =  "0" + str(int(dia)) 
            if int(mes) < 10:
                mes =   "0" + str(int(mes))
            for x in partidos:
                if x.date == "2024-"+str(mes)+"-"+str(dia):
                    print(f"""Numero: {x.number}
Local: {x.home.name}
Visitante: {x.away.name}
Fecha: {x.date}
Grupo: {x.group}

""")
        else:
            pass


    elif opcion == "2":
        nombre = input("Ingrese su nombre: ")
        cedula = input("Ingrese cedula: ")
        edad = input("Ingrese edad: ")
        while edad.isnumeric() == False:
            edad = input("Ingrese edad valida: ")
        for x in partidos:
            print(f"numero: {x.number}. {x.home.name} vs {x.away.name}. fecha: {x.date}")
        numero = input("Ingrese el numero del partido que desea ver: ")
        while numero.isnumeric() == False or int(numero) >36:
            numero = input("Ingrese el numero valido del partido que desea ver: ")
        tipo = input("Pulse 1 para entrada general y cualquier otra tecla para entrada VIP: ")
        if tipo == "1":
            tipo = "G"
            costo = 35
        else:
            tipo = "VIP"
            costo = 75
        costo = costo+costo*0.16
        var=122
        
        for x in partidos:
            if x.number == int(numero):
                for y in estadios:
                    if y.id == x.stadium_id:
                        if tipo == "G":
                            restautante = y.restaurants
                            var = y.capacity[0]

                        else: 
                            restautante = y.restaurants
                            var = y.capacity[1]
                
               
        if tipo == 'G':
            Boleto.tablero(10,int(var/10),ocupadoG[int(numero)-1])
        else:
            Boleto.tablero(10,int(var/10),ocupadoVIP[int(numero)-1])
        
        asiento = input('Elija uno de los varios asiento disponibles, escribiendo la letra y el numero que desea elegir (Por Ejemplo: A6 O G5): ')    
        while not len(asiento) < 5 and not len(asiento) > 1: 
            asiento = input('Has colocado un item invalido. Porfavor Elija un asiento escribiendo la letra y el numero que desea de manera correcta (De nuevo el ejemplo: D3): ')    
        if len(asiento) == 2:
            columna = asiento[0]
            fila = asiento[1]
        elif len(asiento) == 3:
            columna = asiento[0]
            fila = str(asiento[1])+str(asiento[2])
        else:
            columna = asiento[0]
            fila = str(asiento[1])+str(asiento[2])+str(asiento[3])
        
        
        print(f'Bienvenido al sistema de factura {nombre}, nos alegra tenerte aqui!, a continuacion aparecera un texto:! Vamos a confirmar la compra de tu ticket de tu partido: Monto a pagar por el o los tickets comprados: {costo} en el o los asientos: {asiento}')
        confirmar = input('Coloque 1 si quiere confirmar la compra de su entrada. Pulse cualquier otra tecla para cancelar la compra de su entrada: ')
        if confirmar == "1":
            id = Boleto.generar_codigo() 
            boleto = Boleto(nombre,int(numero),costo,cedula,edad,tipo,False,id,restautante,[]) 
            boletos.append(boleto)
            if tipo == 'G':
                ocupadoG[int(numero)-1].append(asiento)
            else:
                ocupadoVIP[int(numero)-1].append(asiento)
            print(f'Se ha confirmado su compra, felicidades. Bienvenido a la Euro {nombre}')
            print(f'Este es el id que tendra su boleto: {boleto.id}. Debe guardarlo para poder validar su entrada al estadio que elegio. ')
    
        else:
            print("Se ha cancelado la compra de su boleto, que lastima. Sin embargo el sistema estara disponible para cuando usted lo necesite, hasta luego!. ")
            
    elif opcion == "3":
        boletos = Boleto.value(boletos)

    elif opcion == "4":
        busqueda = input('''Bienvenido al sistema de restaurantes de los estadios de la Euro: 
Pulse 1 para buscar por nombre de producto:  
Pulse 2 para buscar por tipo
Pulse 3 para buscar por rango de precio
Pulse cualquier otra tecla para retroceder:  
Que desea hacer?: ''')
        while not busqueda.isnumeric():
            busqueda = input("Has seleccionado una opcion no numerica, porfavor coloque una opcion numerica: ")
        if busqueda == "1":
            Restaurante.buscarNombre(restaurantes)

        elif busqueda == "2":
            Restaurante.buscarTipo(restaurantes)

        elif busqueda == "3":
            Restaurante.buscarPrecio(restaurantes)
    elif opcion == "5":
        Valor = input('Ingrese el id de su ticket para confirmar si es o no es premium: ')
        premium = 0 
        for i in boletos:
            if i.id == Valor:
                premium = i         
        
        if premium == 0:
            print('El ticket no se ha encontrado, verifique si escribio el id correctamente, e intentelo nuevamente porfavor: ')
        
        elif premium.tipo == "VIP":
            lista_productos = []
            if premium.valido == True:
                print(f"Bienvenido {premium.nombre}. Aca tiene la lista de productos que puede comprar: ")
                
                for i in premium.restaurante:
                    print(f"Restaurante:  {i.name}")
                    for j in i.restaurants:
                        print(f'''    Nombre: {j.name}, Tipo: {j.adicional}, Precio: {j.price}''')
                print('')

                while True:
                    print(premium.restaurante[0].restaurants[1].name)
                    productos = input('Ingrese el nombre del producto que desea comprar a continuacion (Pulse 1 para terminar compra): ')
                    if productos == '1':
                        break
                    else:
                        found = False
                        for i in premium.restaurante:
                            for j in i.restaurants:
                                if j.name == productos:
                                    save = j
                                    found = True                                        
                        if found == False:
                            print('Asegurese de escribir el nombre correctamente e intentelo nuevamente: ')
                        else:
                            quantity = input('Ingrese cuantas unidades de ese producto desea comprar: ')
                            while not quantity.isnumeric():
                                quantity = input('Ingrese una cantidad numerica correcta, e intentalo denuevo: ')
                            price = float(save.price)*float(quantity)
                            if price > 0:
                                lista_productos.append([productos,price,quantity])
                                print('Se ha anadido el producto a su carrito de compra, la compra continuara a continuacion: ')
                            else:
                                print('Tienes que ingresar las unidades del producto que desea para poder comprarlo: ') 
                print('Estos son los productos disponibles para la compra: ')
                total = 0
                for i in lista_productos:
                    print(f'{i[0]}: {i[1]}')
                    total += float(i[1])
                print(f'El total de tu carrito de compra es: {total}')
                finish = input('Ingrese 1 para culminar la compra o cualquier otra tecla para cancelar: ')
                if finish == '1':
                    for i in boletos:
                        if i == premium:
                            i.carrito.append(lista_productos)    
                                        
                    print('Se ha concluido la compra de los productos seleccionados: ')
                else:
                    print('Se ha cancelado la compra de los productos seleccionados: ')

            else:
                print('Tiene que validar su ticket obtenido anteriormente, antes de comprar algun objeto en los restaurantes: ')
        elif premium.tipo == "G":
            print('La entrada no es premium, por lo que no podra entrar al restaurante ni comprar nada en ellos: ')

        else:
            print('El ticket no se ha encontrado, verifique si escribio el id correctamente y vuelva a intentarlo nuevamente: ')

    
    elif opcion == "6":
        busqueda = input('''Bienvenido al sistema de estadisticas de la Euro: 
Pulse 1 para buscar promedio de gasto de clientes VIP:  
Pulse 2 para asistencia de partidos
Pulse 3 para partido mayor asistido
Pulse 4 para partido mayor boletos vendidos
Pulse 5 para productos mas vendidos
Pulse 6 para clientes que mas compraron boletos
Pulse cualquier otra tecla para retroceder:  
Que desea hacer?: ''')

        if busqueda == '1':
            promedio = 0
            cantidad = 0
            for x in boletos:
                if x.tipo == 'VIP':
                    cantidad += 1
                    suma = x.precio
                    for y in x.carrito:
                        suma += y[1]
                promedio += suma
            promedio = promedio/cantidad
            print(f"El promedio gastado por clientes VIP es: {promedio}")
        elif busqueda == '2':
            mayor_asistidos = [[0,x] for x in range(0,len(partidos))]
            for x in boletos:
                if x.valido == True:
                    mayor_asistidos[(x.partido-1)][0] += 1
            
            listos = []
            listos_partido = []
            terminar = False
            while terminar == False:
                mayor = 0 
                posicion = 0
                for x in mayor_asistidos:
                    if x[0] > mayor and x[1] not in listos_partido:
                        mayor = x[0]
                        posicion = x[1]
                if mayor == 0:
                    terminar = True
                else:
                    listos.append([mayor,posicion])
                    listos_partido.append(posicion)
                    
            for x in listos:
                for y in partidos:
                    if x[1] == y.number:
                        print(f'Al partido numero {y.number+1} entre {y.home.name} y {y.away.name}. asistieron {x[0]} personas')

        elif busqueda == '3':
            mayor_asistidos = [[0,x] for x in range(0,len(partidos))]
            for x in boletos:
                if x.valido == True:
                    mayor_asistidos[(x.partido-1)][0] += 1
            
            listos = []
            listos_partido = []
            terminar = False
            while terminar == False:
                mayor = 0 
                posicion = 0
                for x in mayor_asistidos:
                    if x[0] > mayor and x[1] not in listos_partido:
                        mayor = x[0]
                        posicion = x[1]
                if mayor == 0:
                    terminar = True
                else:
                    listos.append([mayor,posicion])
                    listos_partido.append(posicion)
                    
            for y in partidos:
                if listos[0][1] == y.number:
                    print(f'Al partido numero {y.number+1} entre {y.home.name} y {y.away.name}. asistieron {listos[0][0]} personas')

        elif busqueda == '4':
            mayor_asistidos = [[0,x] for x in range(0,len(partidos))]
            for x in boletos:
                mayor_asistidos[(x.partido-1)][0] += 1
            
            listos = []
            listos_partido = []
            terminar = False
            while terminar == False:
                mayor = 0 
                posicion = 0
                for x in mayor_asistidos:
                    if x[0] > mayor and x[1] not in listos_partido:
                        mayor = x[0]
                        posicion = x[1]
                if mayor == 0:
                    terminar = True
                else:
                    listos.append([mayor,posicion])
                    listos_partido.append(posicion)
                    
            for y in partidos:
                if listos[0][1] == y.number:
                    print(f'Al partido numero {y.number+1} entre {y.home.name} y {y.away.name}. compraron {listos[0][0]} boletos')
        elif busqueda == '5':
            lista_productos = {}
            nombres_productos = []
            for x in boletos:
                for y in x.carrito:
                    if y[0] in nombres_productos:
                        lista_productos[y[0]] += y[2]
                    else:
                        lista_productos[y[0]] = y[2]
                        nombres_productos.append(y[0])
            top = []
            cont = 1
            for x in range(0,3):
                mayor = 0
                cantidad = 0
                for k,v in lista_productos.items():
                    if v > cantidad and k not in top:
                        mayor = k
                        cantidad = v
                if mayor != 0:
                    print(f"El producto numero {cont} vendido es {mayor} con {cantidad} unidades")
                    top.append(mayor)
                cont += 1
        elif busqueda == '6':
            lista_personas = {}
            nombres_personas = []
            for x in boletos:
                if x.nombre in nombres_personas:
                    lista_personas[x.nombre] += 1
                else:
                    lista_personas[x.nombre] = 1
                    nombres_personas.append(x.nombre)
            top = []
            cont = 1
            for x in range(0,3):
                mayor = 0
                cantidad = 0
                for k,v in lista_personas.items():
                    if v > cantidad and k not in top:
                        mayor = k
                        cantidad = v
                if mayor != 0:
                    print(f"La personas numero {cont} que compro entradas es {mayor} con {cantidad} unidades")
                    top.append(mayor)
                cont += 1

    
    
    else:
        ocupadosGjson = open("ocupadosG.json", "w")
        ocupadosGjson.write(json.dumps(ocupadoG))
        ocupadosGjson.close()

        ocupadosVIPjson = open("ocupadosVIP.json", "w")
        ocupadosVIPjson.write(json.dumps(ocupadoVIP))
        ocupadosVIPjson.close()

        lista_boletos = []
        for i in boletos:
            dict_boleto = {}
            dict_boleto["nombre"] = i.nombre
            dict_boleto["partido"] = i.partido
            dict_boleto["precio"] = i.precio
            dict_boleto["cedula"] = i.cedula
            dict_boleto["edad"] = i.edad
            dict_boleto["tipo"] = i.tipo
            dict_boleto["valido"] = i.valido
            dict_boleto["id"] = i.id
            list_res = []
            for x in i.restaurante:
                dict_peq = {}
                dict_peq["nombre"] = x.name
                lista_prod = []
                for y in x.restaurants:
                    dict_pro = {}
                    dict_pro["name"] = y.name
                    dict_pro["quantity"] = y.quantity
                    dict_pro["price"] = y.price
                    dict_pro["stock"] = y.stock
                    dict_pro["adicional"] = y.adicional
                    lista_prod.append(dict_pro)
                dict_peq["restaurants"] = lista_prod
                list_res.append(dict_peq)

            dict_boleto["restaurante"] = list_res

            dict_boleto["carrito"] = i.carrito
            lista_boletos.append(dict_boleto)
        boletojson = open("boleto.json", "w")
        boletojson.write(json.dumps(lista_boletos))
        boletojson.close()  
        print('Hasta luego')
        break