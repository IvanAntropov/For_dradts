def Input_values(write_what_you_want):
    for_checking = False
    while not for_checking:
        try:
            number = int(input(f'{write_what_you_want}'))
            if number > 4 or number < 1:
                for_checking = False
                print('Try again.Enter a number of quarter from 1 to 4.')
            else:
                for_checking = True
        except ValueError:
            print('Try again.Enter a number of quarter from 1 to 4.')
    return number


def Checking(q):
    xy = ['X', 'Y']
    pos_neg = ['+', '-']
    if q == 1:
        print(
            f'For {xy[0]} From 0 to {pos_neg[0]} ∞ \nFor {xy[1]} From 0 to {pos_neg[0]} ∞')
    elif q == 2:
        print(
            f'For {xy[0]} From 0 to {pos_neg[1]} ∞ \nFor {xy[1]} From 0 to {pos_neg[0]} ∞')
    elif q == 3:
        print(
            f'For {xy[0]} From 0 to {pos_neg[1]} ∞ \nFor {xy[1]} From 0 to {pos_neg[1]} ∞')
    else:
        print(
            f'For {xy[0]} From 0 to {pos_neg[0]} ∞ \nFor {xy[1]} From 0 to {pos_neg[1]} ∞')


quarter = Input_values("Enter quarter: ")
Checking(quarter)