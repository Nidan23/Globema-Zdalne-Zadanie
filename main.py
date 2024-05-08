from collections import Counter


# Prime numbers drawing from the range (123 456 789) and using the Eratosthenes sieve
def SieveOfEratosthenes(n):
    prime = [True for _ in range(n + 1)]
    data = []
    p = 2

    while p * p <= n:

        if prime[p]:

            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1

    prime[0] = False
    prime[1] = False

    for p in range(n + 1):
        if prime[p]:
            data.append(str(p))

    return data


# Searching for the similar prime number groups
def FindGroups(data):
    for i in range(len(data)):
        temporary_data = []
        for chars in data[i]:
            temporary_data.append(chars)

        temporary_data = sorted(temporary_data)

        data[i] = ''

        for x in temporary_data:
            data[i] = data[i] + x

    res = Counter(data)

    res = sorted(res.items(), key=lambda kv: (kv[1], kv[0]))

    print(f'The biggest group is: {res[-1][0]} - {res[-1][1]} elements')


if __name__ == '__main__':
    n = 123456789

    FindGroups(SieveOfEratosthenes(n))
