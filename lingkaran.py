import math
r = float (input(" masukan jari-jari lingkaran : "))

luas = math.pi*(r*r)
keliling = 2*math.pi*r

print ("luas lingkaran \t\t= ",luas)
print ("keliling lingkaran\t= ",keliling)

print ("luas lingkaran\t\t= ",format(luas,'.2f'))
print ("keliling lingkaran\t= ",format(keliling,'.2f'))