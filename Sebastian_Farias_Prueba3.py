import csv

def menu():
    print("Menu principal")
    print("1. Filtro jugador ")
    print("2. Filtro consola y año")
    print("3. Escribir archivo")
    print("4. Salir del programa")



def filtro_jugador(som):
    with open('juegos.csv', 'r') as archivo_csv:
        lector_csv= csv.DictReader(archivo_csv)
        for fila in lector_csv:
           tipo_juego=fila['tipo_juego']
           if fila[1]== 1:
               juegot= "Singleplayer"
           else:
               juegot="Multiplayer"
        juegos_clasificados.append({"tipo_juego":tipo_juego})   
               

        

    



def filtro_consola_año():
    with open('juegos.csv', 'r') as archivo_csv:
        lector_csv= csv.DictReader(archivo_csv)

    for fila in lector_csv:
        consola=fila ['tipo_juego']   










juegos_clasificados=[]
consolas=["Nintendo DS","Nintendo Wii","PlayStation3","Sony PSP","X360"]

while True:
    menu()
    op=input("eliga una opcion: ")
    if op=="1":
        print("etrando a la opcion 1")
        som=input("Singleplayer o Multiplayer?(s/m):")
        filtro_jugador(som)
        
    elif op=="2":
        print("2")
    elif op== "3":
        print(3)
    elif op== "4":
        print("Saliendo del programa")
        break
    else:
        print("escribir una opcion valida")  