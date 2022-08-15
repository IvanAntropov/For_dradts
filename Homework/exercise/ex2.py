x = input(f'Enter value X: ')
y = input(f'Enter value Y: ')
z = input(f'Enter value Z: ')
first_part = not (x or y or z)
second_part = not x and not y and not z
if first_part == second_part:
    print(f'True')
else:
    print(f'False')