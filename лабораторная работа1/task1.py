numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

short_list = numbers[:4] + numbers[5:]

sum = sum(short_list)
count = len(short_list) + 1

average = sum / count

numbers[4] = average

print("Измененный список:", numbers)
