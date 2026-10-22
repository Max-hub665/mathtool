import math

maxx = 100000
DIGITS = 4

def ratio(x):
    """Вычислить x / (x + 1)."""
    return x / (x + 1)

def root(x):
    """Вычислить квадратный корень из x*x + 1."""
    return math.sqrt(x * x + 1)

# Для каждой функции задаём её допустимый промежуток.
FUNCTIONS = {
    "ratio": (ratio, "F(x) = x / (x + 1)", 0, 20, True),
    "root": (root, "F(x) = sqrt(x^2 + 1)", -5, 5, False),
}

def validate(start, stop, steps, low, high, closed):
    """Проверить пределы интегрирования и число шагов."""
    if not math.isfinite(start) or not math.isfinite(stop):
        raise ValueError("предел не является конечным числом")
    if start >= stop:
        raise ValueError("начальный предел не меньше конечного")
    for value in (start, stop):
        if closed:
            if value < low or value > high:
                raise ValueError("предел вне промежутка")
        else:
            if value <= low or value >= high:
                raise ValueError("предел вне промежутка")
    if not 1 <= steps <= maxx:
        raise ValueError("количество шагов вне диапазона")

def integral(function, start, stop, steps):
    """Найти интеграл методом левых прямоугольников."""
    dx = (stop - start) / steps
    result = 0
    # Высоту прямоугольника берём на левом краю.
    for i in range(steps):
        x = start + i * dx
        result += function(x) * dx
    return result
