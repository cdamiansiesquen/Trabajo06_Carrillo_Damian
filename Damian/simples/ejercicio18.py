import os
precio_de_silla, precio_de_mesas, precio_adornos= 0 , 0 , 0
#INPUT
precio_de_silla = int(os.sys.argv[ 1 ])
precio_de_mesas = int(os.sys.argv[ 2 ])
precio_adornos = int(os.sys.argv[ 3 ])
# Processing
total = (precio_de_silla + precio_de_mesas + precio_adornos)
#Verificador
comprobando = ( total >= 250 )
#OUPUT
print( "#####################################")
print( "#       Bazar-FLorcita                    ")
print( "#####################################")
print( "#")
print( "#variables:   cantidad")
print( "precio de silla:", precio_de_silla)
print( "precio de mesas:", precio_de_mesas)
print( "precio de adornos:", precio_adornos)
print( "precio total: s/. ", total)
print( "#####################################")

#condicion simple
# Si el total supera los 250, se gana un mesa
if ( comprobando == True ):
    print(" usted gano la mesa ")
#fin_if
