# Si el numero va de 0 a 9, escribir: 'El numero tiene un digito'
# Si el numero va de 10 a 99, escribir: 'El numero tiene dos digitos'
# Si el numero va de 100 a 999, escribir: 'El numero tiene tres digitos'
# Si el numero va de 1000 a 9999, escribir: 'El numero tiene cuatros digitos'


numero = int( input('Ingrese un numero: ') )

#   inferior    superior
if numero>=0 and numero<=9: #¿el numero esta entre el 0 y el 9?
    print('El numero tiene un digito')
elif numero>=10 and numero<=99: #¿el numero esta entre el 10 y el 99?
    print('El numero tiene dos digitos')
elif numero>=100 and numero<=999: #¿el numero esta entre el 100 y el 999?
    print('El numero tiene tres digitos')
elif numero>=1000 and numero<=9999: #¿el numero esta entre el 100 y el 999?
    print('El numero tiene cuatro digitos')


else: 
    print('este mensaje se muestra si fallan todas las validaciones')