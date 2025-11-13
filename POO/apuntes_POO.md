
# 🧠 Programación Orientada a Objetos (POO)

- Consiste en trasladar la naturaleza de los objetos de la vida real al código.  
- Su naturaleza se puede definir en su **comportamiento**, su **estado** y sus **propiedades**.  
- Las características se resumen en **propiedades**.  
- El **comportamiento** es “lo que puede hacer”.

---

## 🚗 Ejemplo: Coche

- **Estado del coche:** Parado, Circulando, Aparcando  
- **Propiedades del coche:** Color, Peso, Tamaño...  
- **Comportamiento del coche:** Arrancar, Frenar...

---

## 📘 Términos de obligado conocimiento

### 🧱 Clase

- Modelo donde se redactan las características comunes del objeto.  
- **Ejemplo:** de construccion de clase

``` python
class Coche:
  #Constructor o setter
  __init__(self, color, tamaño)
    self.color = color
    self.tamaño = tamaño
  #Metodo
  def getinfo(self)
    return f"\nColor: {self.color}\nTamaño: {self.tamaño}

```

---

### 🚙 Instancia u Objeto

- Comparten una misma clase.  
- **Ejemplo:** Coches que comparten un mismo chasis, pero diferentes modelos.

#### Los objetos

- **Propiedades (atributos):**
  - Atributos del coche:
    - Color  
    - Peso  
    - Alto  
    - Largo  

- **Comportamiento (métodos):**
  - Comportamiento del coche:
    - Acelerar  
    - Frenar  
    - Girar  

- Ejemplo de Instancia:

```python

coche1 = Coche("Color", 123)
print(coche1.getinfo())

```

---

### 🧩 Modularización

- Cuando se crea un código complejo, este se puede separar en bloques pero funcionando como una unidad.  
- En el contexto de la POO, se pueden dividir en varias **clases**.  
- Existe la **reutilización de bloques de código**, es decir, si necesitas en otro programa usar un bloque que ya existe, puedes reutilizarlo fácilmente.

---

### 🔒 Encapsulamiento

- Consiste en **encapsular o proteger información** dentro del objeto.  
- **Ejemplo (Coche):** Las piezas ocultas debajo del coche —a las que solo accede el mecánico— son parte del sistema, pero un usuario normal no puede modificarlas.  
- En programación, esto se traduce en **partes del código que no son accesibles para cualquiera**, solo para el programador o mediante métodos específicos.
- Ejemplo de Encapsulación

```python

class Coche:
  _color = ""
  _tamaño = ""
  __init__(self, color, tamaño)
    self._color = color
    self._tamaño = tamaño

```

---

### ⚙️ Nomenclatura del Punto

- **Clase:** `Coche`

#### Ejemplos

- `Coche.color = "rojo"` → Define un **atributo** (propiedad).  
- `Coche.arranca()` → Llama a un **método** (comportamiento) del objeto.

---

### 🧬 Herencia de clases

- Una clase hereda los **métodos y propiedades** de la clase padre.  
- Sirve para la **reutilización de código** en caso de crear objetos similares.  
- Una clase **hereda solo de la clase padre**.
- Las clases que se encuentran mas abajo **son las mas potentes**.
- Ejempo de herencia:

```python
class Coche:
  def __init__(self, color, tamaño)
    self.color = color
    self.tamaño = tamaño
  def getinfo(self)
    return f"\nColor: {self.color}\nTamaño: {self.tamaño}

class Moto (Coche):
  def __init__(self, color, tamaño, isAutomatica)
    super().__init__(self, color, tamaño)

```

---

### 🌀 Polimorfismo

- El **polimorfismo** ocurre cuando un objeto de una clase puede **adoptar diferentes comportamientos** durante la ejecución de un programa.  
- Se presenta principalmente cuando se trabaja con **herencias**, ya que las clases hijas pueden redefinir métodos de la clase padre.  

---

#### 🧩 Ejemplo

```python
def hazlosHablar(lista):
    for persona in lista:
        print(persona.hablar()) ´´´


- En este ejemplo es **persona** quien va variando 
 
