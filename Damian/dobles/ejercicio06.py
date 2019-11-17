import os
nombre, llantas, carburador, aro = " , " , 0 , 0 , 0

# imput
nombre = os.sys.argv [ 1 ]
llantas = int (os.sys.argv [ 2 ])
carburador = int (os.sys.argv [ 3 ])
aro = int (os.sys.argv [ 4 ])

# processing
total = (llantas + carburador + aro)

# verificador
comprobando = (total >= 150 )

# output
print ( " ############################## " )
print ( " # Cherokee motos " )
print ( " #variables: cantidad: " )
print ( " nombre: " , nombre)
print ( " # llantas: " , llantas)
print ( " # carburador: " , carburador)
print ( " # aro: " , aro)
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si supera los 150 soles regalar unos direccionales
if (comprobando ==  True ):
    print ( " se ha ganado par de direccionales" )
else :
    print ( " vuelva pronto " )
# fin_if
