import time


def task1():
    z = 0
    N = 20
    result = [584, 902, 304, 906, 806, 328, 92, 100, 481, 422, 361, 691, 383, 922, 408, 235, 226, 15, 251, 487]
    print(result)
    for i in range(len(result) - 1):
        if result[i] + result[i + 1] >= 0:
            z += 1
    print(f"кол пар элем чья сумма полож {z}")


tick = time.perf_counter()
task1()
tock = time.perf_counter()
print(f"вычисление заняло {tock-tick:0.8f}")


def task2():
    N = 20
    result = [584, 902, 304, 906, 806, 328, 92, 100, 481, 422, 361, 691, 383, 922, 408, 235, 226, 15, 251, 487]
    print(result)
    z = result[0] + result[1]
    for i in range(len(result)-1):
        sum = result[i] + result[i+1]
        if sum > z:
            z = sum
    print(f"макс сумма {z}")


tick = time.perf_counter()
task2()
tock = time.perf_counter()
print(f"вычисление заняло {tock-tick:0.8f}")


def task3():
    N = 20
    result = [584, 902, 304, 906, 806, 328, 92, 100, 481, 422, 361, 691, 383, 922, 408, 235, 226, 15, 251, 487]
    print(result)
    for i in range(len(result) - 1):
        z = result[i]
        d = result[i + 1]
        if z > d:
            print(z)
        else:
            print(d)


tick = time.perf_counter()
task3()
tock = time.perf_counter()
print(f"вычисление заняло {tock-tick:0.8f}")


def task4():
    N = 20
    result = [584, 902, 304, 906, 806, 328, 92, 100, 481, 422, 361, 691, 383, 922, 408, 235, 226, 15, 251, 487]
    print(result)
    z = 0
    for i in range(len(result) - 2):
        if result[i] % 2 == 0 and result[i + 1] % 2 == 0 and result[i + 2] % 2 == 0:
            z += 1
    print(f"тройки элем {z}")


tick = time.perf_counter()
task4()
tock = time.perf_counter()
print(f"вычисление заняло {tock-tick:0.8f}")


def task5():
    N = 20
    result = [584, 902, 304, 906, 806, 328, 92, 100, 481, 422, 361, 691, 383, 922, 408, 235, 226, 15, 251, 487]
    print(result)
    z = 0
    for i in range(len(result) - 1):
        if result[i] * result[i + 1] % 7 == 2:
            z += 1
    print(z)


tick = time.perf_counter()
task5()
tock = time.perf_counter()
print(f"вычисление заняло {tock-tick:0.8f}")


def task6():
    N = 20
    result = [584, 902, 304, 906, 806, 328, 92, 100, 481, 422, 361, 691, 383, 922, 408, 235, 226, 15, 251, 487]
    print(result)
    z = 0
    for i in range(len(result)-1):
        if result[i] - result[i + 1] > abs(14) and result[i] / result[i+1] > abs(1):
            z += 1
    print(z)


tick = time.perf_counter()
task6()
tock = time.perf_counter()
print(f"вычисление заняло {tock-tick:0.8f}")