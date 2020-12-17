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

numVaribles = 15;
capacity = 1747;
weight = array1d (1..numVaribles,[135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]);
profit = array1d (1..numVaribles,[70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]);

output ["x = " ++show(x)++ ", z = " ++show(z)++ "\n"];