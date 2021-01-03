input_seconds = int(input("Введите секунды: "))

hours = input_seconds // (60 * 60)
minutes = (input_seconds % (60 * 60)) // 60
seconds = input_seconds % 60

print('%d:%d:%d' % (hours, minutes, seconds))
