from math import sqrt
from itertools import chain

print(
    *filter(
        lambda x: x < 4 or not any(
            map(
                lambda v: x % v == 0,
                chain([2], range(3, int(sqrt(x)) + 1, 2))
            )
        ),
        range(2, int(input()) + 1)
    )
)
