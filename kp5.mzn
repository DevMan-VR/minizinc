% Use this editor as a MiniZinc scratch book
% Use this editor as a MiniZinc scratch book
array[1..numVaribles] of var 0..1: x; 
array[1..numVaribles] of int: profit;
array[1..numVaribles] of int: weight;
int: capacity;
int: numVaribles; 

var int : z = sum ( [x[j] * profit[j] | j in 1..numVaribles] );
solve maximize z;

constraint 
forall(j in 1..numVaribles)(
  sum(j in 1..numVaribles)(weight[j] * x[j]) <= capacity
);

numVaribles = 8;
capacity = 900;
weight = array1d (1..numVaribles,[350, 400, 450, 20, 70, 8, 5, 5]);
profit = array1d (1..numVaribles,[25, 35, 45, 5, 25, 3, 2, 2]);

output ["x = " ++show(x)++ ", z = " ++show(z)++ "\n"];