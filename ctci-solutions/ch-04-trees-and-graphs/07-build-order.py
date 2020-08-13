# Build Order: You are given a list of projects and a list of dependencies 
# (which is a list of pairs of projects, where the second project is dependent 
# on the first project). All of a project's dependencies must be built before 
# the project is. Find a build order that will allow the projects to be built. 
# If there is no valid build order, return an error.
# EXAMPLE
# Input:
# Projects: a, b, c, d, e, f
# Dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c
# Hints: #26, #47, #60, #85, #725, #133


"""
Idea is to create a graph, remove nodes from the graph iteratively once
they have no incoming edges, then remove their outgoing edges. If we are
left with only nodes with incoming edges, there is no solution
"""

# TODO: Complete this

class Graph:
    def __init__(self):
        pass

class Project:
    def __init__(self):
        pass

def find_build_order(projects, dependencies):
    graph = build_graph(projects, dependencies)
    return order_projects(graph.get_nodes())

def build_graph(projects, dependencies):
    pass

def order_projects(projects):
    pass
