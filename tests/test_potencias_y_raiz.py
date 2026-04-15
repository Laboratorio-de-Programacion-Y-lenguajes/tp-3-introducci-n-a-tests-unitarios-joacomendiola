"""Tests para la función pow_(a, b) -> float y sqrt(x)."""

import pytest

from src.calculator import pow_, sqrt

# --- TESTS PARA POTENCIA (pow_) ---

# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8

def test_pow_cualquier_numero_elevado_a_cero():
    """Cualquier número elevado a 0 debe dar 1."""
    assert pow_(5, 0) == 1
    assert pow_(-3, 0) == 1
    assert pow_(0, 0) == 1

def test_pow_numero_elevado_a_uno():
    """Número elevado a 1 debe dar el mismo número."""
    assert pow_(7, 1) == 7
    assert pow_(-4, 1) == -4
    assert pow_(0, 1) == 0

def test_pow_base_negativa_exponente_par():
    """Base negativa con exponente par debe dar resultado positivo."""
    assert pow_(-2, 4) == 16
    assert pow_(-3, 2) == 9

def test_pow_exponente_decimal():
    """Exponente decimal, ej: 9 ** 0.5 debe dar 3."""
    assert pow_(9, 0.5) == 3
    assert pow_(16, 0.25) == 2


@pytest.mark.parametrize("a, b, esperado", [
    (2, 0, 1),         # Cualquier numero elevado a 0 da 1
    (6, 1, 6),         # Cualquier número elevado a 1 da el mismo numero 
    (-5, 2, 25),       # Base negativa con exponente par debe resultado positivo
    (9, 0.5, 3),       # Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
])
def test_pow_parametrizado(a, b, esperado):
    """Prueba multiples casos de potencia en una sola función usando @pytest.mark.parametrize."""
    assert pow_(a, b) == esperado


# --- TESTS PARA RAÍZ CUADRADA (sqrt) ---

# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


def test_sqrt_cero():
    """La raíz de 0 debe dar 0.0."""
    assert sqrt(0) == 0.0

def test_sqrt_no_cuadrado_perfecto():
    """La raiz de un numero que no es cuadrado perfecto debe dar resultado decimal."""
    assert sqrt(2) == pytest.approx(1.414213562373095)
    assert sqrt(3) == pytest.approx(1.7320508075688772)

def test_sqrt_numero_negativo():
    """La raiz de un numero negativo debe lanzar ValueError."""
    with pytest.raises(ValueError):
        sqrt(-4)