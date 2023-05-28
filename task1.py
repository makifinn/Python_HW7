stih = input('введите стих: ').split()
vowes = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
counts = []

for i in range(len(stih)):
    count = 0
    for j in stih[i]:
        if j in vowes:
            count += 1
    counts.append(count)


if sum(counts) / len(counts) == counts[0]:
    print('Парам пам-пам')
else:
    print('Пам парам')