% new_append/3 for q1 - redefinition of the append/3 predicate %
new_append([], L, L).
new_append([H|L1], L2, [H|L3]) :- new_append(L1, L2, L3).

% reversed/2 for q2 - redefinition of the reverse/2 predicate % 
accumulator([], L, L).
accumulator([H|T], L1, L) :- accumulator(T, [H|L1], L).
reversed(A, L) :- accumulator(A, [], L).

% max/2 for q3 - finds the maximum value in a supplied list %
max([], X, X).
max([H|T], N2, M) :- H > N2 -> max(T, H, M); max(T, N2, M). 
max([H|T], N) :- max(T, H, N).

% binary_number/1 for q4 - is true when input list matches regex 0b(0|(1(0|1)*)) %
binary_number([0,b,0]).
binary_number([0,b,1]).
bin([]).
bin([H|T]) :- H = 0, bin(T); H = 1, bin(T).

binary_number([0,b,1|N]) :- bin(N).

% dna/2 for q5 - completes the other half of given dna strands or determines if two halves are correct %
pair(a,X) :- X = t.
pair(t,X) :- X = a.
pair(c,X) :- X = g.
pair(g,X) :- X = c.

dna([], []).
dna([H1|T1], [H2|T2]) :- pair(H1, X),X=H2,dna(T1, T2).

% eats/2 for q6 %
eats(P, F) :- hungry(P), P = alice, edible(F), \+fast_food(F).
eats(P, F) :- hungry(P), P = bob, edible(F).

% postorder/2 for q7 - completes a postorder tree traversal recursively %
postorder(leaf(A), [A]).
postorder(tree(ROOT, LEFT, RIGHT), T) :- append(CHILDREN, [ROOT], T),
    append(L, R, CHILDREN), 
    postorder(LEFT, L),
    postorder(RIGHT, R).

% unique/2 for q8 - finds all unique values of given list. Uses builtin list_to_set function because im lazy %
unique(L, S) :- list_to_set(L, S).

% merge/3 for q9 - zips given lists together %
merge([], X, X).
merge(X, [], X).
merge([H1|T1], [H2|T2], X) :- (H1 > H2 -> merge([H1|T1], T2, L), append([H2], L, X)); 
                            merge([H2|T2], T1, L), append([H1], L, X).

% merge_sort/2 for q10 - performs a merge sort on the given lists recursively %
even_number([], [], []).
even_number([H|T], O, [H|E]) :- odd_number(T, O, E).

odd_number([], [], []).
odd_number([H|T], [H|O], E) :- even_number(T, O, E).

split_odd_even(L, O, E) :- odd_number(L, O, E).

merge_sort([], []).
merge_sort([X], [X]).
merge_sort(L1, L0) :- split_odd_even(L1, O, E), merge_sort(O, OUT), merge_sort(E, OUT2), merge(OUT, OUT2, L0).

% cartesian_product/3 for q11 - creates a cartesian product from the given lists recursively
pair(_, [], []).
pair(ELEMENT, [H|T], [(ELEMENT, H)|R]) :- pair(ELEMENT, T, R).

cartesian_product([], _, []).
cartesian_product([H|T], L, X) :- cartesian_product(T, L, I), pair(H, L, P), append(P, I, X).
