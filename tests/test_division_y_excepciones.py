"""Tests para la función div(a, b) -> float y sus excepciones."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 2.5),    # Resultado decimal(float)
    (-10, 2, -5.0), # Numerador negativo
    (10, -2, -5.0), # Denominador negativo
    (-10, -2, 5.0)  # Ambos negativos
])

def test_div_parametrizado(a, b, expected):
    """Prueba múltiples casos de división en una sola función."""
    assert div(a, b) == expected

def test_div_por_cero():
    """Verifica que se lance ZeroDivisionError al dividir por0."""
    with pytest.raises(ZeroDivisionError):
        div(10, 0)