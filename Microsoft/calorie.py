date = input("Today's date? ")
breakfast_calories = int(input("Breakfast calories? "))
lunch_calories = int(input("Lunch calories? "))
dinner_calories = int(input("Dinner calories? "))
snack_calories = int(input("Snack calories? "))

sum = breakfast_calories + lunch_calories + dinner_calories + snack_calories

print("Calorie content for " + date + " : " + str(sum))