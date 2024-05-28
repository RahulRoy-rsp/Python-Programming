from itertools import combinations

def generate_matches(teams):
    lis = []
    for match in combinations(teams, 2):
        lis.append(f'{match[0]} vs {match[1]}')
    return lis

def buildSchedule(teams):
    lis = generate_matches(teams)
    trav = [lis[0], lis[-1]]

    while len(trav) != len(lis):
        next_team = [x for x in teams if x not in [trav[-1][0], trav[-1][-1], trav[-2][0], trav[-2][-1]]][0]
        trav_next = f"{next_team}: {trav[-2][0]}, {trav[-2][-1]}"
        buildstr_last1 = f'{trav_next[0]} vs {trav_next[-1]}'
        buildstr_last2 = f'{trav_next[-1]} vs {trav_next[0]}'
        buildstr_first1 = f'{trav_next[0]} vs {trav_next[3]}'
        buildstr_first2 = f'{trav_next[3]} vs {trav_next[0]}'

        if buildstr_last1 in lis:
            if buildstr_last1 not in trav:
                trav.append(buildstr_last1)
            else:
                trav.append(buildstr_first1)
        elif buildstr_last2 in lis:
            if buildstr_last2 not in trav:
                trav.append(buildstr_last2)
            else:
                trav.append(buildstr_first2)

    return trav

def cleanSchedule(trav, lis):
    temp = []

    def remove_invalid():
        for i in trav:
            if i not in lis:
                trav.remove(i)

    def remove_duplicates():
        for i in trav:    
            if i not in temp:
                temp.append(i)

    remove_invalid()
    remove_duplicates()
    return temp

def addMissedMatches(trav, lis):
    not_present = [x for x in lis if x not in trav]

    for np in not_present:
        i = 0
        while i < len(lis):
            check_elements = [trav[i][0], trav[i][-1], trav[i+1][0], trav[i+1][-1]]
            
            if all(element not in check_elements for element in [np[0], np[-1]]):
                trav.insert(i+1, np)
                i = len(lis)
            else:
                i += 1

def main():
    num_teams = int(input("Enter the number of teams: "))
    teams = [input(f"Enter team {i+1}: ") for i in range(num_teams)]
    schedule = buildSchedule(teams)
    schedule = cleanSchedule(schedule, generate_matches(teams))
    addMissedMatches(schedule, generate_matches(teams))
    
    print("\nFinal Schedule:")
    for match in schedule:
        print(match)

if __name__ == "__main__":
    main()
