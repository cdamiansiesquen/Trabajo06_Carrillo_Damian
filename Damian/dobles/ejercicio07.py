import os
nombre, zapatos, chompa, casaca = " , " , 0 , 0 , 0

# imput
nombre = os.sys.argv [ 1 ]
zapatos = int (os.sys.argv [ 2 ])
chompa = int (os.sys.argv [ 3 ])
casaca = int (os.sys.argv [ 4 ])

# processing
total = (zapatos + chompa + casaca)

# verificador
comprobando = (total >= 80 )

# output
print ( " ############################## " )
print ( " # Real plaza chiclayo " )
print ( " #variables: cantidad: " )
print ( " nombre: " , nombre)
print ( " # zapatos: " , zapatos)
print ( " # chompa: " , chompa)
print ( " # casaca: " , casaca)
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si supera los 80 soles, gana un descuento
if (comprobando ==  True ):
    print ( " se ha ganado el descuento " )
else :
    print ( " vuelva pronto " )
# fin_if
