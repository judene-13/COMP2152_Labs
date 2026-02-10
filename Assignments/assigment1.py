"""
Author: <Judene Brown>
Assignment: #1
"""
gym_member = "Alex Alliton" #string
preferred_weight_kg = 20.5 #float
highest_reps = 25 #integer
membership_active = True #boolean


#workout_stats is the dictionary with keys that are string data types (friends names) and tuple value containing integers for the workout minutes
workout_stats= {"Alex": (30, 12,21),
                "Jamie":(45, 21,43),
                "Taylor":(50,30,60)}

"""A for loop is used to calculate the total workout minutes for each friend by using 
 the keys and values from the dictionary workout_stats. """
for name, minutes in list(workout_stats.items()):
	total=0
	for m in minutes:
		total +=m
	workout_stats[name+"_Total"] = total

	if total >= 120:
		print("Great job staying active", name)
	
friend_name = input("Enter your friends name: ")

if friend_name in workout_stats:
	yoga, running, weightlifting = workout_stats[friend_name]
	total_minutes = workout_stats[friend_name + "_Total"]

	print(f"\nWorkout minutes for {friend_name}:")
	print(f"Yoga: {yoga}")
	print(f"Running: {running}")
	print(f"Weightlifting: {weightlifting}")
	print(f"Total workout minutes: {total_minutes}")

else:
	print(f"Friend {friend_name} not found in the records.")

# the workout_list is a nested lists which has the workout minutes from the dictionary as integers
workout_list = [list(minutes) for name, minutes in workout_stats.items() if "_Total" not in name]

matrix= workout_list

rows_1_to_2 = [row[0:2] for row in matrix[0:3]]
print(rows_1_to_2)
sub_matrix = [row[2] for row in matrix[1:3]]
print(sub_matrix)


highest_total = -1
highest_name= ""

lowest_total= 999999
lowest_name=""

for key, value in workout_stats.items():
	if "_Total" in key:
		friend = key.replace("_Total", "")
		total = value

		if total > highest_total:
			highest_total = total
			highest_name = friend

		if total < lowest_total:
			lowest_total = total
			lowest_name = friend


print("Highest total workout minutes", highest_name)
print("Lowest total workout minutes", lowest_name)
