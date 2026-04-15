"""Tests para las funciones aritmeticas basicas (suma, resta, multiplicacion)."""

import pytest

from src.calculator import add, sub, mul

# --- TESTS PARA SUMA (add) ---

# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3

@pytest.mark.parametrize("a,b,expected", [
    (-1, -2, -3),  # Sumar dos números negativos    
    (5, -3, 2),    # Sumar un número positivo y uno negativo
    (0, 5, 5),     # Sumar con cero
    (0, -3, -3),   # Sumar con cero
    (1.5, 2.5, 4.0)  # Sumar dos números decimales (float)
])
def test_add_parametrizado(a, b, expected):
    """Test parametrizado para la función add."""
    assert add(a, b) == expected


# --- TESTS PARA RESTA (sub) ---

# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3



def test_sub_resta_mayor_que_primero():
    """Restar un número mayor al primero debe dar resultado negativo."""
    assert sub(3, 5) == pytest.approx(-2)
    assert sub(0, 1) == pytest.approx(-1)

def test_sub_restar_cero():
    """Restar cero debe dar el mismo número."""
    assert sub(4, 0) == 4
    assert sub(-3, 0) == -3

def test_sub_restar_dos_numeros_negativos():
    """Restar dos números negativos."""
    assert sub(-5, -3) == -2
    assert sub(-1, -4) == 3

def test_sub_restar_dos_numeros_decimales():
    """Restar dos números decimales."""
    assert sub(5.5, 2.2) == pytest.approx(3.3)
    assert sub(-1.1, -3.3) == pytest.approx(2.2)

@pytest.mark.parametrize("a , b, esperado", [
    (3, 5, -2),         # Restar un número mayor al primero da resultado negativo
    (4, 0, 4),          # Restar cero da el mismo número
    (-5, -3, -2),       # Restar dos números negativos
    (5.5, 2.2, 3.3),    # Restar dos números decimales
])
def test_sub_parametrizado(a, b, esperado):
    """Prueba múltiples casos de resta en una sola función usando @pytest.mark.parametrize."""
    assert sub(a, b) == pytest.approx(esperado)



# --- TESTS PARA MULTIPLICACIÓN (mul) ---

# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12

def test_mul_por_Cero():
    """Multiplicar por cero debe dar cero."""
    assert mul(5, 0) == 0
    assert mul(0, 5) == 0  

def test_mul_negativos():
    """Multiplicar dos numeros negativos debe dar un resultado positivo."""
    assert mul(4, -2) == -8
    assert mul(-3, 6) == -18

def test_mul_un_positivo_un_negativo():
    """Multiplicar un numero postivio y uno negativo debe dar un resultado negativo."""
    assert mul(2, -5) == -10
    assert mul(3, -4) == -12

def test_mul_por_uno():
    """Multiplicar por 1 debe devolver el mismo numero."""
    assert mul(7, 1) == 7
    assert mul(1, 9) == 9

def test_mul_decimales():
    """Multiplicar dos numeros decimales (float)."""
    assert mul(1.5, 2.0) == 3.0
    assert mul(-1.5, 2.0) == -3.0

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),          # Multiplicar dos enteros positivos
    (-2, -3, 6),        # Multiplicar dos enteros negativos
    (2, -3, -6),        # Multiplicar un entero positivo y uno negativo
    (0, 5, 0),          # Multiplicar por cero
    (1.5, 2.0, 3.0),    # Multiplicar dos decimales
])
def test_mul_parametrizado(a, b, expected):
    assert mul(a, b) == expected