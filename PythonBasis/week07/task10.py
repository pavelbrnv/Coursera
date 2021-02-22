class Segment:
    start = 0
    end = 0


def normalize_segment(s):
    s.start, s.end = min(s.start, s.end), max(s.start, s.end)


def has_intersection(s1, s2):
    return s1.start <= s2.end and s2.start <= s1.end


def get_intersection(s1, s2):
    s = Segment()
    s.start = max(s1.start, s2.start)
    s.end = min(s1.end, s2.end)
    return s


def main():
    s1, s2 = Segment(), Segment()
    s1.start, s1.end, s2.start, s2.end = map(int, input().split())

    normalize_segment(s1)
    normalize_segment(s2)

    if has_intersection(s1, s2):
        intersection = get_intersection(s1, s2)
        print(intersection.end - intersection.start + 1)
    else:
        print(0)


main()
