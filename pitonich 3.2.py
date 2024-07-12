with open("input.txt", "r") as file:
    dictionary = dict(eval(file.read()))
anser = {}
for stores in dictionary.values():
    for produkt in dict(stores).items():
        if produkt[0] not in anser:
            anser[produkt[0]] = produkt[1]
        else:
            anser[produkt[0]] += produkt[1]
print(anser)
with open('output.txt', 'w') as file:
    for produkt in anser:
        file.write(produkt + ":" + " " + str(anser[produkt])+'\n')