# inicio importar datos

import csv
import random
import os
import time

from os import system

# fin importar datos


mn = '='*30
file = ('fileregistro.csv')
cargos = ['CEO', 'Analista de datos', 'Programador', 'Desarrollador']
listaTrabajadores = []
encabezado = ['id_Trabajador', 'Nombre', 'Apellido', 'Edad', 'Cargo']


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
        "id_Trabajador": id_trabajador,
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

    with open(ruta, 'w', newline='') as file_input:
        file_input.seek(0)
        writer = csv.DictWriter(file_input, fieldnames=encabezado)
        writer.writeheader()
        writer.writerows(listaTrabajadores)

    print('El trabajador ha sido registrado con exito')
    enter = input('Presione enter para continuar')
    system('cls')


def listado():
    print(mn)
    ruta = r"D:\\WorkSpace\\worksspace\\registroTrabajadores\\listcsv.csv"

    with open(ruta, 'r', newline='') as file_reader:
        reader = csv.DictReader(file_reader, dialect='excel', delimiter=',')
        reader.fieldnames
        print(', '.join(reader.fieldnames))
        for row in reader:
            print(f'{row["id_Trabajador"]} {row["Nombre"]} {
                  row["Apellido"]} {row["Edad"]} {row["Cargo"]}')
        enter = input('Presione enter para continuar')
        system('cls')


def buscar():
    print(mn)
    ruta = r"D:\\WorkSpace\\worksspace\\registroTrabajadores\\listcsv.csv"
    with open(ruta, 'r', newline='') as file_reader:
        reader = csv.DictReader(file_reader, dialect='excel', delimiter=',')
        reader.fieldnames
        print(', '.join(reader.fieldnames))
        while True:
            try:
                tipo = input(f'Ingrese el tipo de cargo {cargos} >\t')
                if tipo not in cargos or not tipo.strip():
                    print(mn)
                    print('el cargo no es valido')
                    raise ValueError('El campo no puede estar vacio')
                break
            except ValueError as e:
                print(f'{e}')
        for row in reader:
            if row['Cargo'] == tipo:
                print(f'{row["id_Trabajador"]} {row["Nombre"]} {
                    row["Apellido"]} {row["Edad"]} {row["Cargo"]}')

        print(mn)
        enter = input('Presione enter para continuar')
        system('cls')


def modificar():
    ruta = r"D:\\WorkSpace\\worksspace\\registroTrabajadores\\listcsv.csv"
    temp_file = r"D:\\WorkSpace\\worksspace\\registroTrabajadores\\Temp.csv"

    nombreModificar = input(
        'Ingrese el nombre del trabajdor a modificar>\t').strip()
    filas = []
    trabajador_encontrado = False
    try:
        with open(ruta, 'r', newline='')as file_modify:
            reader = csv.DictReader(
                file_modify, dialect='excel', delimiter=',')
            reader.fieldnames
            print(', '.join(reader.fieldnames))

            for row in reader:
                if row['Nombre'].strip() == nombreModificar:
                    nombre = input('Ingrese el nuevo nombre >\t').strip()
                    apellido = input('Ingrese el nuevo apellido >\t').strip()
                    edad = int(input('Ingrese la nueva edad >\t'))
                    cargo = input('Ingrese el nuevo cargo >\t').strip()

                    if nombre:
                        row["Nombre"] = nombre
                    if apellido:
                        row["Apellido"] = apellido
                    if edad:
                        row["Edad"] = edad
                    if cargo:
                        row["Cargo"] = cargo
                    trabajador_encontrado = True
                filas.append(row)
    except PermissionError as e:
        print(f'{e} , no se puede modificar el archivo, porque se encuentra abierto')
        print('cierre el archivo y vuelva a intentarlo')
        return

    if not trabajador_encontrado:
        print(mn)
        print('tarbajador no encontrado')
        return
    with open(temp_file, 'w', newline='')as file_modify:
        write = csv.DictWriter(
            file_modify, fieldnames=reader.fieldnames, dialect='excel', delimiter=',')
        write.writeheader()
        write.writerows(filas)

        # esperar 1 segundo para que el usuario pueda leer el mensaje
        time.sleep(2)

    os.remove(ruta)  # borrar el archivo original
    os.rename(temp_file, ruta)  # renombrar el archivo temporal

    print('El trabajador ha sido modificado con exito')
    enter = input('Presione enter para continuar')
    system('cls')


def eliminar():
    ruta = r"D:\\WorkSpace\\worksspace\\registroTrabajadores\\listcsv.csv"
    temp_file = r"D:\\WorkSpace\\worksspace\\registroTrabajadores\\Temp.csv"
    nombreEliminar = input(
        'Ingrese el nombre del trabajador a eliminar>\t').strip()
    filas = []
    trabajador_encontrado = False
    nombreEliminar = input(
        'Ingrese el nombre y apellido del trabajador a elminar >\t').strip()

    with open(ruta, 'r', newline='')as file_eliminar:
        reader = csv.DictReader(file_eliminar, dialect='excel', delimiter=',')


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
                print('Registro de Trabajadores')
                print(mn)
                registro()
            if op == 2:
                print(mn)
                print('Listado de Trabajadores')
                print(mn)
                listado()
            if op == 3:
                print(mn)
                system('cls')
                buscar()
            if op == 4:
                print(mn)
                system('cls')
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
