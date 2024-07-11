from fibo import caching_fibonacci

def main():
    fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610


if __name__== "__main__":
    main()
