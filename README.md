# PR_PYTHON_INTRO_NUMERO15 — Fechas y horas

*Autor: **Luis Bravo (braco 96)***

## Qué practico
Parseo y formateo sin perder la zona horaria.

## Lo que me costó entender
- Diferenciar entre intención y efecto colateral: prefiero funciones puras cuando puedo.
- Manejar entradas raras (cadenas vacías, `None`, listas con duplicados, etc.).
- Diseñar pruebas **antes** del código para obligarme a pensar en los casos borde.

## Cómo lo abordé
1. Escribí pruebas con casos felices y casos extremos.
2. Implementé la solución más simple que pasa las pruebas.
3. Refactoricé nombres y extraje helpers cuando lo vi claro.
4. Añadí más pruebas para capturar regresiones.

## Ejecutar
```bash
pytest -q
```

## Errores comunes que anoté
- Asumir que siempre hay datos.
- No validar tipos/valores y luego sorprenderme por excepciones.
- Probar poco: ahora uso parametrización para cubrir más con menos código.

## Ejemplos rápidos
```py
# main.py
# (mira tests/ para más ejemplos)
```