import os
precio_de_ladrillos, precio_de_cemento, precio_yeso= 0 , 0 , 0
#INPUT
precio_de_ladrillos = int (os.sys.argv[1])
precio_de_cemento = int (os.sys.argv[2])
precio_yeso = int (os.sys.argv[3])
# Processing
total = (precio_de_ladrillos + precio_de_cemento + precio_yeso)
#Verificador
comprobando = (total >= 200)
#OUPUT
print( "#####################################")
print( "#       FERROTUMI                    ")
print( "#####################################")
print( "#")
print( "#variables:   cantidad")
print( "precio de ladrillos:", precio_de_ladrillos)
print( "precio de cemento:", precio_de_cemento)
print( "precio de yeso:", precio_yeso)
print( "precio total: s/. ", total)
print( "#####################################")

#condicion simple
# Si el total supera los 200, se gana una bolsa de cemento gratis
if ( comprobando == True ):
    print(" usted gano la bolsa de cemento ")
#fin_if
