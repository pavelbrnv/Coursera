from itertools import permutations

print(
    *sorted(
        map(
            lambda p: ''.join(map(str, p)),
            permutations(range(1, int(input()) + 1))
        )
    ),
    sep='\n'
)
