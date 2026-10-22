import sys
from calc import equation, integration, series, stats
from cli import build_parser

def show_help():
    """Вывести справку по запуску программы."""
    print("mathtool --- решение уравнений вида A*x^2 + B*x + C = 0")
    print("Также доступны статистика, суммы рядов и интегралы.")
    print()
    print("Использование:")
    print("  python mathtool.py               вывод справки")
    print("  python mathtool.py --help        вывод справки")
    print("  python mathtool.py solve         ввод коэффициентов с клавиатуры")
    print("  python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print("  python mathtool.py stats --input numbers.txt   обработка чисел из файла")
    print("  python mathtool.py stats         чтение чисел из стандартного ввода")
    print("  python mathtool.py series --func sqplus --terms 6   сумма по количеству слагаемых")
    print("  python mathtool.py series --func third --eps 0.0001   сумма по точности")
    print("  python mathtool.py integrate --func ratio --from 0 --to 20 --steps 1000   интеграл")
    print("  python mathtool.py <команда> --help   справка по выбранной команде")
    print()
    print("Коэффициенты A, B, C - целые числа, по модулю не превышающие 10000.")
    print("Ряды: third, sqplus. Функции интеграла: ratio, root.")
    print("Для завершения ввода stats нажмите Ctrl+Z, затем Enter.")


def handle_solve(args):
    """Получить коэффициенты и вывести решение уравнения"""
    # Без коэффициентов запрашиваем их с клавиатуры.
    if args.a is None and args.b is None and args.c is None:
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            raise ValueError("коэффициент не является целым числом")
    else:
        if args.a is None or args.b is None or args.c is None:
            raise ValueError("укажите все три коэффициента либо ни одного")
        a, b, c = args.a, args.b, args.c
    kind, d, roots = equation.solve(a, b, c)
    print(f"Уравнение {kind}")
    if d is not None:
        print(f"Дискриминант: {d}")
    if len(roots) == 0:
        print("Действительных корней нет")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")
    return 0

def read_values(stream):
    """Прочитать числа из потока и проверить их"""
    values = []
    for line in stream:
        for word in line.split():
            try:
                value = float(word)
            except ValueError:
                raise ValueError(f"{word} не является числом")
            values.append(value)
            if len(values) > stats.MAX_COUNT:
                raise ValueError("чисел больше 20")
    stats.validate(values)
    return values

def handle_stats(args):
    """Прочитать числа и вывести их показатели"""
    if args.input is not None:
        with open(args.input, encoding="utf-8-sig") as handle:
            values = read_values(handle)
    else:
        values = read_values(sys.stdin)
    for label, function, form in stats.REPORT:
        value = function(values)
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")
    return 0

def handle_series(args):
    """Посчитать и вывести сумму выбранного ряда"""
    series.validate(args.terms, args.eps)
    term, formula = series.FORMULAS[args.func]
    if args.terms is not None:
        result = series.sum_by_terms(term, args.terms)
        count = args.terms
    else:
        result, count = series.sum_by_eps(term, args.eps)
    print(formula)
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {result:.{series.DIGITS}f}")
    return 0

def handle_integrate(args):
    """Посчитать и вывести интеграл выбранной функции"""
    function, formula, low, high, closed = integration.FUNCTIONS[args.func]
    integration.validate(args.start, args.stop, args.steps, low, high, closed)
    result = integration.integral(function, args.start, args.stop, args.steps)
    print(formula)
    print(f"Значение интеграла: {result:.{integration.DIGITS}f}")
    return 0

# Обработчик выбирается по имени команды.
HANDLERS = {
    "solve": handle_solve,
    "stats": handle_stats,
    "series": handle_series,
    "integrate": handle_integrate,
}

def main(argv):
    """Выполнить команду и вернуть код завершения"""
    if argv == ["--help"] or argv == ["-h"]:
        show_help()
        return 0
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        show_help()
        return 0
    try:
        return HANDLERS[args.command](args)
    # Ошибки данных и чтения выводим отдельно от результата.
    except (ValueError, OSError, EOFError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
