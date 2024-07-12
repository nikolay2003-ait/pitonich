try:
    with open('cities.txt','r') as text_file:
        text = text_file.read()
except FileNotFoundError:
    print("This file does not exist")
namber = int(input("Enter a number: "))
with open("cities.txt","r") as a:
    file = a.read()
mass = file.split('\n')

dictionary = {}
sert_dictionary = {}
for line in mass:
    city = line[:line.index(':')]
    population = line[line.index(':')+2:]
    dictionary[city] = population
print(dictionary)
for city in dictionary:
    if int(dictionary[city]) > namber:
        sert_dictionary[city] = dictionary[city]
print(sert_dictionary)
names = sert_dictionary.keys()
sorted_names = sorted(names)
print(sorted_names)
with open('filtered_cities.txt','w') as file:
    for city in sorted_names:
        file.write(city+":"+" "+sert_dictionary[city] + '\n')






