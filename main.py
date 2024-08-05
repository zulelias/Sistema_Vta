import os
import platform
from datetime import datetime
from gestion_ventas import VentaOnline, VentaLocal, SistemaGestionVtas

def limpiar_pantalla():
    '''Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')  # Para Linux/Unix/MacOS

def mostrar_menu():
    print("Sistema de Gestión de Ventas")
    print("1. Agregar Venta Online")
    print("2. Agregar Venta Local")
    print("3. Mostrar Venta")
    print("4. Actualizar Venta")
    print("5. Eliminar Venta")
    print("6. Mostrar Todas las Ventas")
    print("7. Borrar Todas las Ventas")
    print("8. Salir")

if __name__ == "__main__":
    sistema = SistemaGestionVtas('gestventas.json')

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1':            
            limpiar_pantalla()
            fecha = datetime.now()
            cliente = input("Ingrese el nombre del cliente: ")
            productos = input("Ingrese los productos vendidos (separados por comas): ").split(",")
            direccion_envio = input("Ingrese la dirección de envío: ")
            metodo_pago = input("Ingrese el método de pago: ")

            venta_online = VentaOnline(fecha, cliente, productos, direccion_envio, metodo_pago)
            sistema.agregar_venta(venta_online)
            print("Venta online agregada exitosamente.")
            input("Presione Enter para continuar...")

        elif opcion == '2':
            limpiar_pantalla()
            fecha = datetime.now()
            cliente = input("Ingrese el nombre del cliente: ")
            productos = input("Ingrese los productos vendidos (separados por comas): ").split(",")
            cajero = input("Ingrese el nombre del cajero: ")
            tienda = input("Ingrese el nombre de la tienda: ")
            venta_local = VentaLocal(fecha, cliente, productos, cajero, tienda)
            sistema.agregar_venta(venta_local)
            print("Venta local agregada exitosamente.")
            input("Presione Enter para continuar...")

        elif opcion == '3':
            limpiar_pantalla()
            try:
                index = int(input("Ingrese el índice de la venta a mostrar: "))
                venta = sistema.obtener_venta(index)
                if venta:
                    print(venta)
            except ValueError:
                print("Índice inválido.")
            input("Presione Enter para continuar...")

        elif opcion == '4':
            limpiar_pantalla()
            try:
                index = int(input("Ingrese el índice de la venta a actualizar: "))
                tipo = input("¿Es una venta online (1) o local (2)? ")
                fecha = datetime.now()
                cliente = input("Ingrese el nombre del cliente: ")
                productos = input("Ingrese los productos vendidos (separados por comas): ").split(",")
                if tipo == '1':
                    direccion_envio = input("Ingrese la dirección de envío: ")
                    metodo_pago = input("Ingrese el método de pago: ")
                    venta_online = VentaOnline(fecha, cliente, productos, direccion_envio, metodo_pago)
                    sistema.actualizar_venta(index, venta_online)
                elif tipo == '2':
                    cajero = input("Ingrese el nombre del cajero: ")
                    tienda = input("Ingrese el nombre de la tienda: ")
                    venta_local = VentaLocal(fecha, cliente, productos, cajero, tienda)
                    sistema.actualizar_venta(index, venta_local)
                print("Venta actualizada exitosamente.")
            except ValueError:
                print("Índice inválido.")
            input("Presione Enter para continuar...")

        elif opcion == '5':
            limpiar_pantalla()
            try:
                index = int(input("Ingrese el índice de la venta a eliminar: "))
                sistema.eliminar_venta(index)
                print("Venta eliminada exitosamente.")
            except ValueError:
                print("Índice inválido.")
            input("Presione Enter para continuar...")

        elif opcion == '6':
            limpiar_pantalla()
            for i, venta in enumerate(sistema.ventas):
                print(f"{i}: {venta}")
            input("Presione Enter para continuar...")

        elif opcion == '7':
            limpiar_pantalla()
            sistema.borrar_todas_ventas()
            input("Presione Enter para continuar...")

        elif opcion == '8':
            print('Saliendo del programa...')
            break

        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-8)')
            input("Presione Enter para continuar...")