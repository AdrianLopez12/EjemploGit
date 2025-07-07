# Calculadora en Python

Este proyecto implementa una calculadora simple utilizando Python. Incluye un
módulo reutilizable, una interfaz de línea de comandos y un pequeño servidor web
basado en Flask.

## Instalación

Se recomienda crear un entorno virtual y luego instalar las dependencias:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Uso desde la línea de comandos

Ejecute operaciones básicas directamente con:

```bash
python -m calculator sumar 2 3
```

Las operaciones disponibles son `sumar`, `restar`, `multiplicar` y `dividir`.

## Servidor Web

Para iniciar la versión web ejecute:

```bash
python -m calculator.server
```

Luego abra `http://localhost:5000` en su navegador para utilizar la calculadora
a través de una interfaz web.
