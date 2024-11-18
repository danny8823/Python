f = open("/Users/danny714/Desktop/Python/Day 24/test.txt", "r", encoding="utf-8")

with open("/Users/danny714/Desktop/Python/Day 24/test.txt", "w", encoding="utf-8") as file:
    file.write('hello dear')
    file.write('\nBye dear')

content = f.read()
print(content)
