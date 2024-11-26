import sqlite3
conn = sqlite3.connect('vehiculos.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS vehiculos (
                    id INTEGER PRIMARY KEY,
                    modelo TEXT,
                    compania TEXT,
                    año INTEGER,
                    color TEXT,
                    tipo_motor TEXT,
                    precio REAL,
                    kilometraje REAL,
                    puertas INTEGER,
                    transmision TEXT)''')
conn.commit()
def agregar_vehiculo():
    modelo = input("Ingrese el modelo del vehículo: ")
    compania = input("Ingrese la compañía del vehículo: ")
    año = int(input("Ingrese el año del vehículo: "))
    color = input("Ingrese el color del vehículo: ")
    tipo_motor = input("Ingrese el tipo de motor (Ej. Gasolina, Eléctrico): ")
    precio = float(input("Ingrese el precio del vehículo: "))
    kilometraje = float(input("Ingrese el kilometraje del vehículo: "))
    puertas = int(input("Ingrese el número de puertas del vehículo: "))
    transmision = input("Ingrese el tipo de transmisión (Automática/Manual): ")
    
    cursor.execute('''INSERT INTO vehiculos 
                      (modelo, compania, año, color, tipo_motor, precio, kilometraje, puertas, transmision) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (modelo, compania, año, color, tipo_motor, precio, kilometraje, puertas, transmision))
    conn.commit()
    print("Vehículo agregado exitosamente.")
def mostrar_vehiculos():
    cursor.execute("SELECT * FROM vehiculos")
    vehiculos = cursor.fetchall()
    if vehiculos:
        for vehiculo in vehiculos:
            print(f"ID: {vehiculo[0]} - Modelo: {vehiculo[1]} - Compañía: {vehiculo[2]} - Año: {vehiculo[3]} - "
                  f"Color: {vehiculo[4]} - Motor: {vehiculo[5]} - Precio: {vehiculo[6]} - Kilometraje: {vehiculo[7]} - "
                  f"Puertas: {vehiculo[8]} - Transmisión: {vehiculo[9]}")
    else:
        print("No hay vehículos registrados.")
def modificar_vehiculo():
    mostrar_vehiculos()
    id_vehiculo = int(input("Ingrese el ID del vehículo a modificar: "))
    modelo = input("Ingrese el nuevo modelo: ")
    compania = input("Ingrese la nueva compañía: ")
    año = int(input("Ingrese el nuevo año: "))
    color = input("Ingrese el nuevo color: ")
    tipo_motor = input("Ingrese el nuevo tipo de motor: ")
    precio = float(input("Ingrese el nuevo precio: "))
    kilometraje = float(input("Ingrese el nuevo kilometraje: "))
    puertas = int(input("Ingrese el nuevo número de puertas: "))
    transmision = input("Ingrese el nuevo tipo de transmisión: ")
    
    cursor.execute('''UPDATE vehiculos SET modelo=?, compania=?, año=?, color=?, tipo_motor=?, precio=?, kilometraje=?, puertas=?, transmision=? 
                      WHERE id=?''', 
                   (modelo, compania, año, color, tipo_motor, precio, kilometraje, puertas, transmision, id_vehiculo))
    conn.commit()
    print("Vehículo modificado exitosamente.")

def eliminar_vehiculo():
    mostrar_vehiculos()
    id_vehiculo = int(input("Ingrese el ID del vehículo a eliminar: "))
    cursor.execute("DELETE FROM vehiculos WHERE id=?", (id_vehiculo,))
    conn.commit()
    print("Vehículo eliminado exitosamente.")
def mostrar_menu():
    print("\n----- Menú -----")
    print("1) Agregar (Alta)")
    print("2) Consulta (Mostrar)")
    print("3) Modificar (Editar)")
    print("4) Eliminar (Borrar)")
    print("5) Salir")
    opcion = input("Seleccione una opción: ")
    return opcion
while True:
    opcion = mostrar_menu()

    if opcion == '1':
        agregar_vehiculo()
    elif opcion == '2':
        mostrar_vehiculos()
    elif opcion == '3':
        modificar_vehiculo()
    elif opcion == '4':
        eliminar_vehiculo()
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")
conn.close()

