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

numVaribles = 6;
capacity = 150;
weight = array1d (1..numVaribles,[50, 50, 64, 46, 50, 5]);
profit = array1d (1..numVaribles,[56, 59, 80, 64, 75, 17]);

output ["x = " ++show(x)++ ", z = " ++show(z)++ "\n"];