def normalize(number):
    number = number.strip()
    number = number.replace('+7', '8')
    number = number.replace('-', '')
    number = number.replace('(', '')
    number = number.replace(')', '')
    if len(number) == 7:
        number = '8495' + number
    return number


inFile = open('input.txt', 'r', encoding='utf8')

new_number = normalize(inFile.readline())
for i in range(3):
    existing_number = normalize(inFile.readline())
    if new_number == existing_number:
        print('YES')
    else:
        print('NO')

inFile.close()
