# Problem 1 : Critical Connections in a Network
# Time Complexity : O(V+E) where V is number of nodes(servers) and E is the number of connectiosns between nodes
# Space Complexity : O(V+E) where V is number of nodes(servers) and E is the number of connectiosns between nodes
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
from typing import List
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # define the hashMap which will be adjacent list. Keys will be nodes and values will be the list of the connected nodes
        self.hashMap = defaultdict(list)
        # define result list that will store the connections
        self.result =[]
        # define the discoveried array with the length of n and fill with -1
        # this will store the natural order of the node in dfs
        self.discoveried = [-1] * (n)
        # define the lowest array with the length of n and filled with -1
        # this will store the lowest discovery time
        self.lowest = [-1] * (n)
        # define the global time variable and set to 0
        self.time = 0
        # call the buildGraph with the connections
        self.buildGraph(connections)
        # call the dfs function with current node 0 and parent node as 0
        self.dfs(0, 0)
        # return result list
        return self.result
    
    # buildGraph function which create the hashMap adjacent list.
    def buildGraph(self, connections: List[List[int]]) -> None:
        # loop through connections list
        for edge in connections:
            # get the both in and out node from the edge
            inNode, outNode = edge
            # add the out node as value to in node key
            self.hashMap[inNode].append(outNode)
            # add the in node as value to out node key
            self.hashMap[outNode].append(inNode)
    
    # dfs function. this is forward looking dfs algortihm
    def dfs(self, v: int, u: int) -> None:
        # check the value of discoveried array at vth index.
        if self.discoveried[v] != -1:
            # if it is the value is not -1 then return
            return
        # set the discoveried array at vth position yto time
        self.discoveried[v] = self.time
        # set the lowest array at vth position to time
        self.lowest[v] = self.time
        # increment the time variable
        self.time += 1

        # loop through neighbour list for the vrh node
        for ne in self.hashMap[v]:
            # check if the neighbour node is equal to parent node u
            if ne == u:
                # if it is then continue
                continue
            # call dfs with current node as neighbour and parent node as v
            self.dfs(ne, v)
            # check if the value of lowest array at neighbour(next node) postion is greater than the value of discoveried array at vth(current node) position
            if self.lowest[ne] > self.discoveried[v]:
                # if it is then add the neighbour and v node in the result
                self.result.append([ne, v])
            # set the value of the lowest array at vth position as minimum between lowest value at vth position and neth position
            self.lowest[v] = min(self.lowest[v], self.lowest[ne])
