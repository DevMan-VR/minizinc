% Use this editor as a MiniZinc scratch book
% Use this editor as a MiniZinc scratch book
array[1..numVariables] of var 0..1: x; 
array[1..numVariables] of float: profit;
array[1..numMochilas,1..numVariables ] of int: weight;
array[1..numMochilas] of int: capacities;
int: numVariables;
int: numMochilas;

var float : z = sum ( [x[j] * profit[j] | j in 1..numVariables] );
solve maximize z;

constraint 
forall(k in 1..numMochilas)(
  forall(j in 1..numVariables)(
    sum(l in 1..numVariables)(weight[k,j] * x[j]) <= capacities[k]
  )
  
);
numVariables = 10;
numMochilas = 10;
capacities = array1d(1..numMochilas, [450, 540, 200, 360, 440, 480, 200, 360, 440, 480]);
weight = array2d (1..numMochilas, 1..numVariables, [20, 5, 100, 200, 2, 4, 60, 150, 80, 40, 20, 7, 130, 280, 2, 8, 110, 210, 100, 40, 60, 3, 50, 100, 4, 2, 20, 40, 6, 12, 60, 8, 70, 200, 4, 6, 40, 70, 16, 20, 60, 13, 70, 250, 4, 10, 60, 90, 20, 24, 60, 13, 70, 280, 4,10, 70, 105, 22, 28, 5, 2, 20, 100, 2, 5, 10, 60, 0, 0, 45, 14, 80, 180, 6, 10, 40, 100, 20, 0, 55, 14, 80, 200, 6, 10, 50, 140, 30, 40, 65, 14, 80, 220, 6, 10, 50, 180, 30, 50]);
profit = array1d (1..numVariables,[600.1, 310.5, 1800, 3850, 18.6, 198.7, 882, 4200, 402.5, 327]);

output ["x = " ++show(x)++ ", z = " ++show(z)++ "\n"];