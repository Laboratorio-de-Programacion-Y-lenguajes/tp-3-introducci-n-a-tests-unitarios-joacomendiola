"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0

def test_mean_un_solo_elemento():
    """Una lista con un solo elemento debe devolver ese valor."""
    assert mean([10]) == 10.0

def test_mean_negativos():
    """Promedio con numeros negativos."""
    assert mean([-2, -4]) == -3.0

def test_mean_decimales():
    "Promedio con numeros decimales"
    assert mean([1.5, 2.5, 5.0]) == 3.0

def test_mean_lista_vacia():
    """Verifica que lance ValueError si la lista esta vacia."""
    with pytest.raises(ValueError):
        mean([])

@pytest.mark.parametrize("lista, esperado", [
    ([1, 2, 3], 2.0),          
    ([10, 20, 30, 40], 25.0), 
    ([0, 0, 0], 0.0),      
])
def test_mean_parametrizado(lista, esperado):
    assert mean(lista) == esperado
