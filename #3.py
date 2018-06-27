
def longitud (pulgadas):
       Yarda=0
        Pies =0
      While pulgadas>=36:
              Yarda+1
               Pulgadas -=36
       While pulgadas>=12:
               Pies+=1
               Pulgadas-=12
Print("las yardas que tienes son:%d"%yarda)
Print("los pies que tienes son:%d"%pies)
Print("las pulgadas que tienes son:%d"%pulgadas)