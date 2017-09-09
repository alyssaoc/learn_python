for income in range(15000, 2000000, 500000):

    if income < 10000:
        tax_coefficient = 0.0
    elif income < 30000:
        tax_coefficient = 0.2
    elif income < 1000000:
        tax_coefficient = 0.35
    else:
        tax_coefficient = 0.45

    print('If I make', income,': I will pay', income * tax_coefficient,'in taxes')