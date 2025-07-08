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

## Conversor de UTC a hora de Ecuador

En el directorio `utc_to_ecuador` se incluye una pequeña aplicaci\u00f3n HTML/JavaScript que permite convertir cualquier hora UTC a la hora de Ecuador (UTC-5).

Para probarla localmente solo abra el archivo `index.html` en su navegador.

Si desea publicarla con **GitHub Pages**, suba estos archivos al repositorio y active la funci\u00f3n *Pages* en la configuraci\u00f3n del repositorio. GitHub generar\u00e1 un enlace web p\u00fablico para acceder a la aplicaci\u00f3n.
