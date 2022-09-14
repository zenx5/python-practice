# Tres amigos se consiguieron un tesoro pirata
# Este tesoro tenia una cantidad de monedas que el usuario debe indicar
# Tambien el usuario debe decir cuanto se quedo cada amigo
# Al final mostrar los porcentajes


tesoro = int( input('Indique cuantas monedas tiene el tesoro: ') )

print('Quedan ', tesoro)
amigo1 = int( input('Indique cuantas monedas le toco al amigo 1: ') )

print('Quedan ', tesoro-amigo1)
amigo2 = int( input('Indique cuantas monedas le toco al amigo 2: ') )

print('Quedan ', tesoro-amigo1-amigo2)
amigo3 = int( input('Indique cuantas monedas le toco al amigo 3: ') )

# ESTO ES IMPORTANTE
###############
porcentaje1 = amigo1*100/tesoro

porcentaje2 = amigo2*100/tesoro

porcentaje3 = amigo3*100/tesoro
###############

print('Porcentaje amigo 1: %i ' % porcentaje1 )

print('Porcentaje amigo 2: %i ' % porcentaje2 )

print('Porcentaje amigo 3: %i ' % porcentaje3 )