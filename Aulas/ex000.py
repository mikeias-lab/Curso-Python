v1, v2, v3 = map(int, input().split())
maiorAB = (v1 + v2 + abs(v1 - v2)) / 2
if maiorAB > v3:
    print('{:.0f} eh o maior'.format(maiorAB))
else:
    print('{:.0f} eh o maior'.format(v3))
