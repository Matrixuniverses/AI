% second/2 for q1 %
second([_|[A|_]], X) :- A = X.

% swap/2 for q2 %
swap12([F1|[S1|T1]], [F2|[S2|T2]]) :- T1 = T2, F1 = S2, F2 = S1.

% listtran/2 for q3 %
listtran([], []).
listtran([H1| T1], [H2|T2]) :- listtran(T1, T2), tran(H1, H2); listtran(T1, T2), tran(H2, H1).

% twice/2 for q4 %
twice([], []).
twice([H|T1], [F|[S|T2]]) :- H = F, H = S, twice(T1, T2).

% remove/3 for q5 %
remove(_, [], []).
remove(X, [H|T], L) :- X = H, remove(X, T, L); remove(X, T, R), append([H], R, L).

% swap_ends/2 for q6 %
swap_ends([H1|T1], [H2|T2]) :- reverse(T1, [L1|R1]), reverse(T2, [L2|R2]), H1 = L2, L1 = H2, R1 = R2.

% split_odd_even/3 and recursive helper predicates for q7 %
even_number([], [], []).
even_number([H|T], O, [H|E]) :- odd_number(T, O, E).

odd_number([], [], []).
odd_number([H|T], [H|O], E) :- even_number(T, O, E).

split_odd_even(L, O, E) :- odd_number(L, O, E).

% preorder/2 for q8 %
preorder(leaf(L), V) :- append([L],[], V).
preorder(tree(ROOT, LEFT, RIGHT), V) :- append([ROOT], LEVEL, V), 
    append(L1, L2, LEVEL),
    preorder(LEFT, L1),
    preorder(RIGHT, L2).
