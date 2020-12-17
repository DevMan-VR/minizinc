% Use this editor as a MiniZinc scratch book
% Use this editor as a MiniZinc scratch book
array[1..numVariables] of var 0..1: x; 
array[1..numVariables] of int: profit;
array[1..numMochilas,1..numVariables ] of int: weight;
array[1..numMochilas] of int: capacities;
int: numVariables;
int: numMochilas;

var int : z = sum ( [x[j] * profit[j] | j in 1..numVariables] );
solve maximize z;

constraint 
forall(k in 1..numMochilas)(
  forall(j in 1..numVariables)(
    sum(j in 1..numVariables)(weight[k,j] * x[j]) <= capacities[k]
  )
  
);
numMochilas = 10;
numVariables = 6;
capacities = array1d(1..numMochilas, [80, 96, 20, 36, 44, 48, 10, 18, 22, 24]);
weight = array2d (1..numMochilas, 1..numVariables, [8, 12, 13, 64 , 22, 41,  8, 12, 13, 75 , 22, 41, 3, 6, 4, 18, 6, 4, 5, 10, 8, 32, 6, 12, 5, 13, 8, 42, 6, 20, 5, 13, 8, 48, 6, 20, 0, 0, 0, 0, 8, 0, 3, 0, 4, 0, 8, 0,3, 2,4, 0,8, 4, 3, 2, 4, 8, 8, 4 ]);
profit = array1d (1..numVariables,[100,600, 1200, 2400, 500, 2000]);

output ["x = " ++show(x)++ ", z = " ++show(z)++ "\n"];