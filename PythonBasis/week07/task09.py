inFile = open('input.txt', 'r', encoding='utf8')

n = int(inFile.readline().strip())

common_languages = set()
all_languages = set()

for pupil_index in range(n):
    m = int(inFile.readline().strip())
    pupil_languages = set()
    for language_index in range(m):
        language = inFile.readline().strip()
        pupil_languages.add(language)
        all_languages.add(language)
    if pupil_index == 0:
        common_languages = pupil_languages
    else:
        common_languages &= pupil_languages

inFile.close()

print(len(common_languages))
for language in common_languages:
    print(language)

print(len(all_languages))
for language in all_languages:
    print(language)
