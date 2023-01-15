from itertools import permutations


for p in permutations([0, 1, 2]):
    l = []
    print(f'p -> {p}')
    for i in range(5):
        l.append(i)
    print(f'l -> {l}')

print('-----------------------------')

for t in permutations([x for x in range(3)]):
    l = []
    print(f't -> {t}')
    for z in range(5):
        l.append(z)
    print(f'l -> {l}')


