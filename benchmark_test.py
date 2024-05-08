from main import get_prime_numbers_up_to_n, find_most_common_similar_prime_number_group, run


def test_get_prime_numbers_up_to_n(benchmark):
    benchmark.pedantic(get_prime_numbers_up_to_n, args=(123456789,), iterations=1, rounds=2)


def test_find_most_common_similar_prime_number_group(benchmark):
    prime_numbers = get_prime_numbers_up_to_n(123456789)

    benchmark.pedantic(find_most_common_similar_prime_number_group, args=(prime_numbers,), iterations=1, rounds=2)


def test_run(benchmark):
    benchmark.pedantic(run, args=(123456789,), iterations=1, rounds=2)
