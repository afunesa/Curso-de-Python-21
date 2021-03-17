#numero / 23 , el resto cotejar en tabla:
#Posición     0   1   2   3  4   5   6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22
# #Letra        T   R   W   A  G   M   Y  F  P  D  X    B   N   J   Z   S   Q   V   H   L   C   K   E
# w=input("Introduce el número de tu DNI, no en texto, por favor: ")
# w=int(w)
# letras=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
# print('Tachannn...La letra del tu DNI es: ', letras[w%23])

tabla_letras = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
mi_dni = int(23781594)

resto = mi_dni % 23

print(f'La letra para el DNI {mi_dni} es {tabla_letras[resto]}')
