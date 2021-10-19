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
    """
    Notes about the problem object we're provided:
      1. problem.getStartState() - returns the starting coordinates of Pacman - need to search from here
      2. problem.isGoalState(problem.getStartState()) - Are the given coordinates the goal?
      3. problem.getSuccessors(state) - returns a tuple of the available positions you can get to
        (a) problem.getSuccessors(state)[0]: (x,y) - successor to the current state
        (b) problem.getSuccessors(state)[1]: 'action' - the action req'd to get to the successor state
        (c) problem.getSuccessors(state)[2]: 'cost' - the incremental cost of reaching the successor state
    """
    from util import Stack # Using a Stack to implement iterative DFS
    s = problem.getStartState() 
    visited = {s: False}
    path = {s: []}
    
    # Initialize DFS and begin
    S = Stack()
    S.push(s)
    visited[s] = True
    end_state = s

    while not S.isEmpty():
        v = S.pop()
        if problem.isGoalState(v):
            end_state = v
            break

        for neighbor in problem.getSuccessors(v):
            u = neighbor[0]
            dir = neighbor[1]
            cost = neighbor[2]
            if u not in visited or not visited[u]:
                visited[u] = True
                S.push(u)
                path[u] = path[v][:]
                path[u].append(dir)
                
    return path[end_state]

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Very similar to DFS but uses a queue instead to ensure we traverse layer by layer
    from util import Queue # Queues are typically used to perfrom BFS
    s = problem.getStartState() 
    visited = {s: False}
    path = {s: []}
    
    # Initialize BFS and begin
    Q = Queue()
    Q.push(s)
    visited[s] = True
    end_state = s

    while not Q.isEmpty():
        v = Q.pop()
        if problem.isGoalState(v):
            end_state = v
            break

        for neighbor in problem.getSuccessors(v):
            u = neighbor[0]
            dir = neighbor[1]
            cost = neighbor[2]
            if u not in visited or not visited[u]:
                visited[u] = True
                Q.push(u)
                path[u] = path[v][:]
                path[u].append(dir)
                
    return path[end_state]

    
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Here we use a priority queue, by prioritizing searching in nodes that have the lowest total cost path
    from util import PriorityQueue
    s = problem.getStartState() 
    visited = {s: False}
    actions = []

    # Define the frontier and instantiate it
    frontier = PriorityQueue()
    # We'll push tuples of (state, actions) onto the PQ, where the actions associated with state s have the lowest cost
    frontier.push((s, actions), 0) # Note that the start state should alwasy have the lowest priority

    while not frontier.isEmpty():
        node,actions = frontier.pop()
        if problem.isGoalState(node):
            return actions
        if node not in visited or not visited[node]:
            visited[node] = True
            for neighbor in problem.getSuccessors(node):
                neighbor_node = neighbor[0]
                dir = neighbor[1]
                cost = neighbor[2]
                if neighbor_node not in visited or not visited[neighbor_node]:
                    # Add the cost to reach the neighbor_node to the PQ
                    directions = actions[:]
                    directions.append(dir)
                    frontier.push((neighbor_node, directions), problem.getCostOfActions(directions))

    # If we get here something went wrong
    raise Exception("Something went wrong - we did not find a suitable set of actions to reach the goal state")

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    """
        The A* algorithm picks each step according to the function f = g + h
            g: the movement cost to get from the starting point to a given square, following the path used to get there
            h: the estimated movement cost to move from the given square to the final destination, referred to as a "heuristic" (smart guess) 
    """
    from util import PriorityQueue
    s = problem.getStartState() 
    h = heuristic(s, problem)
    g = 0
    f = g + h
    visited = {s: False}
    actions = []

    # Note that we call the heuristic by passing heuristic(state, problem object) - returns the "cost" between the current state, and the problem objects "goal"
    frontier = PriorityQueue()
    frontier.push((s, actions), f)

    while not frontier.isEmpty():
        node,actions = frontier.pop()
        if problem.isGoalState(node):
            return actions
        if node not in visited or not visited[node]:
            visited[node] = True
            for neighbor in problem.getSuccessors(node):
                neighbor_node = neighbor[0]
                dir = neighbor[1]
                cost = neighbor[2]
                h = heuristic(neighbor_node, problem)
                if neighbor_node not in visited or not visited[neighbor_node]:
                    directions = actions[:]
                    directions.append(dir)
                    g = problem.getCostOfActions(directions)
                    f = g + h
                    frontier.push((neighbor_node, directions), f)

    # If we get here something went wrong
    raise Exception("Something went wrong - we did not find a suitable set of actions to reach the goal state")


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
