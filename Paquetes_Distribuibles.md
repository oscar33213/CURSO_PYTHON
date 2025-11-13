# CREAR PAQUETES DISTRIBUIBLES

- En la carpeta raíz, crear un archivo llamado **`setup.py`**.  
- Dentro de **`setup.py`**, indicar los siguientes parámetros:

```python
from setuptools import setup, find_packages

setup(
    name="OperacionesMatematicasBasicas",
    version="0.1.0",
    description="Paquete para realizar operaciones matemáticas básicas y complejas",
    author="Óscar Hidalgo Llopez©",
    author_email="oshill146@gmail.com",
    packages=find_packages(where="."),  # detecta todos los paquetes con __init__.py
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # ajusta según tu licencia
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.12",
    include_package_data=True,
) 
```

- En la consola indicamos lo siguiente: **python setup.py sdist**
- Si funciona, creara un archivo .tar

## INSTALACIÓN DE UN PAQUETE .tar

- Creamos el paquete y la carpeta **dist**

```bash
python setup.py sdist
```

- Entramos en el directorio donde tengamos el paquete (con cmd)

```bash

cd dist
```

- Instalamos pip (si no lo tenemos instalado) con:  

```bash
python.exe -m pip install --upgrade pip
```

- Instalamos el paquete

```bash
pip install nombre_del_paquete.tar.gz
```

## ACTUALIZACIÓN DE UN PAQUETE .tar

- En el **setup.py** añadimos la nueva versión

```bash
python setup.py sdist
```

- Navegamos hasta la carpeta /dist

```bash
cd dist
```

- Actualizamos el paquete:

```bash
pip install -- update nombre_del_paquete
```
