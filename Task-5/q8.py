'''8. Employee Skill Grouping
A company receives a list of employee skill codes represented as strings. 
Employees having the same set of characters in their skill codes belong to the same skill category, 
even if the characters appear in a different order. 
The HR system needs to organize employees into appropriate skill groups.
'''
def group_anagrams(words):
    groups = {}

    for word in words:

        key = ''.join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


skills = list(map(str, input().split()))

print(group_anagrams(skills))