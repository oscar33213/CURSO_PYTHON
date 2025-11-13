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

- Entramos en el directorio donde tengamos el paquete (con cmd)
- Instalamos pip (si no lo tenemois instalado con: **'python.exe -m pip install --upgrade pip'**)
- Una vez instalado, instalamos el paquete con el siguiente comando:  **'pip install nombre_del_paquete'**
- Ejemplo:

```bash

python setup.py sdist
cd dist
pip install nombre_del_paquete.tar.gz
```

## ACTUALIZACIÓN DE UN PAQUETE .tar

- En el **setup.py** añadimos la nueva versión
- En la consola creamos otro paquete distribuible con **python setup.py sdist**
- Navegamos hasta la carpeta /dist y lo actualizamos con: **'pip install -- update nombre_del_paquete'**
