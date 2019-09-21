from search import *


class LCFSFrontier():
   def __init__(self):
       self.container = []
   
   def add(self, path):
       self.container.append(path)
   
   def __iter__(self):
       return self
   
   def __next__(self):
       self.sort_container()
       value = self.container.pop(0)
       return value
    
   # This implementation uses a counting sort, however using heapq the implementation can be done so
   # that heapq manages the sort on each iteration
   def sort_container(self):
       cost_list = []
       for path in self.container:
           total = 0
           for arc in path:
               total += arc[3]
           cost_list.append(total)
       self.container = [x for _, x in sorted(zip(cost_list,self.container))]
