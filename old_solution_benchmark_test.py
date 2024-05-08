from old_solution import SieveOfEratosthenes, FindGroups, old_solution_run


def test_old_solution_SieveOfEratosthenes(benchmark):
    benchmark.pedantic(SieveOfEratosthenes, args=(123456789,), iterations=1, rounds=2)


def test_old_solution_FindGroups(benchmark):
    prime_numbers = SieveOfEratosthenes(123456789)

    benchmark.pedantic(FindGroups, args=(prime_numbers,), iterations=1, rounds=2)


def test_old_solution_run(benchmark):
    benchmark.pedantic(old_solution_run, args=(123456789,), iterations=1, rounds=2)

