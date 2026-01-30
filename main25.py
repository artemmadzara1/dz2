import random
x, y, z = 3, 3, 3

matrix_3d = [[[random.randint(1, 99) for _ in range(z)] for _ in range(y)] for _ in range(x)]


for i, layer in enumerate(matrix_3d):
    print(f"Слой {i}: {layer}")
import time
from memory_profiler import profile

tick =time.perf_counter()
import time
from memory_profiler import memory_usage


def benchmark(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        start_time = time.time()
        mem_before = memory_usage()[0]
        result = func(*args, **kwargs)
        mem_after = memory_usage()[0]
        end_time = time.time() - start_time
        print(f"Вызов №{count} время выполнения {end_time:.6f} сек.")
        print(f"Память до: {mem_before:.2f} MiB, после: {mem_after:.2f} MiB, разница: {mem_after - mem_before:.2f} MiB")
        return result

    return wrapper
@benchmark
def find_positions(n):
    positions = []
    for i in range(x):
        for b in range(y):
            for j in range(z):
                if matrix_3d[i][b][j] == n:
                    positions.append((i, b, j))
    return positions
target = 50
result = find_positions(target)

if result:
    print(f"\nЧисло {target} найдено на позициях: {result}")
else:
    print(f"\nЧисло {target} не найдено в матрице.")
