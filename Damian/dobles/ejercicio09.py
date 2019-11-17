import os
#Declarar variables
fierro, cemento, tubos=0 , 0 , 0

#input
fierro = int(os.sys.arguv[1])
cemento = int(os.sys.arguv[2])
tubos = int(os.sys.arguv[3])

#processing
total = ( fierro + cemento + tubos )

#verificador
comprador = ( total >= 300 )

#ouput
print( "##################################")
print( "#           Ferrotumi             ")
print( "#variables:         cantidad:     ")
print( "#fierro:", fierro)
print( "#cemento:", cemento)
print( "#tubos:", tubos)
print( "#total:", total)
print( "##################################")
#Condicion
#si es comprador se puede llevar un descuento
if( comprador == True ):
    print(" ha ganado un descuento ")
else:
    print(" vuelva pronto ")
#fin if
