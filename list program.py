# A list of integers
number_list = [1,2,3,4,5]
print(number_list)

# A list of strings
fruits_list = ['apple', 'banana', 'cherry']
print(fruits_list)

# A list of flloats
float_list = [1.5, 2.7, 3.14, 4.8, 5.0]
print(float_list)

#A list of booleans
boolean_list = [ True, False, True, True, False]
print(boolean_list)

#A mixed list
mixed_list = [1, 'apple', 3.14, True]
print(mixed_list)              

# Accessing List Element
fruits_list = ['apple', 'banana', 'cherry']
print(fruits_list[0])
print(fruits_list[1])
print(fruits_list[-1])
print(fruits_list[-2])

# Modifying list
fruits_list[1] = 'blueberry'
print(fruits_list)

# Adding Element
fruits_list.append('orange')
print(fruits_list)

# Insert
fruits_list.insert(1, 'kiwi')
print(fruits_list)

#Removing Element
fruits_list.remove('kiwi')
print(fruits_list)

# pop: remove an element by index and returns it
last_fruit = fruits_list.pop()
print(last_fruit)

# Clear
fruits_list.clear()
print(fruits_list)

# Slicing List
numbers = [0,1,2,3,4,5,6]
print(numbers[1:4])
print(numbers[:3])
print(numbers[4:])

# Useful List Methods:
# len(list): Returns the number of elements in the list.
print(len(numbers))

# list.sort()
numbers.sort()
print(numbers)

# list.reverse()
print(numbers)


# list.index(item)
fruits_list = ['apple', 'banana', 'cherry']
print(fruits_list.index('apple'))

# list.coount(item)
print(fruits_list.count('cherry'))
























    
