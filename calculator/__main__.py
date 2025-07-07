"""Command line interface for the calculator."""

import argparse
from .core import calculate


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculadora básica")
    parser.add_argument("operacion", choices=["sumar", "restar", "multiplicar", "dividir"], help="Operación a realizar")
    parser.add_argument("a", type=float, help="Primer número")
    parser.add_argument("b", type=float, help="Segundo número")
    args = parser.parse_args()

    try:
        resultado = calculate(args.a, args.b, args.operacion)
        print(f"Resultado: {resultado}")
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
