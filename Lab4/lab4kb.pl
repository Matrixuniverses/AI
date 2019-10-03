% eats/2 predicate for Q1 %
eats(X, Y) :- likes(X, Y).
eats(X, Y) :- hungry(X), edible(Y).

% reflection/2 predicate for Q2 %
reflection(point(X, Y), point(Y, X)).

% Knowledge required for diagnosis/4 predicate for Q5 %
/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

% diagnosis/4 predicate for Q5 %
diagnosis(hard_lenses, Age, Astigmatic, Tear_Rate) :- young(Age), Astigmatic == yes, normal_tear_rate(Tear_Rate).
diagnosis(soft_lenses, Age, Astigmatic, Tear_Rate) :- young(Age), Astigmatic == no, normal_tear_rate(Tear_Rate).
diagnosis(no_lenses, Age, Astigmatic, Tear_Rate) :- low_tear_rate(Tear_Rate).


% Knowledge required for contains/4 predicate for Q6 %
directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).

% contains/2 predicate for Q6 %
contains(X, Y) :- directlyIn(Y, X); directlyIn(Y, Z), contains(X, Z).

% solution/6 predicate for Q7 %
solution(V1, V2, V3, H1, H2, H3) :- word(V1, _, V1H1, _, V1H2, _, V1H3, _),
    word(V2, _, V2H1, _, V2H2, _, V2H3, _),
    word(V3, _, V3H1, _, V3H2, _, V3H3, _),
    word(H1, _, V1H1, _, V2H1, _, V3H1, _),
    word(H2, _, V1H2, _, V2H2, _, V3H2, _),
    word(H3, _, V1H3, _, V2H3, _, V3H3, _).

% mirror/2 predicate 
mirror(leaf(X), leaf(Y)) :- X = Y.
mirror(tree(X, Y), tree(Z, A)) :- mirror(X, A), mirror(Y, Z).
