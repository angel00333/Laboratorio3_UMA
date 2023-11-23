from datetime import datetime

class Carro:

    def __init__(self, marca, modelo, num_asientos, color, tipo, tipo_combustible, precio, años_garantia, fecha_de_ingreso):
        self.marca = marca
        self.modelo = modelo
        self.num_asientos = num_asientos
        self.color = color
        self.tipo = tipo
        self.tipo_combustible = tipo_combustible
        self.precio = precio
        self.años_garantia = años_garantia
        self.fecha_de_ingreso = fecha_de_ingreso

    def informacion_carro(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Asientos: {self.num_asientos}")
        print(f"Color: {self.color}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio: ${self.precio}")
        print(f"Garantia: {self.años_garantia} años")
        print(f"Fecha: {self.fecha_de_ingreso.strftime('%d-%B-%Y')}")
        print()

print("-------Ejemplos dados-------")
Primer_Carro = Carro("Toyota", "Yaris", 5, "Gris metalico", "Sedan", "Gasolina", 24000, 10, datetime(2022, 8, 9))
Segundo_Carro = Carro("Nissan", "Frontier", 5, "Rojo", "Pickup", "Gasolina", 44900, 3, datetime(2022, 8, 23))


Primer_Carro.informacion_carro()
Segundo_Carro.informacion_carro()

print("-------Mis ejemplos------")
Tercer_Carro = Carro("Kia", "Ceed", 5, "Negro", "Sedan", "Gasolina", 54200, 5, datetime(2022, 8, 14))
Cuarto_Carro = Carro("Toyota", "Tacoma",4, "Cafe plateado", "Sedan", "Hibrido", 56000, 1, datetime(2023, 4, 8))
Quinto_Carro = Carro("Nissan", "Pathfinder",5, "Blanco", "Sedan", "Diesel", 21000, 7, datetime(2022, 7, 6))
Sexto_Carro = Carro("Mitsubishi", "Colt pequeño",5, "Rojo", "Pickup", "Diesel", 64000, 6, datetime(2023, 4, 6))

Tercer_Carro.informacion_carro()
Cuarto_Carro.informacion_carro()
Quinto_Carro.informacion_carro()
Sexto_Carro.informacion_carro()