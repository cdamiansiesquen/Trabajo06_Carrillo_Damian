import os
nombre, brocas, taladro_inalamabrico, tarugos=",", 0, 0 ,0

#imput
nombre = os.sys.argv [ 1 ]
brocas = int (os.sys.argv [ 2 ])
taladro_inalambrico = int(os.sys.argv[3])
tarugos = int (os.sys.argv [ 4 ])

#procesing
total = ( brocas + taladro_inalambrico + tarugos )

#verificador
comprador_compulsivo = ( total >= 120 )

#output
print(" ##############################")
print(" #SODIMAC")
print(" #variables:    cantidad:")
print(" nombre:",       nombre)
print(" #brocas:",     brocas)
print(" #taladro_inalambrico:",  taladro_inalambrico)
print(" #tarugos:",     tarugos)
print(" total:",        total)
print(" ##############################")

#condicion simple
#si s comprador compulsivo mostrar tarjeta visa
if ( comprador_compulsivo == True ):
    print("se gano un maletin para taladro+kit de herramientas")
if ( 100< comprador_compulsivo <120 ):
    print("se gano un kit de herramientas ")
if ( comprador_compulsivo <99 ):
    print("Gracias por su compra")
#fin_if


