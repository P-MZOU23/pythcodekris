import math
from operator import itemgetter
def dijkstra(graph, start):
    #intitialize tentative and confirmed dictionaries
    tentative = {}
    confirmed = {}

    #add start_node and cost to confirmed dictionary
    confirmed[start] = 0
    #place the start node's neighbors in the tentative dictionary
    for node, distance in graph[start].items():
        tentative[node] = distance
    #set next to the node last added to confirmed
    next = start
        #(next is the node that is getting path comparisions away from it next)
    #while the tentative dictionary still has nodes
    while tentative:
        shortest_distance = math.inf
        #select node from tentative dictionary with the lowest cost
        for node, distance in tentative.items():
            #determine the shortest distaqnce node
            if distance < shortest_distance:
                shortest_distance = distance
                next = node
        
        #add lowest cost node to confirmed dict and update next
        confirmed[next] = shortest_distance
        #remove next node from tentative dict
        tentative.pop(next)
        #if not already there, place next node's neighbors on tentative
        for node, distance in graph[next].items():
            cost = confirmed[next] + distance
            #if node in tentative, update cost if necessary
            #if neighbor is in confirmed, then ignore
            if node in confirmed:
                continue
            #here we undate the cost to get to a spot like b that has multiple paths
            elif (node in tentative) and (cost < tentative[node]):
                tentative[node] = cost
            elif node not in tentative:
                tentative[node] = cost

    return confirmed

def main():
   

    graph = {
        'A':{'B':5, 'C':10},
        'B':{'A':5, 'C':3, 'D':11},
        'C':{'A':10, 'B':3, 'D':2},
        'D':{'B':11, 'C':2}
    }
    #choose start node
    start_node = 'D'

    distances = dijkstra(graph, start_node)

    for node, distance in distances.items():
        print(f"{node} -> {distance}")
main()


"""A = {'B':5, 'C':10}
    #print the cost to B from A
    #'key': definition
    print(A['B'])

    for node, cost in A.items():
        print(f"{node} -> {cost}")
"""