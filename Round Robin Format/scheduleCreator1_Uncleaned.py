from itertools import combinations

teams = ['a','b','c','d', 'e'] # works well for 5, 6, 7, 8, 9, 10
lis = []
for match in combinations(teams, 2):
    lis.append(f'{match[0]} vs {match[1]}')
# print(lis)

# lis = ['a vs b', 'a vs c', 'a vs d', 'a vs e', 'b vs c', 'b vs d', 'b vs e', 'c vs d', 'c vs e', 'd vs e']
#  (start with min and max & after select last)
trav = []
trav.append(lis[0])
# print(trav)
curr = 1
trav.append(lis[len(lis)-1])
# print(trav)

while len(trav) != len(lis):
    next = [x for x in teams if x not in [trav[-1][0], trav[-1][-1], trav[-2][0], trav[-2][-1]]]
    # print([trav[-1][0], trav[-1][-1], trav[-2][0], trav[-2][-1]])
    # print(next)
    travNext = f"{next[0]}: {trav[-2][0]}, {trav[-2][-1]}"
    # print(travNext)
    # print('loop:', curr)
    buildstrLast1 = f'{travNext[0]} vs {travNext[-1]}'
    buildstrLast2 = f'{travNext[-1]} vs {travNext[0]}' 
    # print(buildstrLast1, buildstrLast2)

    buildstrFirst1 = f'{travNext[0]} vs {travNext[3]}'
    buildstrFirst2 = f'{travNext[3]} vs {travNext[0]}'
    # print(buildstrFirst1, buildstrFirst2)

    # break

    if buildstrLast1 in lis:
        if buildstrLast1 not in trav:
            trav.append(buildstrLast1)
        else:
            trav.append(buildstrFirst1)
    elif buildstrLast2 in lis:
        if buildstrLast2 not in trav:
            trav.append(buildstrLast2)
        else:
            trav.append(buildstrFirst2)

    curr += 1

# print('\nbefore manipulation')
# print(trav)
# print(len(lis), len(trav), len(set(trav)))

# print('\nafter manipulation')
temp = []
def remInvalid():
    for i in trav:
        if i not in lis:
            trav.remove(i)

def remDuplicates():
    for i in trav:    
        if i not in temp:
            temp.append(i)

remInvalid()
remDuplicates()
trav = temp
# print(trav)
# print(len(lis), len(trav), len(set(trav)))

# print('\nnot present')
notPresent = [x for x in lis if x not in trav]
# print(notPresent, '\n')

for np in notPresent:
    # for i in range(len(trav)-1):
    i = 0
    # print('w')
    while i < len(lis):
        # print('wh')
        checkElements = [ trav[i][0], trav[i][-1], trav[i+1][0], trav[i+1][-1]]
        # print(checkElements)
        # print(i, i+1, trav[i][0], trav[i+1][-1])
        
        if all(element not in checkElements for element in [np[0], np[-1]]):
            # print(np, '->', i,':', i+1, checkElements)
            trav.insert(i+1, np)
            # notPresent.remove(np)
            i = len(lis)
            # print(notPresent, i)
            # break
        else:
            i += 1

# print('\n')
# print(trav)
# print(len(lis), len(trav), len(set(trav)), sorted(trav) == sorted(lis))


while sorted(trav) != sorted(lis):
    remInvalid()
    remDuplicates()

print(trav)
# print(len(lis), len(trav), len(set(trav)), sorted(trav) == sorted(lis))
