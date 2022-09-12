#!/bin/python3
# From: https://www.hackerrank.com/challenges/torque-and-development/problem?isFullScreen=true

from collections import defaultdict, deque

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib
    
    city_nodes = defaultdict(lambda: set())
    for city1, city2 in cities:
        city_nodes[city1].add(city2)
        city_nodes[city2].add(city1)
    
    city_group_qty = 0
    accounted_nodes = 0
    while city_nodes:
        city_group_qty += 1
        curr_city_node = next(iter(city_nodes.items()))
        curr_city_group = find_city_group(curr_city_node, city_nodes)
        accounted_nodes += len(curr_city_group)
        for city in curr_city_group:
            del city_nodes[city]
    
    city_group_qty += (n - accounted_nodes)
    number_of_needed_roads = n - city_group_qty
    number_of_libraries = city_group_qty
    return (number_of_libraries * c_lib) + (number_of_needed_roads * c_road)


def find_city_group(root_node, city_nodes):
    city_group = set()
    nodes_to_visit = deque([root_node])
    while nodes_to_visit:
        curr_node = nodes_to_visit.pop()
        city_group.add(curr_node[0])
        for connected_node in curr_node[1]:
            if connected_node not in city_group:
                nodes_to_visit.appendleft((connected_node, city_nodes[connected_node]))
    
    return city_group
