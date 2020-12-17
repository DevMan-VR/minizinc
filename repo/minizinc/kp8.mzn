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

numVaribles = 24;
capacity = 6404180;
weight = array1d (1..numVaribles,[382745, 799601, 909247, 729069, 467902, 44328, 34610, 698150, 823460, 903959, 853665, 551830, 610856, 670702, 488960, 951111, 323046, 446298, 931161, 31385, 496951, 264724, 224916, 169684]);
profit = array1d (1..numVaribles,[825594, 1677009, 1676628, 1523970, 943972, 97426, 69666, 1296457, 1679693, 1902996, 1844992, 1049289, 1252836, 1319836, 953277, 2067538, 675367, 853655, 1826027, 65731, 901489, 577243, 466257, 369261]);

output ["x = " ++show(x)++ ", z = " ++show(z)++ "\n"];