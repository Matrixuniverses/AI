from search import *
from heapq import *
import math

class RoutingGraph(Graph):
    """
    Subclass of graph which takes a string of a map and coverts it into a graph object then finds
    outgoing arcs for each of the possible moves in the given cardinal directions 
    """

    def __init__(self, map_str):
        """
        Initialises the routing graph and populates the start nodes and goal nodes
        """

        self.map_str = map_str

        # Population of the graph representation of the map
        self.graph = [list(item) for item in self.map_str.strip().split("\n")]
        self.start = []
        self.goal_nodes = []

        # Define what items invalidate a path in a given direction
        self.blocks = ['+', '|', '-', 'X']
            
        # Performs 2D matrix iteration to find the parts of the graph relevant ie. matching (S, F, [0-9]+)        
        for row_index in range(len(self.graph)):
            for col_index in range(len(self.graph[row_index])):
                node = self.graph[row_index][col_index]

                if node == 'S': 
                    self.start.append((row_index, col_index, math.inf))
                elif node.isdigit(): 
                    self.start.append((row_index, col_index, int(node)))
                elif node == 'G': self.goal_nodes.append((row_index, col_index))
    
    def starting_nodes(self):
        """
        OVERRIDE: implements the starting_nodes method by returning a generator expression for all 
        the iems in the starting nodes
        """
        return (node for node in self.start)

    def outgoing_arcs(self, tail_node):
        """
        OVERRIDE: Implements the outgoing_arcs method by generating possible directions that can be 
        taken from the given node as an Arc type
        """
       
        # Path direction definition which defines index updates for the caridnal directions
        # Form (DIR, update ROW INDEX, update COL INDEX)
        directions = [('N' , -1, 0),
                 ('E' ,  0, 1),
                 ('S' ,  1, 0),
                 ('W' ,  0, -1),] #<-- it seems this list is incomplete


        for direction in directions:
            row_index, col_index, fuel = tail_node[0] + direction[1], tail_node[1] + direction[2], tail_node[2]
            
            # Checks to see if the directional move is valid, then reduces fuel accordingly
            if self.graph[row_index][col_index] not in self.blocks and fuel > 0:
                head_node = (row_index, col_index, fuel - 1)
                yield Arc(tail_node, head_node, direction[0], 5)

        if self.graph[tail_node[0]][tail_node[1]] == 'F' and fuel < 9:
            head_node = (tail_node[0], tail_node[1], 9)
            yield Arc(tail_node, head_node, "Fuel up", 15)

    def estimated_cost_to_goal(self, node):
        """
        OVERRIDE: Implements the estimtaed_cost_to_goal method using the manhattan distance
        """
        return min([(abs(goal[0] - node[0]) + abs(goal[1] - node[1])) * 5 for goal in self.goal_nodes])


    def is_goal(self, node):
        return (node[0], node[1]) in self.goal_nodes

class AStarFrontier(Frontier):
    """
    Subclass of the Frontier class that implements an AStar searching alogirthm, including heuristic calculation
    """

    def __init__(self, graph):
        self.graph = graph
        self.queue = []
        self.container = set()
        self.counter = 1

    def add(self, path):
        """
        OVERRIDE: Implements the add method by checking to ensure that the new head is not already in
        the frontier. The costs of all the edges in the path is calculated and the heuristic added
        """
        arc = path[-1]
        if arc.head not in self.container:
            edge_costs = sum([edge.cost for edge in path])

            heappush(self.queue, (self.graph.estimated_cost_to_goal(arc.head) + edge_costs, self.counter, path))
            self.counter += 1
    
    def __next__(self):
        """
        OVERRIDE: Implements the next function by creating an iterator
        """
        while self.queue:
            path = heappop(self.queue)[2]
            arc = path[-1]

            if arc.head not in self.container:
                self.container.add(arc.head)
                return path
        raise StopIteration

def print_map(map_graph, frontier, solution):
    """
    Prints a graphical version of the map containing the paths taken to get to the solution (if one should
    exist)
    """

    for row_index in range(len(map_graph.graph)):
        for col_index in range(len(map_graph.graph[row_index])):
            is_agent = True if map_graph.graph[row_index][col_index] in ['S', 'G'] else False

            # We can consider the node to contain math.inf fuel as it is a solar agent
            node = (row_index, col_index, math.inf)
                
            # First case is finding a solution inside of the solution path for the given node
            if solution is not None and node in [x.tail for x in solution] and not is_agent: print('*', end='')

            # Second case is finding if the node has been traversed but is not inside of the solution path
            elif node in frontier.container and not is_agent: print('.', end='')

            # Final case is the agents, goal node(s), obstacles and map components
            else: print(map_graph.graph[row_index][col_index], end='')
        print()
