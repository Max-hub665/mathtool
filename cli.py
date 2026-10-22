import argparse
from calc import integration, series

def build_parser():
    """Создать разборщик команд и параметров"""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="Расчёты над уравнениями и числовыми последовательностями",
        allow_abbrev=False,
    )
    # Описываем команды и их параметры.
    commands = parser.add_subparsers(dest="command")

    solve = commands.add_parser(
        "solve", help="Решить уравнение", description="Решение Ax^2 + Bx + C = 0",
        allow_abbrev=False,
    )
    solve.add_argument("-a", type=int, help="Коэффициент A, модуль не больше 10000")
    solve.add_argument("-b", type=int, help="Коэффициент B, модуль не больше 10000")
    solve.add_argument("-c", type=int, help="Коэффициент C, модуль не больше 10000")

    stats = commands.add_parser(
        "stats", help="Показатели последовательности", description="Статистика до 20 чисел",
        allow_abbrev=False,
    )
    stats.add_argument("--input", help="Файл UTF-8 с числами; без него читается stdin")

    sums = commands.add_parser(
        "series", help="Сумма ряда", description="Суммирование знакочередующегося ряда",
        allow_abbrev=False,
    )
    sums.add_argument("--func", choices=sorted(series.FORMULAS), required=True, help="Имя ряда")
    # Нужен один способ остановки: количество или точность.
    mode = sums.add_mutually_exclusive_group(required=True)
    mode.add_argument("--terms", type=int, help="Количество слагаемых от 1 до 10000")
    mode.add_argument("--eps", type=float, help="Точность: 0 < eps <= 0.0001")

    integrals = commands.add_parser(
        "integrate", help="Численное интегрирование", description="Метод левых прямоугольников",
        allow_abbrev=False,
    )
    integrals.add_argument("--func", choices=sorted(integration.FUNCTIONS), required=True, help="Имя функции")
    integrals.add_argument("--from", dest="start", type=float, required=True, help="Нижний предел")
    integrals.add_argument("--to", dest="stop", type=float, required=True, help="Верхний предел")
    integrals.add_argument("--steps", type=int, required=True, help="Число шагов от 1 до 100000")
    return parser


