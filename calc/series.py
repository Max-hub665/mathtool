import math

MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100_000
DIGITS = math.ceil(-math.log10(MAX_EPS))

def sign(n):
    """Вернуть знак слагаемого по его номеру"""
    if n % 2 == 0:
        return -1
    return 1

def third(n):
    """Найти слагаемое ряда third с номером n"""
    return sign(n) / (3 * n)

def sqplus(n):
    """Найти слагаемое ряда sqplus с номером n"""
    return sign(n) / (n * n + 1)

# Храним формулу вместе с функцией слагаемого.
FORMULAS = {
    "third": (third, "S = 1/3 - 1/6 + 1/9 - ..."),
    "sqplus": (sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
}

def validate(terms, eps):
    """Проверить способ остановки и допустимый предел"""
    if (terms is None) == (eps is None):
        raise ValueError("укажите ровно один из terms и eps")
    if terms is not None:
        if not 1 <= terms <= MAX_TERMS:
            raise ValueError("количество слагаемых вне диапазона")
    else:
        if not math.isfinite(eps) or not 0 < eps <= MAX_EPS:
            raise ValueError("точность вне диапазона")

def sum_by_terms(term, count):
    """Сложить count слагаемых функции term"""
    validate(count, None)
    result = 0
    for n in range(1, count + 1):
        result += term(n)
    return result

def sum_by_eps(term, eps):
    """Вернуть сумму и число слагаемых при точности eps"""
    validate(None, eps)
    result = 0
    n = 0
    while True:
        n += 1
        value = term(n)
        result += value
        # Последнее маленькое слагаемое уже включено в сумму.
        if abs(value) < eps:
            return result, n
        if n >= MAX_ITERATIONS:
            raise ValueError("точность не достигнута")
