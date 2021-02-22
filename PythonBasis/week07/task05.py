inFile = open('input.txt', 'r', encoding='utf8')
file_iterator = iter(inFile)

n, m = map(int, next(file_iterator).split())

ann_colors = set()
boris_colors = set()

for i in range(n):
    color = int(next(file_iterator))
    ann_colors.add(color)

for i in range(m):
    color = int(next(file_iterator))
    boris_colors.add(color)

inFile.close()

common_colors = ann_colors & boris_colors
print(len(common_colors))
print(*sorted(common_colors))

only_ann_colors = ann_colors - boris_colors
print(len(only_ann_colors))
print(*sorted(only_ann_colors))

only_boris_colors = boris_colors - ann_colors
print(len(only_boris_colors))
print(*sorted(only_boris_colors))
