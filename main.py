from collections import Counter

empty_string = ''


# Prime numbers drawing from the range (123 456 789) and using the Eratosthenes sieve
def get_prime_numbers_up_to_n(n):
    prime = [True] * (n+1)
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    primes = [2] + [p for p in range(3, n, 2) if prime[p]]

    return primes


# Searching for the similar prime number groups
def find_most_common_similar_prime_number_group(data):
    size = len(data)

    for i in range(size):
        data_as_string = str(data[i])
        sorted_data = sorted(data_as_string)
        data[i] = empty_string.join(sorted_data)

    counter = Counter(data)

    biggest_group = counter.most_common()[0]

    return biggest_group


def run(n):
    prime_numbers = get_prime_numbers_up_to_n(n)
    most_common_group = find_most_common_similar_prime_number_group(prime_numbers)

    number_group = most_common_group[0]
    number_group_count = most_common_group[1]

    print(f'The biggest group is: {number_group} - {number_group_count} elements')

    return number_group, number_group_count


if __name__ == '__main__':
    run(123456789)
