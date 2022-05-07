#ejercicio tienda de libros
print('ingresá los siguientes datos del libro: ')
nombre = input('ingresá el nombre del libro: ')
id = int(input('ingresá el ID del libro: '))
precio = float(input('ingresáel precio del libro:'))
envioGratuito = input('ingresá si el envío es gratuito o no (True o False) :  i')
if envioGratuito == 'True' or 'true' :
    envioGratuito = True
elif envioGratuito == 'False' or 'false' :
    envioGratuito = False
else :
    envioGratuito = 'el valor ingresado es incorrecto, recordá ingressar solo True/False'
print(f'''
    Nombre : {nombre}
    Id : {id}
    Precio : ${precio}
    Envío gratuito : {envioGratuito}
''')
