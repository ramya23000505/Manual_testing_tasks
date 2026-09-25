'''
1. Student Attendance Analysis
A college maintains the daily attendance details of its students in the form of a list containing student IDs. 
Some students may have attended multiple sessions on the same day. 
The administration wants to identify the longest continuous sequence of sessions in which no student ID is repeated. 
Develop a solution that determines the maximum length of such a sequence.
'''
# Problem: Longest sequence without repeated student ID

def longest_unique(attendance):
    seen = set()
    left=0
    maxi=0

    for right in range(len(attendance)):
        while attendance[right] in seen:
            seen.remove(attendance[right])
            left +=1
        seen.add(attendance[right])
        maxi = max(maxi, right-left+1)
    return maxi

attendance = list(map(int, input().split()))
print('maximum length of unique student IDs:', longest_unique(attendance))     