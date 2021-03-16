# https://www.hackerrank.com/challenges/nested-list/problems

# Authors notes:
# - learned about lambdas finally they're not scary
# - sorted() function works on lists of lists but .sorted() method does not

# Goal:
# Print the name(s) of any student(s) having the second lowest grade in. If there are
# multiple students, order their names alphabetically and print each one on a new line.

# https://stackoverflow.com/questions/26779618/python-find-second-smallest-number
# The above link is for a list but I need to use my brainpower somehow to
# modify Martijn's code to act on a list of lists
def second_smallest(number_list_of_list):
    m1, m2 = float('inf'), float('inf')
    for x in number_list_of_list:
        if x[1] <= m1:
            m1, m2 = x[1], m1
        # This is the edited part because the original code doesn't account for
        # there being duplicate smallest values
        # So we have to check to make sure that x[1] isn't the same as m1 then make
        # m2 that new x[1] which is the second smallest number
        elif x[1] != m1:
            m2 = x[1]
            break
    return m2

if __name__ == '__main__':
    # the original code did not have n_s_list but I don't know how you would make
    #a list WITHIN a for loop
    n_s_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        n_s_list.append([name, score])


    # Store the second lowest grade number in a variable
    # sorted byt the lambda is key so the list goes from smallest to largest
    second_lowest_num = second_smallest(sorted(n_s_list, key=lambda x: x[1]))
    # print('second_lowest_num:', second_lowest_num)

    # List comprehension to return the tuples that have values of second_lowest_num
    second_lowest_grade = [i for i in n_s_list if i[1] == second_lowest_num]

    for i in sorted(second_lowest_grade):
        print(i[0])
