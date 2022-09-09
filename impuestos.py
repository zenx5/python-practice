# Menos de 100€       	=>          5%
# Entre 100€ y 200€	    =>          15%
# Entre 200€ y 350€	    =>          20%
# Entre 350€ y 600€	    =>          30%
# Más de 600€	        =>          45%

sueldo = input( 'Cuál es el sueldo? ')


if sueldo<100
   print(Su impuesto es de 5%)
elif sueldo>=100 and <=200
   print(Su impuesto es de 15%)
elif sueldo>=200 and <=350
   print(Su impuesto es de 20%)
elif sueldo>=350 and <=600
   print(Su impuesto es de 30%)
elif sueldo>=600
   print(Su impuesto es de 45%)
