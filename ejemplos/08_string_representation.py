a = 1
b = 2
texto_uno = 'De vez en cuando'
texto_dos = 'la vida'
print(f'Dice un cantautor que "{texto_uno} {texto_dos} toma conmigo café" ')

exit(0)

# recomended
print(f'El valor de a = {a} y el de b es {b}, y el valor de a menos b = {b}')

# Extended
print('El valor de a = {first} y el de b es {second}, y el valor de a menos b = {second}'.format(first=a, second=b))

my_multi_lineal_string = f'''{a}Minions ipsum baboiii para tú potatoooo. Butt bappleees poulet tikka masala baboiii
 jiji tatata bala tu wiiiii bappleees poulet tikka masala wiiiii. Poulet tikka masala jeje potatoooo poulet tikka
  masala jiji. Poulet tikka masala wiiiii poopayee tank yuuu! Tank yuuu! Uuuhhh baboiii me want bananaaa! Tatata bala
   tu tatata bala tu. Tulaliloo pepete para tú daa aaaaaah poopayee poopayee. Para tú jiji la bodaaa me want bananaaa!
    Ti aamoo! chasy la bodaaa poopayee butt hana dul sae ti aamoo! Tatata bala tu.{a}'''

print(my_multi_lineal_string)
print('el valor de a =', a)

if a > 0:
    print('a es mayor que 0')
