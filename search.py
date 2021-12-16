# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    "*** YOUR CODE HERE ***"
    import util as U

    visited_nodes = []                                                                          #nodes that have been visited                     
    final_path=[]                                                                               #final path traversed
    leaf = U.Stack()                                                                            #stack that contains nodes to expand                
    curr_path=U.Stack()                                                                         #path from the start to current           
    leaf.push(problem.getStartState())                                                          #starts from start state
    curr_node = leaf.pop()                                                                      #current state = start state
    while not problem.isGoalState(curr_node):
        if curr_node not in visited_nodes:
            visited_nodes.append(curr_node)                                                    #changing current node`s state to visited
            succ_nodes = problem.getSuccessors(curr_node)                                      #gets successor nodes of current node
            for child_node,dir,cost in succ_nodes:
                leaf.push(child_node)                                                           #adding child node to the stack
                tempPath = final_path + [dir]                                                   
                curr_path.push(tempPath)                                                        #updating current path
        final_path = curr_path.pop()                                                            #updating final path
        curr_node = leaf.pop()                                                                 #updating state of the current node
    return final_path
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    import util as u

    visited_nodes = []                                                                          #nodes that have been visited                            
    int_path=[]                                                                                 #path of intermediate nodes                             
    final_path=[]                                                                               #final path traversed  
    leaf = u.Queue()                                                                            #queue that contains nodes to expand                        
    curr_node_path=u.Queue()                                                                    #path from the start to current                   
    leaf.push(problem.getStartState())                                                          #starts from start state
    curr_node = leaf.pop()                                                                     #current state = start state
    while not problem.isGoalState(curr_node):
        if curr_node not in visited_nodes:
            visited_nodes.append(curr_node)                                                    #changing current node`s state to visited    
            succ_nodes = problem.getSuccessors(curr_node)                                      #gets successor nodes of current node
            for child_node,dir,cost in succ_nodes:
                leaf.push(child_node)                                                           #adding child node to the queue
                int_path = final_path + [dir]                                                   #keeping track of intermediate path
                curr_node_path.push(int_path)                                                   #updating current path
        final_path = curr_node_path.pop()                                                       #updating final path
        curr_node = leaf.pop()                                                                 #updating state of the current node
        
    return final_path
    
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "* YOUR CODE HERE *"
    """Search the node of least total cost first."""
    "* YOUR CODE HERE *"
    import util as u
    visited_nodes = []                                                                          #nodes that have been visited                               
    int_path=[]                                                                                 #path of intermediate nodes                               
    final_path=[]                                                                               #path of final nodes                                    
    leaf = u.PriorityQueue()                                                                    #has states and priority of node                  
    currentnode_path=u.PriorityQueue()                                                          #current node`s path and cost             
    leaf.push(problem.getStartState(),0)                                                        #pushing start node 
    curr_node = leaf.pop() 
    while not problem.isGoalState(curr_node):
        if curr_node not in visited_nodes:
            visited_nodes.append(curr_node)                                                  #changing current node state to visisted
            succ_nodes = problem.getSuccessors(curr_node)                                    #gets all successors of current node
            for child_node,dir,cost in succ_nodes:
                int_path = final_path + [dir]                                                   #keeping track of intermediate path
                trav_cost = problem.getCostOfActions(int_path)                                  #cost = cost(node) + heuristic(node)
                if child_node not in visited_nodes:
                    leaf.push(child_node,trav_cost)                                             #adding a node and its cost, if it is unvisited
                    currentnode_path.push(int_path,trav_cost)                                   #updating the current path
        final_path = currentnode_path.pop()                                                     #updating the final path 
        curr_node = leaf.pop()                                                               #updating the state of current node
    return final_path

    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "* YOUR CODE HERE *"
    import util as u
    visited_nodes = []                                                                          #nodes that have been visited                               
    int_path=[]                                                                                 #path of intermediate nodes                               
    final_path=[]                                                                               #path of final nodes                                    
    leaf = u.PriorityQueue()                                                                    #has states and priority of node                  
    currentnode_path=u.PriorityQueue()                                                          #current node`s path and cost             
    leaf.push(problem.getStartState(),0)                                                        #pushing start node 
    curr_node = leaf.pop() 
    while not problem.isGoalState(curr_node):
        if curr_node not in visited_nodes:
            visited_nodes.append(curr_node)                                                  #changing current node state to visisted
            succ_nodes = problem.getSuccessors(curr_node)                                    #gets all successors of current node
            for child_node,dir,cost in succ_nodes:
                int_path = final_path + [dir]                                                   #keeping track of intermediate path
                trav_cost = problem.getCostOfActions(int_path) + heuristic(child_node,problem)  #cost = cost(node) + heuristic(node)
                if child_node not in visited_nodes:
                    leaf.push(child_node,trav_cost)                                             #adding a node and its cost, if it is unvisited
                    currentnode_path.push(int_path,trav_cost)                                   #updating the current path
        final_path = currentnode_path.pop()                                                     #updating the final path 
        curr_node = leaf.pop()                                                               #updating the state of current node
    return final_path

    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch