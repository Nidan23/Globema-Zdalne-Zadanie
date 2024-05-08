# Globema Remote Assignment

Remote assignment for Globema.

# Requirements:
 - Find similar prime numbers in a given range

# Description:
 Similar prime number is a number that has the same digits as another prime number. For example, 113 and 131 are similar prime numbers. The task is to find all similar prime numbers in a given range.


## Benchmarks were run on the following machine:
- Apple MacBook Pro (16-inch, M2 max, 2023), 64GB RAM, 2TB SSD

 # OLD SOLUTION

| Name (time in s)                      | Min            | Max            | Mean           | StdDev         | Median         | IQR            | Outliers | OPS           | Rounds | Iterations |
|---------------------------------------|----------------|----------------|----------------|----------------|----------------|----------------|----------|---------------|--------|------------|
| test_old_solution_FindGroups          | 4.0742 (1.0)   | 4.6944 (1.0)   | 4.3843 (1.0)   | 0.4385 (12.44) | 4.3843 (1.0)   | 0.6202 (12.44) | 0;0      | 0.2281 (1.0)  | 2      | 1          |
| test_old_solution_SieveOfEratosthenes | 14.3250 (3.52) | 14.3932 (3.07) | 14.3591 (3.28) | 0.0483 (1.37)  | 14.3591 (3.28) | 0.0683 (1.37)  | 0;0      | 0.0696 (0.31) | 2      | 1          |
| test_old_solution_run                 | 18.8457 (4.63) | 18.8955 (4.03) | 18.8706 (4.30) | 0.0353 (1.0)   | 18.8706 (4.30) | 0.0499 (1.0)   | 0;0      | 0.0530 (0.23) | 2      | 1          |

# NEW SOLUTION

| Name (time in s)                                 | Min            | Max            | Mean           | StdDev         | Median         | IQR            | Outliers | OPS           | Rounds | Iterations |
|--------------------------------------------------|----------------|----------------|----------------|----------------|----------------|----------------|----------|---------------|--------|------------|
| test_find_most_common_similar_prime_number_group | 1.8412 (1.0)   | 2.6008 (1.0)   | 2.2210 (1.0)   | 0.5371 (15.85) | 2.2210 (1.0)   | 0.7596 (15.85) | 0;0      | 0.4503 (1.0)  | 2      | 1          |
| test_get_prime_numbers_up_to_n                   | 12.2465 (6.65) | 12.4886 (4.80) | 12.3675 (5.57) | 0.1712 (5.05)  | 12.3675 (5.57) | 0.2421 (5.05)  | 0;0      | 0.0809 (0.18) | 2      | 1          |
| test_run                                         | 14.9045 (8.10) | 14.9524 (5.75) | 14.9284 (6.72) | 0.0339 (1.0)   | 14.9284 (6.72) | 0.0479 (1.0)   | 0;0      | 0.0670 (0.15) | 2      | 1          |
