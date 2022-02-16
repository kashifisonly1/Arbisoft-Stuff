from queue import Queue
from queue import LifoQueue

def BFS(routes, connected, start, not_connected):
    q = Queue()
    q.put(start)
    while not q.empty():
        s = q.get()
        connected[s] = True
        not_connected.remove(s)
        if s in routes:
            for c in routes[s]:
                if not connected[c]:
                    q.put(c)
                    connected[c] = True

def DFS(parent_routes, connected, start, not_connected, child_routes):
    stack = LifoQueue()
    stack.put(start)
    while not stack.empty():
        s = stack.get()
        BFS(child_routes, connected, s, not_connected)
        if s in parent_routes:
            for p in parent_routes[s]:
                if not connected[p]:
                    stack.put(p)
                    break

def solve(airports, routes, start):
    airport_index = {}
    for i in range(len(airports)):
        airport_index[airports[i]] = i
    connected = [False for i in range(len(airports))]
    not_connected = [ i for i in range(len(airports)) ]
    start_index = airport_index[start]

    child_routes = {}
    parent_routes = {}
    for route in routes:
        a1 = airport_index[route[0]]
        a2 = airport_index[route[1]]
        if a1 not in child_routes:
            child_routes[a1] = [a2]
        else:
            child_routes[a1].append(a2)
        if a2 not in parent_routes:
            parent_routes[a2] = [a1]
        else:
            parent_routes[a2].append(a1)
    counter = 0
    BFS(routes, connected, start_index, not_connected)
    while len(not_connected)!=0:
        counter += 1
        DFS(parent_routes, connected, not_connected[0], not_connected, child_routes)
    return counter

x = {
  "airports": ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"],
  "routes": [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"]
  ],
  "startingAirport": "LGA"
}

print(solve(x["airports"], x["routes"], x["startingAirport"]))