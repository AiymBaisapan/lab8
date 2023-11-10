def all_true_elements(tuple_elements):
    return all(tuple_elements)

my_tuple = (True, True, True, False)
result = all_true_elements(my_tuple)

if result:
    print("All elements in the tuple are True.")
else:
    print("Not all elements in the tuple are True.")
