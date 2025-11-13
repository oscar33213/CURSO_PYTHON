import random

class Vehiculo:
    def __init__(
        self,
        colorVehiculo=None,
        numRuedas=None,
        cargaTotal=None,
        cilindradaVehiculo=None,
        anchoChasis=None,
        altoVehiculo=None,
        numMarchas=None,
        numAsientos=None,
        aire=None,  # True/False or None
    ):
        # Pedir sólo si es None
        if colorVehiculo is None:
            colorVehiculo = input("Indica el color del vehiculo: ")
        if numRuedas is None:
            numRuedas = int(input("Indica el numero de ruedas: "))
        if cargaTotal is None:
            cargaTotal = float(input("Indica el total de carga en KG: "))
        if cilindradaVehiculo is None:
            cilindradaVehiculo = int(input("Indica el numero de cilindrada: "))
        if anchoChasis is None:
            anchoChasis = float(input("Indica el ancho del chasis en metros: "))
        if altoVehiculo is None:
            altoVehiculo = float(input("Indica el alto del vehiculo en metros: "))
        if numMarchas is None:
            numMarchas = int(input("Indica el numero total de marchas del vehiculo: "))
        if numAsientos is None:
            numAsientos = int(input("Indica el numero de asientos: "))
        if aire is None:
            respuesta = input("Indica si el vehiculo tiene aire acondicionado (s/n): ").strip().lower()
            aire = respuesta == "s"

        self.colorVehiculo = colorVehiculo
        self.numRuedas = numRuedas
        self.cargaTotal = cargaTotal
        self.cilindradaVehiculo = cilindradaVehiculo
        self.anchoChasis = anchoChasis
        self.altoVehiculo = altoVehiculo
        self.numMarchas = numMarchas
        self.numAsientos = numAsientos
        self.aire = aire

    def getInfoVehiculo(self):
        aire_texto = "Sí" if self.aire else "No"
        return (
            f"\nInformación del vehiculo:"
            f"\nColor: {self.colorVehiculo}"
            f"\nRuedas: {self.numRuedas}"
            f"\nCarga Del Vehiculo: {self.cargaTotal} kg"
            f"\nCilindrada: {self.cilindradaVehiculo}"
            f"\nAncho del Chasis: {self.anchoChasis} m"
            f"\nAlto del Vehiculo: {self.altoVehiculo} m"
            f"\nNumero de Marchas: {self.numMarchas}"
            f"\nNumero de Asientos: {self.numAsientos}"
            f"\nAire acondicionado: {aire_texto}."
        )

    def get_colorVehiculo(self):
        return self.colorVehiculo

    def get_numRuedas(self):
        return self.numRuedas

    def get_cargaVehiculo(self):
        return self.cargaTotal

    def get_Cilindrada(self):
        return self.cilindradaVehiculo

    def get_AnchoVehiculo(self):
        return self.anchoChasis

    def get_AltoVehiculo(self):
        return self.altoVehiculo

    def get_NumMarchas(self):
        return self.numMarchas

    def get_Asientos(self):
        return self.numAsientos

    def get_AireAcon(self):
        return self.aire

    def Arrancar(self):
        numeroAleatorio = random.randint(0, 100)
        if numeroAleatorio < 50:
            return "Arranca"
        else:
            return "Calado"

    def Acelerar(self):
        return "Acelera"

    def Frenar(self):
        return "Frena"

    def Saltar(self):
        return "Salta"

    def Cargar(self):
        return f"El vehiculo carga {self.cargaTotal} KG"

    def Derrapar(self):
        return "Derrapa"

    def Girar(self):
        numeroAleatorio = random.randint(0, 100)
        if numeroAleatorio < 50:
            return "Gira a la derecha"
        else:
            return "Gira a la izquierda"

    def MarchaAtras(self):
        return "Marcha Atras"

    def NumDeRuedas(self):
        return f"El vehiculo tiene {self.numRuedas} ruedas"

    def EncenderAire(self):
        if self.aire:
            return "El aire acondicionado se ha encendido."
        else:
            return "Este vehículo no tiene aire acondicionado."


class Coche(Vehiculo):
    def __init__(self, tipo_carroceria=None, **kwargs):
        # kwargs pasan los parámetros base al padre; si faltan, el padre los pedirá
        super().__init__(**kwargs)
        if tipo_carroceria is None:
            tipo_carroceria = input("Indica el tipo de carrocería (sedán, SUV, etc.): ")
        self.tipo_carroceria = tipo_carroceria

    def getInfoVehiculo(self):
        info = super().getInfoVehiculo()
        return info + f"\nTipo de carrocería: {self.tipo_carroceria}"


class Moto(Vehiculo):
    def __init__(self, tiene_electronica=None, **kwargs):
        super().__init__(**kwargs)
        if tiene_electronica is None:
            tiene_electronica = input("¿Tiene electrónica avanzada (s/n)?: ").strip().lower() == "s"
        self.tiene_electronica = tiene_electronica

    def getInfoVehiculo(self):
        info = super().getInfoVehiculo()
        tiene_elec = "Sí" if self.tiene_electronica else "No"
        return info + f"\nElectrónica avanzada: {tiene_elec}"


class Furgoneta(Vehiculo):
    def __init__(self, volumen_carga=None, **kwargs):
        super().__init__(**kwargs)
        if volumen_carga is None:
            volumen_carga = float(input("Indica el volumen de carga en m³: "))
        self.volumen_carga = volumen_carga

    def getInfoVehiculo(self):
        info = super().getInfoVehiculo()
        return info + f"\nVolumen de carga: {self.volumen_carga} m³"


class Bicicleta(Vehiculo):
    def __init__(self, material_cuadro=None, **kwargs):
        # Forzamos 2 ruedas si no se pasa explícitamente
        if "numRuedas" not in kwargs:
            kwargs["numRuedas"] = 2
        super().__init__(**kwargs)
        if material_cuadro is None:
            material_cuadro = input("Indica el material del cuadro (aluminio, carbono, acero...): ")
        self.material_cuadro = material_cuadro
        self.numRuedas = 2

    def getInfoVehiculo(self):
        info = super().getInfoVehiculo()
        return info + f"\nMaterial del cuadro: {self.material_cuadro}"


def menu():
    print("\n--- Gestor de Vehículos ---")
    print("1) Crear Vehículo genérico")
    print("2) Crear Coche")
    print("3) Crear Moto")
    print("4) Crear Furgoneta")
    print("5) Crear Bicicleta")
    print("6) Listar vehículos creados")
    print("7) Salir")
    return input("Elige una opción (1-7): ").strip()


def main():
    vehiculos = []
    while True:
        opcion = menu()
        if opcion == "1":
            v = Vehiculo()
            vehiculos.append(v)
            print("Vehículo creado.")
        elif opcion == "2":
            c = Coche()
            vehiculos.append(c)
            print("Coche creado.")
        elif opcion == "3":
            m = Moto()
            vehiculos.append(m)
            print("Moto creada.")
        elif opcion == "4":
            f = Furgoneta()
            vehiculos.append(f)
            print("Furgoneta creada.")
        elif opcion == "5":
            b = Bicicleta()
            vehiculos.append(b)
            print("Bicicleta creada.")
        elif opcion == "6":
            if not vehiculos:
                print("No hay vehículos creados.")
            else:
                for i, veh in enumerate(vehiculos):
                    print(f"\n--- Vehículo #{i} ({veh.__class__.__name__}) ---")
                    print(veh.getInfoVehiculo())
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
