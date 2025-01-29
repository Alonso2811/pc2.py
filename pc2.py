class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = set()

class Bus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horarios = set()
        self.conductor = None

class Admin:
    def __init__(self):
        self.buses = {} 
        self.conductores = {}
    
    def menu(self):
        while True:
            op = input("1.Agregar Bus\n2.Agregar Ruta\n3.Registrar Horario\n4.Agregar Conductor\n5.Asignar Bus\n6.Salir\n")
            if op == "1":
                bus_id = input("ID Bus: ")
                self.buses[bus_id] = Bus(bus_id)
            elif op == "2":
                bus = self.buses.get(input("ID Bus: "))
                if bus: bus.ruta = input("Ruta: ")
            elif op == "3":
                bus = self.buses.get(input("ID Bus: "))
                if bus: bus.horarios.add(input("Horario: "))
            elif op == "4":
                nombre = input("Nombre: ")
                self.conductores[nombre] = Conductor(nombre)
            elif op == "5":
                bus = self.buses.get(input("ID Bus: "))
                conductor = self.conductores.get(input("Nombre: "))
                if bus and conductor: bus.conductor = conductor
            elif op == "6":
                break
            else:
                print("Opción inválida")

if __name__ == "__main__":
    Admin().menu()
