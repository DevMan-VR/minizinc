% Use this editor as a MiniZinc scratch book
% Use this editor as a MiniZinc scratch book
array[1..numVaribles] of var 0..1: x; 
array[1..numVaribles] of int: profit;
array[1..numVaribles] of int: weight;
int: capacity;
int: numVaribles;
int: nMochilas

var int : z = sum ( [x[j] * profit[j] | j in 1..numVaribles] );
solve maximize z;

constraint 
forall(j in 1..numVaribles)(
  sum(j in 1..numVaribles)(weight[j] * x[j]) <= capacity
);

numVaribles = 5;
capacity = 51;
weight = array1d (1..numVaribles,[24, 13, 23, 15, 16]);
profit = array1d (1..numVaribles,[12, 7, 11, 8, 9]);

output ["x = " ++show(x)++ ", z = " ++show(z)++ "\n"];