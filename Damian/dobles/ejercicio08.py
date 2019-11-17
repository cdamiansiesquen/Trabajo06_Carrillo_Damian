import os
nombre, precio01, precio02, precio03 = " , " , 0 , 0 , 0

# imput
nombre = os.sys.argv [ 1 ]
precio01 = int (os.sys.argv [ 2 ])
precio02 = int (os.sys.argv [ 3 ])
precio03 = int (os.sys.argv [ 4 ])

# processing
total = (precio01 + precio02 + precio03)

# verificador
comprobando = (total >= 50 )

# output
print ( " ############################## " )
print ( " #negocios linares " )
print ( " #variables: cantidad: " )
print ( " nombre: " , nombre)
print ( " # precio01: " , precio01)
print ( " # precio02: " , precio02)
print ( " # precio03: " , precio03)
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si supera los 50 soles regalar un plato
if (comprobando ==  True ):
    print ( " se ha ganado un plato " )
else :
    print ( " volveremos pronto " )
# fin_if
