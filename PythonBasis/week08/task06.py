print(
    *map(
        lambda x: (int(x[0]) + int(x[1])) % 2,
        zip(
            input().split(),
            input().split()
        )
    )
)
