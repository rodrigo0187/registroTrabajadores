# inicio importar datos

import csv
import random
import os
from os import system

# fin importar datos


mn = '='*30
file = ('fileregistro.csv')
cargos = ['CEO', 'Analista de datos', 'Programador', 'Desarrollador']
listaTrabajadores = []
encabezado = ['id_trabajador', 'Nombre', 'Apellido', 'Edad', 'Cargo']


def registro():
    id_trabajador = random.randint(1, 1000)
    while True:
        try:
            nombre = input('Ingrese el nombre del trabajador>\t')
            if not nombre.strip():
                print(mn)
                raise ValueError('el nombre no puede estar vacio')
            break

        except ValueError as e:
            print(f'{e}')

    while True:
        try:
            apellido = input('ingrese el apellido del trabajador>\t')
            if not apellido.strip():
                print(mn)
                raise ValueError('El campo apellido no puede estar vacio')
            break
        except ValueError as e:
            print(f'{e}')
    while True:
        try:
            edad = int(input('Ingrese la edad del trabajador>\t'))
            if edad < 0:
                print(mn)
                raise ('La edad no puede ser menor a 0')

            break
        except TypeError as e:
            print(f'{e}')
    while True:
        try:
            print(f'los cargos disponibles son:\n{cargos}')
            print(mn)
            cargo = input('Ingrese el cargo del trabajador >\t')
            if cargo.strip() not in cargos:
                raise ValueError('El cargo no es valido')
            break
        except ValueError as e:
            print(f'{e}')

    listAux = {
        "id_trabajador": id_trabajador,
        "Nombre": nombre,
        "Apellido": apellido,
        "Edad": edad,
        "Cargo": cargo
    }
    listaTrabajadores.append(listAux)

    # ruta de la carpeta donde se va a guardar el archivo , validacion de existencia de la carpeta
    ruta = r"D:\\WorkSpace\\worksspace\\registroTrabajadores\\listcsv.csv"
    directory = os.path.dirname(ruta)
    os.makedirs(directory, exist_ok=True)

    with open(ruta, 'a+', newline='') as file_input:
        writer = csv.DictWriter(file_input, fieldnames=encabezado)
        writer.writeheader()
        writer.writerows(listaTrabajadores)

    print('El trabajador ha sido registrado con exito')


def menu():
    print(mn)
    print('1 . Registro de Trabjadores')
    print('2 . Listado de Trabajadores')
    print('3 . Buscar por Tipo')
    print('4 . Modificar Trabajador')
    print('5 . Eliminar Trabajador')
    print('6 . Salir')
    print(mn)

    while True:
        try:
            op = int(input('Ingrese la opcion deseada >\t'))
            if not op:
                print(mn)
                raise ValueError('La opcion no puede estar vacia')
            if op == 1:
                print(mn)
                registro()
            if op == 2:
                print(mn)
                listado()
            if op == 3:
                print(mn)
                buscar()
            if op == 4:
                print(mn)
                modificar()
            if op == 5:
                print(mn)
                eliminar()
            if op == 6:
                print(mn)
                print('Gracias por usar el sistema')
                system('cls')
                exit()

        except ValueError as e:
            print(f'{e}')


if __name__ == '__main__':
    menu()
