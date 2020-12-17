
# numVariables Capacidad
# [beneficios]
# [pesos]
# Óptimo


class readKP:

  def read_KpProblems():
    problems = dict();
    problems['data'] = []
    problems['capacidad'] = []
    problems['beneficio'] = []
    problems['pesos'] = []
    problems['optimo'] = []
    f = open("./kp_problems.txt", "r")
    lines = f.readlines()
    for line in lines:
      if '#' in line:
        data = lines[lines.index(line)+1].split()
        data = list(map(int, data))
        capacidad = data[1]
        beneficio = lines[lines.index(line)+2].split()
        beneficio = list(map(float, beneficio))
        pesos = lines[lines.index(line)+3].split()
        pesos = list(map(float, pesos))
        optimo = lines[lines.index(line)+4].split()
        optimo = int(optimo[0])
        #print(capacidad, beneficio,pesos, optimo)
        problems['data'].append(data)
        problems['capacidad'].append(capacidad)
        problems['beneficio'].append(beneficio)
        problems['pesos'].append(pesos)
        problems['optimo'].append(optimo)

    f.close()
    return problems

