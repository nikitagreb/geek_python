proceeds = int(input("Введите выручку вашей фирмы: "))
costs = int(input("Введите издержки вашей фирмы: "))

if proceeds > costs:
    print("У вашей фирмы прибыль")
    profitability = proceeds / costs
    print(f"Рентабельность вашей фирмы: {profitability}")
    employees = int(input("Введите количество сотрудников, которые работают в вашей фирме: "))
    print(f"Прибыль фирмы, в расчете на одного сотрудника составила: {proceeds / employees}")
else:
    print("У вашей фирмы убыток")
