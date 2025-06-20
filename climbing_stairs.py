
def rec(n: int):
    '''This is a recursive function which adds the rec of its previous numbs'''
    if n == 1:
        return 1
    if n == 0:
        return 1
    op1 = rec(n-1)
    op2 = rec(n-2)
    return op1+op2


def ways(n: int):
    try:
        if not (1 <= n <= 45):
            print('ⓘ Invalid number of steps...')
        ans = rec(n)
        int(ans)
        #return ans
        print(f"\nThere are {ans} ways to climb {n} steps")
    except Exception as e:
        print(f'An unexpected error occured: {e}')
        
num_of_steps = input('\n Enter Number of steps: ')
num_of_steps = int(num_of_steps)
ways(num_of_steps)