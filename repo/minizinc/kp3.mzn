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
%SFS(, , )
numVaribles = 7;
capacity = 107;
weight = array1d (1..numVaribles,[70, 20, 39, 37, 7, 5, 10]);
profit = array1d (1..numVaribles,[31, 10, 20, 19, 4, 3, 6]);

output ["x = " ++show(x)++ ", z = " ++show(z)++ "\n"];