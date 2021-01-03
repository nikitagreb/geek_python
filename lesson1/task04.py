string_number = input("Введите число: ")
lenght = len(string_number)
index = 0
max_number = 0

while index != lenght:

    if max_number == 0:
        max_number = int(string_number[index])

    if string_number[index] > max_number:
        max_number = int(string_number[index])

    index = index + 1

print(f"Самая большая цифра {max_number}")
