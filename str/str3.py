resp = 'n'
carneirinho = 0
while resp == 'n' or resp == 'N':
    resp = input("Ja dormiu ? ")
    carneirinho += 1
    
print (carneirinho)

resp = 'n'
carneirinho = 0
while resp in 'nN': 
    resp = input("Ja dormiu ? ")
    carneirinho += 1
print(carneirinho)