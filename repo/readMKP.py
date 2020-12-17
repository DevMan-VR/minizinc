
class readMKP:

  def read_MkpProblems():
    problems = dict();
    problems['data'] = []
    problems['capacidad'] = []
    problems['beneficio'] = []
    problems['pesos'] = []
    problems['optimo'] = []
    f = open("./mkp_problems.txt", "r")
    lines = f.readlines()
    for line in lines:
      if '#' in line:
        data = lines[lines.index(line)+1].split()
        data = list(map(int, data))
        nmochilas = data[1]
        capacidad = lines[lines.index(line)+2].split()
        capacidad = list(map(float, capacidad))
        beneficio = lines[lines.index(line)+3].split()
        beneficio = list(map(float, beneficio))
        optimo = float(lines[lines.index(line)+4+nmochilas])
        pesos = []
        #print(data)
        problems['data'].append(data)
        #print(capacidad)
        problems['capacidad'].append(capacidad) 
        #print(beneficio)
        problems['beneficio'].append(beneficio)
        for knapsack in range(lines.index(line)+4,lines.index(line)+4+nmochilas):
          mochila_pesos = lines[knapsack].split()
          mochila_pesos = list(map(float, mochila_pesos))
          pesos.append(mochila_pesos)
        #print(pesos)
        problems['pesos'].append(pesos)
        #print(optimo)
        problems['optimo'].append(optimo)

    f.close()
    return problems
