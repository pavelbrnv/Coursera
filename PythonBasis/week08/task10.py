from functools import reduce

print(
    *reduce(
        lambda a, b: map(
            lambda x: (x[0] + x[1]) % 2,
            zip(a, b)
        ),
        map(
            lambda temp: map(int, input().split()),
            range(int(input()))
        )
    )
)
