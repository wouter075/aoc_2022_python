with open('day1.txt') as f:
    lines = [line.rstrip() for line in f]

part1 = 0
part2 = 0

calories = []
calorie_list = []

for line in lines:
    if line == '':
        total_calories = sum(calories)
        if total_calories > part1:
            part1 = total_calories

        calorie_list.append(total_calories)
        calories = []
    else:
        calories.append(int(line))

calorie_list.append(sum(calories))
calorie_list.sort(reverse=True)
part2 = sum(calorie_list[:3])

print(part1)
print(part2)
