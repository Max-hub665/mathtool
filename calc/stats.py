import math

MAX_COUNT = 20
MAX_ABS = 10000

def validate(values):
    """Проверить количество и значения чисел"""
    if len(values) == 0:
        raise ValueError("последовательность пуста")
    if len(values) > MAX_COUNT:
        raise ValueError("чисел больше 20")
    for value in values:
        if not math.isfinite(value):
            raise ValueError("число не является конечным")
        if abs(value) > MAX_ABS:
            raise ValueError("число вне допустимого диапазона")

def count(values):
    """Вернуть количество чисел"""
    return len(values)

def total(values):
    """Вернуть сумму чисел"""
    result = 0
    for value in values:
        result += value
    return result

def mean(values):
    """Найти среднее арифметическое"""
    return total(values) / len(values)

def square_total(values):
    """Сложить квадраты чисел"""
    result = 0
    for value in values:
        result += value ** 2
    return result

def rms(values):
    """Найти среднее квадратическое"""
    return math.sqrt(square_total(values) / len(values))

def deviation_total(values):
    """Сложить квадраты отклонений от среднего"""
    # Среднее считаем до суммы квадратов отклонений.
    average = mean(values)
    result = 0
    for value in values:
        result += (value - average) ** 2
    return result

def variance(values):
    """Найти дисперсию с делением на N"""
    return deviation_total(values) / len(values)

def sigma(values):
    """Найти корень из дисперсии."""
    return math.sqrt(variance(values))

def sample_sigma(values):
    """Найти отклонение по N-1, для одного числа вернуть None"""
    if len(values) < 2:
        return None
    return math.sqrt(deviation_total(values) / (len(values) - 1))

def minimum(values):
    """Найти наименьшее число"""
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result

def maximum(values):
    """Найти наибольшее число"""
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result

def positive_count(values):
    """Посчитать числа больше нуля"""
    result = 0
    for value in values:
        if value > 0:
            result += 1
    return result

def negative_count(values):
    """Посчитать числа меньше нуля"""
    result = 0
    for value in values:
        if value < 0:
            result += 1
    return result

# Подпись показателя, его функция и формат вывода.
REPORT = [
    ("Количество", count, "d"),
    ("Сумма", total, ".3f"),
    ("Ср. арифм.", mean, ".3f"),
    ("Сумма кв.", square_total, ".3f"),
    ("Ср. кв.", rms, ".3f"),
    ("Дисперсия", variance, ".3f"),
    ("СКО", sigma, ".3f"),
    ("Станд. откл.", sample_sigma, ".3f"),
    ("Наименьшее", minimum, ".3f"),
    ("Наибольшее", maximum, ".3f"),
    ("Положительных", positive_count, "d"),
    ("Отрицательных", negative_count, "d"),
]
