import random

# -------------------- CLASES --------------------

class Vehiculo:
    tipo = "Vehículo genérico"
    icono = "🚘"

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
        aire=None,
    ):
        print(f"\n--- Construyendo un {self.tipo} {self.icono} ---")
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
            f"\n[{self.icono} {self.tipo}]"
            f"\n🎨 Color: {self.colorVehiculo}"
            f"\n🛞 Ruedas: {self.numRuedas}"
            f"\n📦 Carga Del Vehiculo: {self.cargaTotal} kg"
            f"\n🏎️ Cilindrada: {self.cilindradaVehiculo}"
            f"\n📏 Ancho del Chasis: {self.anchoChasis} m"
            f"\n📐 Alto del Vehiculo: {self.altoVehiculo} m"
            f"\n⚙️ Numero de Marchas: {self.numMarchas}"
            f"\n💺 Numero de Asientos: {self.numAsientos}"
            f"\n❄️ Aire acondicionado: {aire_texto}."
        )

    # Métodos de comportamiento con emojis
    def Arrancar(self):
        return f"{self.icono} 🚦 Arranca" if random.randint(0, 100) < 50 else f"{self.icono} 💥 Calado"

    def Acelerar(self):
        return f"{self.icono} 🏁 Acelera"

    def Frenar(self):
        return f"{self.icono} 🛑 Frena"

    def Saltar(self):
        return f"{self.icono} 🦘 Salta"

    def Cargar(self):
        return f"{self.icono} 📦 El vehiculo carga {self.cargaTotal} KG"

    def Derrapar(self):
        return f"{self.icono} 💨 Derrapa"

    def Girar(self):
        return f"{self.icono} ↪️ Gira a la derecha" if random.randint(0, 100) < 50 else f"{self.icono} ↩️ Gira a la izquierda"

    def MarchaAtras(self):
        return f"{self.icono} 🔄 Marcha Atras"

    def NumDeRuedas(self):
        return f"{self.icono} 🛞 El vehiculo tiene {self.numRuedas} ruedas"

    def EncenderAire(self):
        return f"{self.icono} ❄️ El aire acondicionado se ha encendido." if self.aire else f"{self.icono} Este vehículo no tiene aire acondicionado."


class Coche(Vehiculo):
    tipo = "Coche"
    icono = "🚗"

    def __init__(self, tipo_carroceria=None, **kwargs):
        super().__init__(**kwargs)
        if tipo_carroceria is None:
            tipo_carroceria = input("Indica el tipo de carrocería (sedán, SUV, etc.): ")
        self.tipo_carroceria = tipo_carroceria

    def getInfoVehiculo(self):
        return super().getInfoVehiculo() + f"\n🚗 Tipo de carrocería: {self.tipo_carroceria}"


class Furgoneta(Coche):
    tipo = "Furgoneta"
    icono = "🚚"

    def __init__(self, volumen_carga=None, **kwargs):
        super().__init__(**kwargs)
        if volumen_carga is None:
            volumen_carga = float(input("Indica el volumen de carga en m³: "))
        self.volumen_carga = volumen_carga

    def getInfoVehiculo(self):
        return super().getInfoVehiculo() + f"\n📦 Volumen de carga: {self.volumen_carga} m³"


class Bicicleta(Vehiculo):
    tipo = "Bicicleta"
    icono = "🚲"

    def __init__(self, material_cuadro=None, **kwargs):
        if "numRuedas" not in kwargs:
            kwargs["numRuedas"] = 2
        super().__init__(**kwargs)
        if material_cuadro is None:
            material_cuadro = input("Indica el material del cuadro (aluminio, carbono, acero...): ")
        self.material_cuadro = material_cuadro
        self.numRuedas = 2

    def getInfoVehiculo(self):
        return super().getInfoVehiculo() + f"\n🔧 Material del cuadro: {self.material_cuadro}"


# Moto hereda de Coche y Bicicleta
class Moto(Coche, Bicicleta):
    tipo = "Moto"
    icono = "🏍️"

    def __init__(self, tiene_electronica=None, **kwargs):
        super().__init__(**kwargs)
        if tiene_electronica is None:
            tiene_electronica = input("¿Tiene electrónica avanzada (s/n)?: ").strip().lower() == "s"
        self.tiene_electronica = tiene_electronica

    def getInfoVehiculo(self):
        tiene_elec = "Sí" if self.tiene_electronica else "No"
        return super().getInfoVehiculo() + f"\n💻 Electrónica avanzada: {tiene_elec}"


# -------------------- SELECCIÓN DE VEHÍCULO --------------------

tipos_vehiculo = {
    "1": Coche,
    "2": Moto,
    "3": Furgoneta,
    "4": Bicicleta,
    "5": Vehiculo
}

print("Selecciona el tipo de vehículo a construir:")
print("1) Coche 🚗")
print("2) Moto 🏍️")
print("3) Furgoneta 🚚")
print("4) Bicicleta 🚲")
print("5) Vehículo genérico 🚘")

opcion = input("Elige una opción (1-5): ").strip()

if opcion in tipos_vehiculo:
    ClaseVehiculo = tipos_vehiculo[opcion]
    vehiculo = ClaseVehiculo()
    print("\n--- Información del vehículo construido ---")
    print(vehiculo.getInfoVehiculo())

    # Ejemplo de métodos con emojis
    print("\n--- Ejemplos de acciones del vehículo ---")
    print(vehiculo.Arrancar())
    print(vehiculo.Acelerar())
    print(vehiculo.Frenar())
    print(vehiculo.Cargar())
else:
    print("Opción no válida.")

