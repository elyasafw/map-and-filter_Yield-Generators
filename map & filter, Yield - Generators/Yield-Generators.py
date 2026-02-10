#1
def count_up(n):
    index = 1
    while index <= n:
        yield index
        index += 1

for num in count_up(5):
 print(num)


#2
def evens(n):
    for num in range(1, n + 1):
        if num % 2 == 0:
            yield num

print(list(evens(10)))


#3
gen = count_up(3)
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
print(next(gen)) # StopIteration 


#4
def digits(n):
    for value in str(n)[::-1]:
        yield int(value)

print(list(digits(4827)))


#5
def count_from(start):
    while True:
        yield start
        start += 1

gen = count_from(10)
print(next(gen)) # 10
print(next(gen)) # 11
print(next(gen)) # 12
# ... never stops


#6
def fibonacci():
    num1, num2 = 0 ,1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")


# #7
def take(n, gen):
    for _ in range(n):
            yield next(gen)

print(list(take(5, fibonacci())))
print(list(take(3, count_from(100))))


#8
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#a
square_even_gen = (n ** n for n in nums if n % 2 == 0)
#b
print(sum(square_even_gen))


#9
def read_lines(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as f:
        for line in f:
            yield line.strip()


for line in read_lines("./map-and-filter.py"):
    print(line)


#10
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

print(list(take(10, primes())))


#11
def sliding_window(data, size):
    for i in range(len(data) - size + 1):
        yield data[i : i + size]

data = [1, 2, 3, 4, 5, 6]

print(list(sliding_window(data, 3)))
print(list(sliding_window(data, 2)))