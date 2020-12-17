from SFS import SFS
import time
from readMKP import readMKP
from readKP import readKP

# SFS(Pesos Max, Pesos, Beneficios, tipo problema (KP por defecto))
# Instancias KP
#kpproblem1 = SFS(51, [24, 13, 23, 15, 16], [12, 7, 11, 8, 9])
#kpproblem2 = SFS(150, [50, 50, 64, 46, 50, 5], [56, 59, 80, 64, 75, 17])
#kpproblem3 = SFS(107, [70, 20, 39, 37, 7, 5, 10], [31, 10, 20, 19, 4, 3, 6])
#kpproblem4 = SFS( 107, [70, 20, 39, 37, 7, 5, 10], [31, 10, 20, 19, 4, 3, 6] )
#kpproblem5 = SFS(900, [350, 400, 450, 20, 70, 8, 5, 5] , [25, 35, 45, 5, 25, 3, 2, 2])
#kpproblem6 = SFS(309, [92, 57, 49, 68, 60, 43, 67, 84, 87, 72], [23, 31, 29, 44, 53, 38, 63, 85, 89, 82] )
#kpproblem7 = SFS(1747, [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240], [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120])
#kpproblem8 = SFS(6404180, [382745, 799601, 909247, 729069, 467902, 44328, 34610, 698150, 823460, 903959, 853665, 551830, 610856, 670702, 488960, 951111, 323046, 446298, 931161, 31385, 496951, 264724, 224916, 169684], [825594, 1677009, 1676628, 1523970, 943972, 97426, 69666, 1296457, 1679693, 1902996, 1844992, 1049289, 1252836, 1319836, 953277, 2067538, 675367, 853655, 1826027, 65731, 901489, 577243, 466257, 369261])


# cycle(Generaciones, Numero de Hijos, Tamaño poblacion (opcional, 5 por defecto) )

def KpProblem(instancia, comentario, optimo, printer):
  if(printer):
    print(comentario)
  gain = instancia.cycle(5,3,printer)
  if(printer):
    print("Beneficio deseado:", optimo, "\n")
  return gain

#start_time = time.time()
#KpProblem(kpproblem1, "PROBLEMA KP - 1", 26,1)
#KpProblem(kpproblem2, "PROBLEMA KP - 2", 198,1)
#KpProblem(kpproblem3, "PROBLEMA KP - 3", 55,1)
#KpProblem(kpproblem4, "PROBLEMA KP - 4", 55,1)
#KpProblem(kpproblem5, "PROBLEMA KP - 5", 104,1)
#KpProblem(kpproblem6, "PROBLEMA KP - 6", 309,1)
#KpProblem(kpproblem7, "PROBLEMA KP - 7", 916,1)
#KpProblem(kpproblem8, "PROBLEMA KP - 8", 13549094,1)
#print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
problems_data = readKP.read_KpProblems()
for element in range(len(problems_data['data'])):
  kpProblem = SFS(problems_data['capacidad'][element],problems_data['pesos'][element],problems_data['beneficio'][element]) 
  f = open("PROBLEMA KP - " + str(element+1) + ".csv","w+")
  #f.write("instancia,fitness\n")
  for i in range(30):
    f.write(str(KpProblem(kpProblem,f'PROBLEMA KP - {element+1}',problems_data['optimo'][element],1)) + "\n")
    #f.write(str(i) + "," + str(KpProblem(kpProblem,f'PROBLEMA KP - {element+1}',problems_data['optimo'][element],1)) + "\n")
  f.close()
print("--- %s seconds ---" % (time.time() - start_time))
print("\n\n")



start_time = time.time()
problems_data = readMKP.read_MkpProblems()
for element in range(len(problems_data['data'])):
  mkpProblem = SFS(problems_data['capacidad'][element],problems_data['pesos'][element],problems_data['beneficio'][element],"MKP")
  f = open("PROBLEMA MKP - " + str(element+1) + ".csv","w+")
  for i in range(30):

    optimo = mkpProblem.cycle(5,3,1)
    f.write(str(optimo) + "\n")
    #f.write(str(i) + "," + str(KpProblem(kpProblem,f'PROBLEMA KP - {element+1}',problems_data['optimo'][element],1)) + "\n")
  f.close()

  print(f'PROBLEMA MKP - {element+1}')
  mkpProblem.cycle(5,3,1)
  print("Beneficio deseado:", problems_data['optimo'][element], "\n")

print("--- %s seconds ---" % (time.time() - start_time))



