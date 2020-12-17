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

numVaribles = 10;
capacity = 309;
weight = array1d (1..numVaribles,[92, 57, 49, 68, 60, 43, 67, 84, 87, 72]);
profit = array1d (1..numVaribles,[23, 31, 29, 44, 53, 38, 63, 85, 89, 82]);

output ["x = " ++show(x)++ ", z = " ++show(z)++ "\n"];