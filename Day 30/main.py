# with open('a_file.text') as file:
#     file.read()

# KeyError
# a_dictionary = {'key': 'value'}
# value = a_dictionary['non_existent_key']

# IndexError
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[0]

# TypeError
# text = 'abc'
# print(text + 5)

try:
    file = open("/Users/danny714/Desktop/Python/Day 30/a_text.txt")
    a_dictionary = {'key': 'value'}
    print(a_dictionary['key'])
except FileNotFoundError:
    file = open("/Users/danny714/Desktop/Python/Day 30/a_text.txt", "w")
    file.write('something')
except KeyError as error_message:
    print('That key does not exist', error_message)
else:
    content = file.read()
    print(content)
finally:
    raise KeyError('Hi')

height = int(input("Height: "))
weight = int(input("Weight: "))

if height > 7:
    raise ValueError("Human Height should not be over 8 feet.")

bmi = (weight/(height*height)) * 703

print(bmi)
