import itertools

# Digits 0-9
digits = list(range(1000))

# Use itertools.permutations
permutations = itertools.permutations(digits)
# Get the millionth permutation (index 999,999)
millionth_perm_itertools = next(itertools.islice(permutations, 1_000_000 - 1, None))

print(''.join(map(str, millionth_perm_itertools
