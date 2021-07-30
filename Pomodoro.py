# Pomodoro

#! python3

import winsound
import time

default = 20*60
tiempo = 'undefined'
Flag = False


def TiempoFuera():
    print('''
    
    
          TIEMPO FUERA!!!
                \/ 
               \||/
              °°  °°
             °°    °°
             °°    °°
              °°°°°°
        --------------------
        |                  |
        ''')
    for i in range (0,2):
        winsound.Beep(590,300)
        winsound.Beep(430,300)
        time.sleep(1)
        winsound.Beep(590,300)
        winsound.Beep(430,300)
        winsound.Beep(500,300)
        winsound.Beep(590,390)
        time.sleep(3)
    
def Conteo(tiempo):
    if tiempo == 'undefined':
        tiempo = default
    
    print('''



         EMPIEZA POMODORO
            A TRABAJAR
         
               \||/
              °°°°°°
             °°°°°°°°
             °°°°°°°°
              °°°°°°
        --------------------
        |                  |
    ''')

    while tiempo > 0:
        time.sleep(1)
        tiempo = tiempo - 1
        if tiempo % 60 == 0 and tiempo > 0:
            min = int(tiempo/60)
            print("Quedan " + str(min) + " min")
        elif tiempo % 10 == 0 and tiempo > 0 and tiempo <= 60:
            print("Quedan " + str(tiempo) + " segundos")
        
    TiempoFuera()

def main():
    global tiempo
    global Flag
    
    print('''


                            Bienvenido a Pomodoro Terminal by @notalion

    Este es un programa que te ayuda a estudiar, 
    La Técnica Pomodoro es un método de gestión del tiempo que puede ayudar a que tu productividad sea mayor

    Se iniciara el conteo a 20 minutos, esta de acuerdo? [S/N]

    ''')

    while Flag == False: 

        ans = str.upper(input())
        
        if ans == "S":
            Conteo(tiempo)
            Flag = True

        elif ans == "N":
            print("¿Cuantos minutos desea estudiar?")
            tiempo = int(input()) * 60
            Conteo(tiempo)
            Flag = True

        else:
            print("Porfavor elija una respuesta [S/N]")

main()
