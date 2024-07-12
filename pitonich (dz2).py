slovo = input()

caunter = 0
while len(slovo) < 2:
    a = input("try agan ")
calculator = set()
for i in range(len(slovo)):
    for j in range (i+2,len(slovo)+1):
        srez = slovo [i:j]
        rev = srez [::-1]
        if srez == rev:
            calculator.add(srez)
print(len(calculator))
print(calculator)



