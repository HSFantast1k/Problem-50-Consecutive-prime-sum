import time


def sieve(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n ** 0.5 + 1), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime


list_simple_values = sieve(1_000_000)


def No_Name(number):
    x = y = finish = 0
    start = time.time()
    while finish - start < 1:
        if list_simple_values[x: y] == number:
            return False
        if sum(list_simple_values[x: y]) == number:
            return [y - x, x, y, finish - start]
        if sum(list_simple_values[x: y]) < number:
            y += 1
        else:
            x += 1
        finish = time.time()

resaut_list = {}
max_resaut = 0
t1 = time.time()
for number in list_simple_values[::-1]:
    resaut = No_Name(number)
    if resaut:
        if resaut[0] > max_resaut:
            t2 = time.time()
            max_resaut = resaut[0]
            print("Число - {}, время - {}".format(number, t2 - t1))
    t3 = time.time()
    if t3 - t1 > 60:
        break