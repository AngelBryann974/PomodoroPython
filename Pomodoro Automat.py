# Pomodoro

#! python3

import winsound
import time

tiempo = 5*60
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

def main():

    print('''


                            Bienvenido a Pomodoro Terminal by @notalion

    Este es un programa que te ayuda a estudiar, 
    La Técnica Pomodoro es un método de gestión del tiempo que puede ayudar a que tu productividad sea mayor

    Se iniciara el conteo a 5 minutos

    ''')
    Conteo(tiempo)
    TiempoFuera()

main()