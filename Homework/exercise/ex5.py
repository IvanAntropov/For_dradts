def Input_values(write_what_you_want):
    for_checking = False
    while not for_checking:
        try:
            number = float(input(f'{write_what_you_want}'))
            for_checking = True
        except ValueError:
            print(
                'Try again. It must be DIGIT. \nIf you wanna enter float number use ".", exampple: 1.25 ')
    return number


def Measure(x1, y1, x2, y2):
    first_step = (x1 - x2)**2
    second_step = (y1 - y2)**2
    third_step = (first_step + second_step)**0.5
    return third_step
    


x1 = Input_values("Enter X for first point: ")
y1 = Input_values("Enter Y for first point: ")
x2 = Input_values("Enter X for second point: ")
y2 = Input_values("Enter Y for second point: ")
print(f'Distance between first and second points is {Measure(x1, y1, x2, y2)} things')