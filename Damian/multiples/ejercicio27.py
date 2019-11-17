import os
nota1, nota2 , nota3 =  0 , 0 , 0

# imput
nota1 = int (os.sys.argv [ 1 ])
nota2 = int (os.sys.argv [ 2 ])
nota3 = int (os.sys.argv [ 3 ])

# processing
promedio = ( nota1 + nota2 + nota3 )/3

# verificador
aprobado = (promedio == 20 )

# output
print ( " ############################## " )
print ( " # UNPRG " )
print ( " #variables: cantidad: " )
print ( " #nota1: " , nota1)
print ( " #nota2: " , nota2)
print ( " #nota3: " , nota3)
print ( " promedio: " , promedio)
print ( " ############################## " )

# condicion simple
# si es aprobado, paso de año
if (aprobado ==  True ):
    print ( " Felicitaciones " )
if ( 12 < aprobado < 16 ):
    print ( " Estudie mas " )
if (aprobado < 11 ):
    print ( " nos vemos el proximo año " )
# fin_if
