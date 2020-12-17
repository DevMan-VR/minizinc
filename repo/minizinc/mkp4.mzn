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
numVariables = 20;
numMochilas = 10;
capacities = array1d(1..numMochilas, [550, 700, 130, 240, 280, 310, 110, 205, 260, 275]);
weight = array2d (1..numMochilas, 1..numVariables, [8, 24, 13, 80, 70, 80, 45, 15, 28, 90, 130, 32, 20, 120, 40, 30, 20, 6, 3, 180, 8, 44, 13, 100, 100, 90, 75, 25, 28, 120, 130, 32, 40, 160, 40, 60, 55, 10, 6, 240, 3, 6, 4, 20, 20, 30, 8, 3, 12, 14, 40, 6, 3, 20, 5, 0, 5, 3, 0, 20,5, 9, 6, 40, 30, 40, 16, 5, 18, 24, 60, 16, 11, 30, 25, 10, 13, 5, 1, 80,5, 11, 7, 50, 40, 40, 19, 7, 18, 29, 70, 21, 17, 30, 25, 15, 25, 5, 1, 100,5, 11, 7, 55, 40, 40, 21, 9, 18, 29, 70, 21, 17, 35, 25, 20, 25, 5, 2, 110,0, 0, 1, 10, 4, 10, 0, 6, 0, 6, 32, 3, 0, 70, 10, 0, 0, 0, 0, 0,3, 4, 5, 20, 14, 20, 6, 12, 10, 18, 42, 9, 12, 100, 20, 5, 6, 4, 1, 20,3, 6, 9, 30, 29, 20, 12, 12, 10, 30, 42, 18, 18, 110, 20, 15, 18, 7, 2, 40, 3, 8, 9, 35, 29, 20, 16, 15, 10, 30, 42, 20, 18, 120, 20, 20, 22, 7, 3, 50   ]);
profit = array1d (1..numVariables,[100, 220, 90, 400, 300, 400, 205, 120, 160, 580, 400, 140, 100, 1300, 650, 320, 480, 80, 60, 2550]);

output ["x = " ++show(x)++ ", z = " ++show(z)++ "\n"];