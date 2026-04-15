[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jLxPRyso)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23569719)
# TP2 · Introducción a Tests Unitarios con pytest

**Stack**: Python 3.13+, `pytest`, pytest-cov, Git/GitHub Classroom (autograding)  
**Entrega**: código en el repositorio asignado (push a `main`). Los tests se ejecutan automáticamente.

---

## 1) Objetivo

Implementar una **calculadora** con funciones puras y desarrollar una **suite de tests unitarios** con `pytest`.

**Relevancia profesional**: En la industria, los tests unitarios permiten detectar errores temprano, documentar el comportamiento esperado y refactorizar con seguridad. `pytest` es el estándar en proyectos Python modernos.

**Qué van a construir**:
- Un módulo `src/calculator.py` con operaciones matemáticas puras.
- Una suite de tests en `tests/` que verifique cada función (incluyendo **casos borde** y **manejo de excepciones**).
- Autograding con GitHub Actions y cobertura mínima del 80%.

---

## 2) Instalación de Python y pip (guía rápida)

### Windows (10/11)
1. Descargá Python 3.13.x desde [python.org/downloads](https://www.python.org/downloads/).
2. Durante la instalación, marcá **"Add Python to PATH"** → **Install Now**.
3. Verificá en PowerShell o CMD:
   ```bash
   python --version
   pip --version
   ```
   Si `python` no se reconoce, reiniciá la terminal o reinstalá marcando "Add Python to PATH".

### macOS
1. Instalá con [Homebrew](https://brew.sh/):
   ```bash
   brew install python@3.13
   ```
2. Verificá:
   ```bash
   python3 --version
   pip3 --version
   ```
   > En macOS los comandos suelen ser `python3` y `pip3`.

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
pip3 --version
```

---

## 3) Setup del proyecto

### 1. Cloná tu repo de Classroom
```bash
git clone <URL-del-repo-asignado>
cd <carpeta-del-repo>
```

### 2. Creá un entorno virtual (recomendado)

**Windows (PowerShell)**:
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalá dependencias
```bash
pip install -r requirements.txt
```

---

## 4) Ejecutar los tests

```bash
# Todos los tests con detalle
pytest -v

# Con reporte de cobertura
pytest --cov=src --cov-report=term-missing

# Con umbral mínimo (80%)
pytest --cov=src --cov-fail-under=80
```

---

## 5) Estructura del repositorio

```
.
├── src/
│   ├── __init__.py
│   └── calculator.py               ← Implementar aquí
├── tests/
│   ├── __init__.py
│   ├── test_add.py                 ← Tests para add()
│   ├── test_sub.py                 ← Tests para sub()
│   ├── test_mul.py                 ← Tests para mul()
│   ├── test_div.py                 ← Tests para div()
│   ├── test_pow.py                 ← Tests para pow_()
│   ├── test_sqrt.py                ← Tests para sqrt()
│   └── test_mean.py                ← Tests para mean()
├── .github/
│   └── workflows/
│       └── autograding.yml
├── requirements.txt
├── README.md
└── RUBRICA.md
```

---

## 6) Archivos de tests

Hay **un archivo de tests por cada función** de la calculadora. Cada archivo ya tiene:
- Un **ejemplo funcionando** (no borrar) que muestra la sintaxis correcta.
- **Comentarios guía** con los casos que tenés que cubrir.
- Pistas sobre `pytest.raises` (para excepciones) y `@pytest.mark.parametrize` (para múltiples casos).

| Archivo | Función a testear | Excepción esperada |
|---------|------------------|--------------------|
| `tests/test_add.py` | `add(a, b)` | — |
| `tests/test_sub.py` | `sub(a, b)` | — |
| `tests/test_mul.py` | `mul(a, b)` | — |
| `tests/test_div.py` | `div(a, b)` | `ZeroDivisionError` si `b == 0` |
| `tests/test_pow.py` | `pow_(a, b)` | — |
| `tests/test_sqrt.py` | `sqrt(x)` | `ValueError` si `x < 0` |
| `tests/test_mean.py` | `mean(values)` | `ValueError` si lista vacía |

**Tu tarea**: completar cada archivo con tests adicionales que cubran los casos indicados en los comentarios.

---

## 7) Cómo se entrega

1. Implementá las funciones en `src/calculator.py`.
2. Completá los tests en cada archivo de `tests/`.
3. Corré los tests localmente: `pytest -v`.
4. Hacé **≥ 6 commits** significativos (ej: `"feat: add div + tests"`).
5. Hacé `push` a `main`.
6. Revisá **GitHub → Actions** para ver si quedó ✅.

---

## 8) Funciones (`src/calculator.py`)

| Función | Firma | Comportamiento esperado |
|---------|-------|------------------------|
| `add` | `add(a, b) -> float` | Retorna `a + b` |
| `sub` | `sub(a, b) -> float` | Retorna `a - b` |
| `mul` | `mul(a, b) -> float` | Retorna `a * b` |
| `div` | `div(a, b) -> float` | Retorna `a / b`; lanza `ZeroDivisionError` si `b == 0` |
| `pow_` | `pow_(a, b) -> float` | Retorna `a ** b` |
| `sqrt` | `sqrt(x) -> float` | Retorna `√x`; lanza `ValueError` si `x < 0` |
| `mean` | `mean(values) -> float` | Promedio de la lista; lanza `ValueError` si está vacía |

---

## 9) Evaluación automática

Al hacer **push a main**, GitHub Actions:
1. Instala dependencias.
2. Ejecuta `pytest -v --cov=src`.
3. Verifica cobertura ≥ 80%.
4. Reporta ✅ o ❌ en la pestaña **Actions**.

---

## 10) Troubleshooting rápido

| Problema | Solución |
|----------|---------|
| `pip: command not found` | Usá `python -m pip --version` |
| `pytest: command not found` | Activá el entorno virtual y corré `pip install -r requirements.txt` |
| Un test falla | Leé el mensaje: muestra "esperado vs obtenido" |
| Actions falla pero local pasa | Revisá la versión de Python y que las dependencias estén en `requirements.txt` |
| `ModuleNotFoundError: src` | Corré `pytest` desde la raíz del proyecto, no desde dentro de `src/` |
