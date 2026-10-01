'''4. Employee Performance Analysis
A company stores the monthly performance scores of an employee for several months. 
The scores may contain both positive and negative values depending on the employee's performance. 
Management wants to identify the continuous period during which the employee achieved the highest overall performance.
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
