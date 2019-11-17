import os
precio_de_laptop, precio_de_mouse, precio_cpu = 0 , 0 , 0
#INPUT
precio_cpu = int (os.sys.argv[ 1 ])
precio_de_laptop = int (os.sys.argv[ 2 ])
precio_de_mouse = int (os.sys.argv[ 3 ])
# Processing
total = (precio_de_laptop + precio_de_mouse + precio_cpu)
#Verificador
comprobando = ( total >= 600 )
#OUPUT
print( "#####################################")
print( "#       Ventas JUANITO               ")
print( "#####################################")
print( "#")
print( "#variables:   cantidad")
print( "precio de laptop es s/.:",precio_de_laptop)
print( "precio de mouse es s/.:",precio_de_mouse)
print( "precio total: s/. ", total)
print( "#####################################")

#condicion simple
# Si el total supera los 600, entra al sorteo de una PC
if ( comprobando == True ):
    print(" usted entro al sorteo de una PC")
#fin_if

