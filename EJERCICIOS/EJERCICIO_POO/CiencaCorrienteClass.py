class CuentaCorriente:
    def __init__(self):
        # Todos los datos se introducen por consola
        self.__numCuenta = input("🔢 Introduce el número de cuenta: ")
        self.__titularCuenta = input("👤 Introduce el titular de la cuenta: ")
        self.__saldoCuenta = float(input("💰 Introduce el saldo inicial (€): "))

    # --- GETTERS ---
    def get_numCuenta(self):
        return self.__numCuenta

    def get_titularCuenta(self):
        return self.__titularCuenta

    def get_saldoCuenta(self):
        return self.__saldoCuenta

    # --- SETTERS ---
    def set_numCuenta(self, numCuenta):
        self.__numCuenta = numCuenta

    def set_titularCuenta(self, titularCuenta):
        self.__titularCuenta = titularCuenta

    def set_saldoCuenta(self, saldo):
        if saldo >= 0:
            self.__saldoCuenta = saldo
        else:
            print("❌ El saldo no puede ser negativo.")

    # --- MÉTODOS FUNCIONALES ---
    def getInfoCuenta(self):
        return f"\n📄 Información de la cuenta:\nNúmero: {self.__numCuenta}\nTitular: {self.__titularCuenta}\nSaldo disponible: {self.__saldoCuenta} €"

    def ingresarDinero(self):
        dineroIntroducido = float(input("💶 Indica el dinero a introducir: "))
        while dineroIntroducido < 0:
            print("❌ Solo valores positivos")
            dineroIntroducido = float(input("💶 Indica el dinero a introducir: "))
            break
        self.__saldoCuenta += dineroIntroducido
        print(f"✅ Ingreso realizado. Nuevo saldo: {self.__saldoCuenta} €")

    def retirarDinero(self):
        dineroRetirado = float(input("💸 Indique el dinero a retirar: "))
        while dineroRetirado > self.__saldoCuenta:
            print("⚠️ Saldo insuficiente.")
            dineroRetirado = float(input("💸 Indique el dinero a retirar: "))
            break

        self.__saldoCuenta -= dineroRetirado
        print(f"✅ Retirada realizada. Nuevo saldo: {self.__saldoCuenta} €")


# ---------- Nueva clase Cuenta_Joven ----------
class Cuenta_Joven(CuentaCorriente):
    def __init__(self):
        # Llamamos al constructor de la clase base (pide número, titular y saldo)
        super().__init__()

        # Pedimos el bonus promocional en porcentaje (como en tu intento original)
        # Guardamos tanto el porcentaje como el importe en euros
        try:
            porcentaje = float(input("🎁 Indica el bonus en % (ej. 10 para 10%). Si no hay, escribe 0: "))
        except ValueError:
            print("❌ Valor no válido para el bonus. Se asigna 0%.")
            porcentaje = 0.0

        if porcentaje < 0:
            print("❌ El porcentaje no puede ser negativo. Se asigna 0%.")
            porcentaje = 0.0

        self.__bonus_promo_percent = porcentaje

        # Calculamos el importe del bonus en euros y lo aplicamos al saldo mediante los getters/setters
        saldo_actual = self.get_saldoCuenta()
        bonus_importe = saldo_actual * (self.__bonus_promo_percent / 100.0)
        self.__bonus_promo_importe = round(bonus_importe, 2)  # redondear a 2 decimales

        # Actualizamos el saldo usando el setter (para respetar la encapsulación)
        nuevo_saldo = saldo_actual + self.__bonus_promo_importe
        self.set_saldoCuenta(nuevo_saldo)

        # Mensaje informativo
        if self.__bonus_promo_importe > 0:
            print(f"✅ Bonus aplicado: {self.__bonus_promo_importe} € ({self.__bonus_promo_percent}%). Nuevo saldo: {self.get_saldoCuenta()} €")
        else:
            print("ℹ️ No se aplicó bonus promocional.")

    # Método para devolver el importe del bonus (en euros)
    def getBonus(self):
        return self.__bonus_promo_importe

    # ingresarDinero() y retirarDinero() se heredan directamente de CuentaCorriente

    # Sobrescribimos getInfoCuenta para incluir el bonus
    def getInfoCuenta(self):
        datos_base = super().getInfoCuenta()
        return f"{datos_base}\nBonus promoción: {self.__bonus_promo_importe} € ({self.__bonus_promo_percent} %)"


# --- Ejemplo de uso ---

# Mantengo tu ejemplo original de CuentaCorriente
persona1 = CuentaCorriente()
print(persona1.getInfoCuenta())  # Mostrar información inicial
persona1.ingresarDinero()        # Ingreso
persona1.retirarDinero()         # Retirada
print(persona1.getInfoCuenta())  # Mostrar información final

# Ejemplo adicional para Cuenta_Joven (se pueden comentar si no se desean ejecutar)
print("\n--- Creación de una Cuenta Joven ---")
persona_joven = Cuenta_Joven()
print(persona_joven.getInfoCuenta())
persona_joven.ingresarDinero()   # heredado
persona_joven.retirarDinero()    # heredado
print(persona_joven.getInfoCuenta())
