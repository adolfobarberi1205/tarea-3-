class Empleado:
    def __init__(self, nombre, cedula, rol, balance):
        self.nombre = nombre
        self.cedula = cedula
        self.rol = rol
        self.balance = balance

    def retirar_dinero(self, cantidad):
        if cantidad > self.balance:
            print("No hay suficiente saldo para retirar.")
        else:
            self.balance -= cantidad
            print("Retiro exitoso. Saldo actual: ", self.balance)

    def pagar_salario(self, cantidad):
        self.balance += cantidad
        print("Pago de salario exitoso. Saldo actual: ", self.balance)


class Nomina:
    def __init__(self, presupuesto):
        self.presupuesto = presupuesto
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        print("Lista de empleados:")
        for empleado in self.empleados:
            print(empleado.nombre, empleado.cedula, empleado.rol, empleado.balance)

    def pagar_nomina(self):
        total_a_pagar = 0
        for empleado in self.empleados:
            if empleado.rol == "Programador Junior":
                cantidad_a_pagar = 1000
            elif empleado.rol == "Programador Senior":
                cantidad_a_pagar = 2000
            elif empleado.rol == "Manager":
                cantidad_a_pagar = 3000
            else:
                cantidad_a_pagar = 0
                print("Rol de empleado no válido.")
            total_a_pagar += cantidad_a_pagar
            empleado.pagar_salario(cantidad_a_pagar)
        if total_a_pagar > self.presupuesto:
            print("No hay suficiente presupuesto para pagar a todos los empleados.")
        else:
            self.presupuesto -= total_a_pagar
            print("Pago de nómina exitoso. Presupuesto actual: ", self.presupuesto)

    def agregar_presupuesto(self, cantidad):
        self.presupuesto += cantidad
        print("Presupuesto actualizado. Presupuesto actual: ", self.presupuesto)



nomina = Nomina(5000)


while True:
    print("1. Agregar empleado")
    print("2. Mostrar empleados")
    print("3. Pagar nómina")
    print("4. Agregar presupuesto")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        nombre = input("Ingrese el nombre del empleado: ")
        cedula = input("Ingrese la cédula del empleado: ")
        rol = input("Ingrese el rol del empleado: ")
        balance = int(input("Ingrese el balance actual del empleado: "))
        empleado = Empleado(nombre, cedula, rol, balance)
        nomina.agregar_empleado(empleado)
    elif opcion == 2:
        nomina.mostrar_empleados()
    elif opcion == 3:
        nomina.pagar_nomina()
    elif opcion == 4:
        cantidad = int(input("Ingrese la cantidad a agregar al presupuesto: "))
        nomina.agregar_presupuesto(cantidad)
    elif opcion == 5:
        break
    else:
        print("Opción no válida. Intente de nuevo.")