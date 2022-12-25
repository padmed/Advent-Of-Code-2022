elve_calories = []
with open('input.txt') as elves:
    calories = elves.readlines()

    elve_calorie = 0
    for i in range(len(calories)):
        calorie = calories[i].strip()

        if calorie != '':
            elve_calorie += int(calorie)
        else:
            elve_calories.append(elve_calorie)
            elve_calorie = 0


#Answer for part 2
elve_calories.sort()
top3_elves = elve_calories[-3:]
top3_sum = sum(top3_elves)

print(top3_sum)
