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
%7 1735
%442 525 511 593 546 564 617
%41 50 49 59 55 57 60
%172
numVaribles = 7;
capacity = 1735;
weight = array1d (1..numVaribles,[442, 525, 511, 593, 546, 564, 617]);
profit = array1d (1..numVaribles,[41, 50, 49, 59, 55, 57, 60]);

output ["x = " ++show(x)++ ", z = " ++show(z)++ "\n"];