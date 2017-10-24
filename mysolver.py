###################################################
# Projeto 1 AI 2017/2018                          #
# IST                                             #
# PEDRO SILVA                                     #
# ANDRE BAIAO                                     #
###################################################
from myclass import *
from myread import *
import itertools


def payload(vert):
    soma = 0
    for k in vert:
        soma += k[1]#soma a massa de cada vertice
    return soma

def comb(members, rule):
    valid = []
    for i in range(0,len(members)+1):
        for subset in itertools.combinations(members, i):
            if (payload(subset) <= rule) :
                valid.append(subset)


def solver(problem):
    solution = []
    pairs = []
    
    for vert in problem.vertices:
        solution.append(vert[0])

    for aux in problem.edges:
        pairs.append(aux)

    
def dfs(graph, start, goal):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)

            if node == goal:
                return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
