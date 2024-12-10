import multiprocessing as mp
import math
import time

def leibniz(k):
    return (-1)**k / (2*k + 1)

def calc(start, end):
    partial_sum = 0
    for k in range(start, end):
        partial_sum += leibniz(k)
    return partial_sum

def main(k, n):
    chunk_size = k // n
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(n)]
    with mp.Pool(processes=n) as pool:
        partial_sums = pool.starmap(calc, ranges)
    summe = sum(partial_sums)
    pi = 4 * summe
    return pi

if __name__ == '__main__':
    try:
        k = int(input("Iterationen:"))
        n = int(input("Prozesse:"))
    except:
        print(f"Ungültige Eingabe:")
    time1 = time.time()
    pi_approximation = main(k, n)
    print(f"annährerung von pi mit {k} Iterationen (k) und {n} Prozessen: {pi_approximation}")
    if pi_approximation < math.pi:
        print(f"Die Abweichung beträgt {(math.pi - pi_approximation)}")
    elif pi_approximation > math.pi:
        print(f"Die Abweichung beträgt {(pi_approximation - math.pi)}")
    else:
        print("Du hast Pi!")
    print(f"Benötigte Zeit: {time.time()-time1}")