import os
nombre, fierro, cemento, tubo = " , " , 0 , 0 , 0

# imput
nombre = os.sys.argv [ 1 ]
fierro = int (os.sys.argv [ 2 ])
cemento = int (os.sys.argv [ 3 ])
tubo = int (os.sys.argv [ 4 ])

# processing
total = ( fierro + cemento + tubo )

# verificador
comprador = (total >= 700 )

# output
print ( " ############################## " )
print ( " # Ferrotumi" )
print ( " #variables: cantidad: " )
print ( " nombre: " , nombre)
print ( " #fierro: " , fierro)
print ( " #cemento: " , cemento)
print ( " #tubo: " , tubo)
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si es comprador  tenga 50% de descuento
if (comprador ==  True ):
    print ( " se ha ganado un descuento " )
if ( 640> comprador < 700 ):
    print ( " consiga mas descuentos " )
if (comprador < 630 ):
    print ( " vuelva pronto" )
# fin_if
