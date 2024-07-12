a = input()
chisla = "1234567890"
chiselko = ''
mass = []
for i in range(len(a)):
    if a[i] in chisla:
        chiselko += a[i]
    else:
        if chiselko != '':
            k = int(chiselko)
            mass.append(k)
            chiselko = ''
if chiselko != '':
    mass.append(int(chiselko))
print(mass)
print(sum(mass))




