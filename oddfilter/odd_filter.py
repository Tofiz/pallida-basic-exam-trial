# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

numbers_list = [1, 2, 3, 4, 5, 8]
odd_numbers = []
def odd_filter(l, o):
    for i in l:
        if i %2 == 0:
            o.append(i)
    return(o)

print(odd_filter(numbers_list, odd_numbers))  # should print [1, 3, 5]


