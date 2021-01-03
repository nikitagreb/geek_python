current_result = int(input("Введите результат первого дня в км: "))
desired_result = int(input("Введите желаемоего количество киломметров: "))
day = 1

while current_result < desired_result:
    current_result = current_result * 1.1
    day = day + 1

print(f"На {day} день вы достигните желаемого результата")
