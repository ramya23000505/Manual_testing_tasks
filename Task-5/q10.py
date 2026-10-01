'''10. Hospital Appointment Scheduling
A hospital receives appointment requests represented by starting and ending times.
Some appointments overlap with each other.
The scheduling system needs to combine overlapping appointment periods so that the final schedule contains only non-overlapping time ranges.
'''

def merge_intervals(intervals):

    intervals.sort()

    result = [intervals[0]]

    for start, end in intervals[1:]:

        last_end = result[-1][1]

        if start <= last_end:
            result[-1][1] = max(last_end, end)

        else:
            result.append([start, end])

    return result


n = int(input("Enter number of appointments: "))

appointments = []

for i in range(n):
    start, end = map(int, input(f"Enter appointment {i + 1} (start end): ").split())
    appointments.append([start, end])

print("Merged appointments:", merge_intervals(appointments))