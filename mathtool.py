import sys
import math

maxx = 10000

def show_help():
    print("mathtool --- решение уравнений вида A*x^2 + B*x + C = 0")
    print()
    print("Использование:")
    print("  python mathtool.py               вывод справки")
    print("  python mathtool.py --help        вывод справки")
    print("  python mathtool.py solve         ввод коэффициентов с клавиатуры")
    print("  python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print()
    print("Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.")

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0 or (len(args) == 1 and args[0] == "--help"):
        show_help()
        sys.exit(0)
    if args[0] != "solve":
        print("ОШИБКА: неизвестная команда. Используйте 'solve' или '--help'.", file=sys.stderr)
        sys.exit(1)

    A = B = C = None

    if len(args) == 1:
        try:
            A = int(input("Введите A: "))
            B = int(input("Введите B: "))
            C = int(input("Введите C: "))
        except ValueError:
            print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
            sys.exit(1)
    elif len(args) == 7:
        if args[1] != "-a" or args[3] != "-b" or args[5] != "-c":
            print("ОШИБКА: неверные флаги. Ожидаются -a, -b, -c.", file=sys.stderr)
            sys.exit(1)
        try:
            A = int(args[2])
            B = int(args[4])
            C = int(args[6])
        except ValueError:
            print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
            sys.exit(1)
    else:
        print("ОШИБКА: неверный набор параметров.", file=sys.stderr)
        sys.exit(1)
    if abs(A) > maxx or abs(B) > maxx or abs(C) > maxx:
        print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
        sys.exit(1)
    if A == 0:
        if B == 0:
            print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
            sys.exit(1)
        else:
            print("Уравнение линейное")
            x = -C / B
            print(f"x = {x:.3f}")
    else:
        print("Уравнение квадратное")
        D = B*B - 4*A*C
        print(f"D = {D}")
        if D > 0:
            sqrt_D = math.sqrt(D)
            x1 = (-B + sqrt_D) / (2*A)
            x2 = (-B - sqrt_D) / (2*A)
            print(f"x1 = {x1:.3f}")
            print(f"x2 = {x2:.3f}")
        elif D == 0:
            x = -B / (2*A)
            print(f"x = {x:.3f}")
        else:
            print("Действительных корней нет")

    sys.exit(0)
