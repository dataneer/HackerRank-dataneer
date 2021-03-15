
# https://www.hackerrank.com/challenges/list-comprehensions/problem

# Remove all arrays that sume to n = 2 to leave only the valid permutations
# So get an array of True False ones

"""

List Comp:

(values) = []
for (value) in (collection):
    values.append( (expression) )

values = [ (expression) for (value) in (collection)
"""

def list_comp(n):
    list_made = [i for i in range(0,n + 1)]
    return list_made

if __name__ == '__main__':

    # Number inputs
    x = int(input())
    y = int(input())
    z = int(input())

    # Remove all arrays that sum up to n
    n = int(input())

    # Create three lists to return the list of numbers from 0 <= i <= input()
    """
    x_list = [i for i in range(0,x + 1)]
    y_list = [i for i in range(0,y + 1)]
    z_list = [i for i in range(0,z + 1)]
    """
    # Above is a lot of repeating code so why don't we create a function for it?

    x_list = list_comp(x)
    y_list = list_comp(y)
    z_list = list_comp(z)

    # Python | All possible permutations of N lists
    # https://www.geeksforgeeks.org/python-all-possible-permutations-of-n-lists/

    # Use list comprehension to compute all possible permutations
    all_perm = [[i, j, k] for i in x_list
                    for j in y_list
                    for k in z_list]

    """
    valid_perm = []
    for i in all_perm:
        if sum(i) != n:
            valid_perm.append(i)
    """

    valid_perm = [i for i in all_perm if sum(i) != n]

    print(valid_perm)

# Edit: however a lot of people appear to have completed this as a one line so
# I will revisit this problem
