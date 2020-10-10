dictionary, result = dict(), dict()

for _ in range(int(input())):
    key, values = input().split(' - ')
    dictionary[key] = values.split(', ')

for key in dictionary.keys():
    for val in dictionary[key]:
        result.setdefault(val, []).append(key)

print(len(result))
for key in sorted(result.keys()):
    print(key, end=' - ')
    print(*sorted(result[key]), sep=', ')