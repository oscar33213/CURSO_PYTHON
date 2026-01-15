# PANDAS

## ¿QUÉ ES PANDAS?

- Proviene del nombre **Pan**el **Da**ta
- Libreria de codigo abierto usada por cientificos y analistas de datos
- **Creada en 2008** por la necesidad de analizar **grades volumenes de datos**
- Cuenta con una extructura flexible
- Es usada en diferetes areas:
  - Analitica
  - Estadistica
  - Economia
  - Banca
  - *Etc*

- Ventajas:
  - Reducción de lineas de codigo
  - Especilmente diseñada para analisis de grandes volumenes de datos
  - Documentación API de facil compresión
  - Integra **Matplotlib** para graficos
  - Copatibilidad con **Numpy**

'''

## USO DE PANDAS

- Para empezar a usar **Pandas** deberemos tener instalda su libreria pertinente
- Para comprobarlo (si nunca lo has usado, lo logico es no tenerlo) en un arhivo *.py* importaremos

```python
import pandas as pd 
```

- Si se importa bien, tenemos la libreria instalada
- Si no se importa, deberemos instalarla

```bash
pip install pandas

```

- Codigo sencillo de Pandas

```python
import pandas as pd

df = pd.DataFrame({'num_legs': [2,4], 'num_wings': [2,0]}, index= ['falcon', 'dog'])

print(df)
```

- Lo que mostrara por consola

```bash
num_legs  num_wings
falcon         2          2
dog            4          0
```

- El manejo de **DataFrame** nos permite:

  - Carga de datos de diferentes origenes
  - No permite trabajar asemejandonos a una tabla dinamica
  - Tranformación de datos
  - Calculos por **filas** y/o **columnas**
  - Analisis de datos visuales *(Graficos, lineas...)*
  - Exportaciones de datos
