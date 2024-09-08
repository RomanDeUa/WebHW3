import time
import multiprocessing

# Функція для знаходження всіх дільників числа
def factorize_number(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

# Синхронна версія factorize
def factorize_sync(*numbers):
    result = []
    for number in numbers:
        result.append(factorize_number(number))
    return result

# Паралельна версія factorize з використанням multiprocessing
def factorize_parallel(*numbers):
    with multiprocessing.Pool() as pool:
        result = pool.map(factorize_number, numbers)
    return result

# Функція для вимірювання часу виконання
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"{func.__name__} виконалась за {end_time - start_time:.4f} секунд")
    return result

# Головна функція для запуску тестів
def main():
    numbers = (128, 255, 99999, 10651060)

    # Синхронна версія
    a, b, c, d = measure_time(factorize_sync, *numbers)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    # Паралельна версія
    a, b, c, d = measure_time(factorize_parallel, *numbers)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

if __name__ == "__main__":
    main()

# Перевірка python HW3.2.py