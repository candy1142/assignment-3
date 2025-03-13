fruits_tuple = ('apple', 'banana', 'cherry', 'apple')
#print(fruits_tuple.count('a'))

letter = input("Enter an alphabet:")
'''element = fruits_tuple[3]
count_element = element.count(letter)
print(f"Letter {letter} repititions in the element {element}:{count_element}")
'''

count_all= 0
for string in fruits_tuple:
    count_all = count_all + string.count(letter)
print(f"Letter {letter} repitition in the tuple: {count_all}")
