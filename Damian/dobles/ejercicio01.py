import os
cable, tv, pelicula = 0 , 0 , 0

# imput
cable = int (os.sys.argv [ 1 ])
tv = int (os.sys.argv [ 2 ])
pelicula = int (os.sys.argv [ 3 ])

# processing
total = (cable + tv + pelicula)

# verificador
comprobando = (total >= 150 )

# output
print ( " ############################## " )
print ( " # Feria Balta " )
print ( " #variables: cantidad: " )
print ( " # cable: " , cable )
print ( " # tv: " , tv )
print ( " # pelicula: " , pelicula )
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si supera los 150 soles regalar un descuento
if (comprobando ==  True ):
    print ( " se le a dado un descuento " )
else :
    print ( " vuelva pronto " )
# fin_if
