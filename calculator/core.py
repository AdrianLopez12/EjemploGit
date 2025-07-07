"""Core arithmetic operations for the calculator."""

from typing import Callable


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b


OPERATIONS: dict[str, Callable[[float, float], float]] = {
    "sumar": add,
    "restar": subtract,
    "multiplicar": multiply,
    "dividir": divide,
}


def calculate(a: float, b: float, operation: str) -> float:
    if operation not in OPERATIONS:
        raise ValueError("Operación no soportada.")
    return OPERATIONS[operation](a, b)
