#Desarrolle un programa de línea de comandos, basado en funciones,
# que dado un número identifique si el mismo es par o impar.
# Para dicho programa cree una clase de pruebas
# utilizando el framework unittest y ejecute las pruebas unitarias correspondientes
def tipo_numero(numero):
    """la funcion tipo_numero admite un numero introducido por
    teclado y evalua si el numero introducido es par o impar
    y
    :param numero:

    :return:
    bool
    resultado del numero cuando es par
    """

    if (numero % 2) == 0:
       print ("El número es par")
    else:
       print ("El número es impar")
def inicio():
    """
    la funcion inicio imprime
    un mensaje de bienvenido y
    un mensaje sobre lo que realizara el programa

    """
    print('BIENVENIDO...')

    print('introduce un numero para verificar si es par o impar')

if __name__=="__main__":

    reinicio=True

    while reinicio:
        print('\n\n')
        inicio()
        try:

            numero=int(input('Aqui tu numero: \n'))
            reinicio=False
            tipo_numero(numero)
        except ValueError:

            print('ERROR...esto no es un numero, introduce un numero valido')
        except:
            print('error..')
