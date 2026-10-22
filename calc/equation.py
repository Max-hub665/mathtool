import math

MAX_VALUE = 10000

# Сначала проверяем исходные данные.
def validate(coefficients):
    """Проверить диапазон коэффициентов и наличие неизвестного."""
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")
    if coefficients["A"] == 0 and coefficients["B"] == 0:
        raise ValueError("это не уравнение, неизвестное отсутствует")

def solve(a, b, c):
    """Вернуть вид уравнения, дискриминант и список корней."""
    validate({"A": a, "B": b, "C": c})
    if a == 0:
        return "линейное", None, [-c / b]
    # Число действительных корней зависит от знака дискриминанта.
    d = b * b - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return "квадратное", d, [x1, x2]
    if d == 0:
        return "квадратное", d, [-b / (2 * a)]
    return "квадратное", d, []
