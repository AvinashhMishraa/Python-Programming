# file_path = 'C:\Users\user\Python_Programming\example.txt'

# with open(file_path, 'r') as file:
#     content = file.read()
#     print(content)


file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

