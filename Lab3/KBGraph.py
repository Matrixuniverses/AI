from search import *
from ForwardDeduce import clauses

class KBGraph(Graph):
    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query

    def starting_nodes(self):
        return list(self.query) 
        
    def is_goal(self, node):
        return True if node == [] else False

    def outgoing_arcs(self, tail_node):
        arcs = []
        tail = list(tail_node)

        for clause in self.clauses:
            if clause[0] == tail[0]:
                head = tail[1:] if len(tail) > 1 else []
                
                for body in clause[1]:
                    head.insert(0, body)

                arcs.append(Arc(tail, head, str(tail) + '->' + str(head), 1))

        return arcs
