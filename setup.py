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
