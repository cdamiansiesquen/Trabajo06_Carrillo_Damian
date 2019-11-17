import os
#DECLARAR VARIABLES
precio_cambio_de_aceite_de_moto, precio_de_lavado_de_moto, precio_de_afinamiento = 0, 0 ,0

#imput
precio_cambio_de_aceite_de_moto = int(os.sys.argv [ 1 ])
precio_de_lavado_de_moto = int(os.sys.argv [ 2  ])
precio_de_afinamiento = int(os.sys.argv [ 3 ])

#procesing
total = ( precio_cambio_de_aceite_de_moto + precio_de_lavado_de_moto + precio_de_afinamiento )

#verificador
descuento = ( total >=25 )

#output
print( "##############################")
print( "#LUBRICENTRO_MICHELL")
print( "#variables:                cantidad:")
print( "#precio cambio de_aceite de moto:",   precio_cambio_de_aceite_de_moto )
print( "#precio de lavado de moto:",   precio_de_lavado_de_moto )
print( "#precio de afinamiento:",  precio_de_afinamiento )
print( "#total:", total)
print("##############################")

#condicion simple
#si supera 20, descuento
if ( descuento == True):
    print( " gano puntos para un sorteo de productos de motos " )
if (  18 < descuento < 25 ):
    print( " compra mas y mas probabilidades de ganar " )
if ( descuento < 17 ):
    print( " vuelva pronto " )
#fin_if
