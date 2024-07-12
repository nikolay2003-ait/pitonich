stroka = input("bukvi ")
amount = 0
spisochek = ''
mass = []

while stroka.islower() == False:
    stroka = input('try agane ')
n = int(input('chislo '))
while n > len(stroka):
    n = int(input('try agane '))

for i in range(len(stroka)-n+1):
    spisochek += stroka[i]
    for j in range(i+1, n+i):
        if stroka[j] in spisochek:
            break
        spisochek += stroka[j]
    if len(spisochek) == n:
        amount += 1
        mass.append(spisochek)
    spisochek = ''
print(mass)
print(amount)


