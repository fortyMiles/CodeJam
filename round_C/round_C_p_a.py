from functools import lru_cache
from utilities import process_input
from utilities import small_input_validation


def reminder(m, n): return m % n


@lru_cache(maxsize=2*20)
def frac(n):
    if n == 1: return 1
    else:
        return n * frac(n-1)


def _a_N_frac(a, n, p):
    if n == 1: return a % p
    elif n % 2 == 0:
        return (_a_N_frac(a, n//2, p)**2) % p
    else:
        return (a * _a_N_frac(a, n-1, p)) % p


def large_a_n_frac(a, n, p):
    if a % p == 0: return 0
    elif n == 1: return a % p
    else:
        return (pow(a, n) * large_a_n_frac(a, n-1, p)) % p


def a_N_frac(a, n, p):
    return large_a_n_frac(a, n, p)


assert reminder(10, 1) == 0
assert reminder(10, 2) == 0
assert reminder(10, 5) == 0
assert reminder(10, 3) == 1
assert frac(3) == 6
assert frac(2) == 2

assert a_N_frac(2, 1, 2) == 0
assert a_N_frac(3, 3, 2) == 1

if __name__ == '__main__':
    file_n = 'round_C/data/A-small-practice.in'
    # file_n = 'round_C/data/A-large-practice.in'
    result = 'round_C/small_output.txt'
    # process_input(main_f=large_a_n_frac, input_file=file_n)
    small_input_validation(a_N_frac, input_file=file_n, result_file=result)
