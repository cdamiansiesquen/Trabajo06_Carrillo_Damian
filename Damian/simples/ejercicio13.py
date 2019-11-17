import os
precio_de_arroz_con_pato, precio_de_jarras_de_chicha, precio_ceviche=0 , 0 , 0
#INPUT
precio_ceviche = int (os.sys.argv[ 1 ])
precio_de_jarras_de_chicha = int (os.sys.argv[ 2 ])
precio_de_arroz_con_pato = int (os.sys.argv[ 3 ])
# Processing
total = (precio_de_arroz_con_pato + precio_de_jarras_de_chicha + precio_ceviche)
#Verificador
comprobando = (total >= 120)
#OUPUT
print( "#####################################")
print( "#       Rest. MI RAMADA              ")
print( "#####################################")
print( "#")
print( "#variables:   cantidad")
print( "precio de arroz con pato:", precio_de_arroz_con_pato)
print( "precio de jarras de chicha:", precio_de_jarras_de_chicha)
print( "precio ceviche:", precio_ceviche)
print( "precio total:", total)
print( "#####################################")

#condicion simple
# Si el total supera los 120, se gano un descuento de 30 soles
if ( comprobando == True ):
    print(" usted gano el descuento de 30 soles")
#fin_if
