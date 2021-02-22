import itertools

print(
    *map(
        lambda args: next(
            itertools.chain(
                map(
                    lambda r: ' '.join(map(str, r[0])),
                    filter(
                        lambda o: all(
                            map(
                                lambda s:
                                    (o[0].index(s[0]) < o[0].index(s[1]))
                                    != (o[0].index(s[2]) < o[0].index(s[3])),
                                o[1]
                            )
                        ),
                        zip(
                            itertools.permutations(range(1, args[0] + 1)),
                            itertools.repeat(
                                list(
                                    map(
                                        lambda tmp:
                                            list(
                                                map(
                                                    int,
                                                    input().split()
                                                )
                                            ),
                                        range(args[1])
                                    )
                                )
                            )
                        )
                    )
                ),
                [0]
            )
        ),
        [tuple(map(int, input().split()))]
    )
)
