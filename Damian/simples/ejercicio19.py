import os
precio_de_vasos, precio_de_tazas, precio_plato= 0 , 0 , 0
#INPUT
precio_de_vasos=int(os.sys.argv[1])
precio_de_tazas=int(os.sys.argv[2])
precio_plato=int(os.sys.argv[3])
# Processing
total=(precio_de_vasos+precio_de_tazas+precio_plato)
#Verificador
comprobando=(total>=50)
#OUPUT
print("#####################################")
print("#    Tienda JUANITA                  ")
print("#####################################")
print("#")
print("#variables:   cantidad")
print("precio de vasos:", precio_de_vasos)
print("precio de tazas:", precio_de_tazas)
print("precio de plato:", precio_plato)
print("precio total: s/. ", total)
print("#####################################")

#condicion simple
# Si el total supera los 50, se gana la tarjeta dorada
if (comprobando == True):
    print(" usted gano la tarjeta dorada ")
#fin_if
