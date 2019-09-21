from search import *


class LocationGraph(Graph):
   def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes):
       self.nodes = nodes
       self.locations = locations
       self.edge_list = edges
       self._starting_nodes = starting_nodes
       self.goal_nodes = goal_nodes

   def starting_nodes(self):
       return self._starting_nodes

   def is_goal(self, node):
       return node in self.goal_nodes

   def outgoing_arcs(self, node):
       arcs = []
       for edge in self.edge_list:
           tail, head = edge
           tail_x, tail_y = self.locations[tail]
           head_x, head_y = self.locations[head]
           cost = ((tail_x - head_x) ** 2 + (tail_y - head_y) ** 2) ** 0.5

           if tail == node:
               arcs.append(Arc(tail, head, str(tail) + '->' + str(head), cost))
           elif head == node and (head, tail) not in self.edge_list:
               arcs.append(Arc(head, tail, str(head) + '->' + str(tail), cost))
       return sorted(arcs, key=lambda x : x[1])
