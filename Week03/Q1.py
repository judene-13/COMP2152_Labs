grades=[85,92,78,95,88]
grades.append(90)
grades.sort()
print(f"Sorted grades:{grades}")

#-1 is always the lowest in the list
print(f"Highest grades: {grades[-1]}")

#0 is the first
print(f"Lowest grades: {grades[0]}")

print(f"Total number of grades: {len(grades)}")