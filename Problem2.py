# Problem 2 : Minimize Malware Spread
# Time Complexity : O(n^3) where n is the number of nodes
# Space Complexity : O(n^2) where n is the number of nodes
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
from typing import List

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        # get the length of the graph
        length = len(graph)
        # colors array to store the color for each node in the graph (information on group to which node belongs)
        # fill the array with -1
        colors = [-1] * (length)
        # color variable for seting the color for the node. Set the initial value to 0
        color = 0

        # dfs function to traver the graph for the neighbouring nodes with index i and color code with color
        def dfs(graph: List[List[int]], colors: List[int], i: int, color: int) -> None:
            # base
            # check if the color of the node is already by checking with the initial value
            if colors[i] != -1:
                # if it is already set then return
                return
            
            # logic
            # set the colors array of the ith node at ith position with color value
            colors[i] = color
            # loop from 0 to column length for the ith node
            for j in range(len(graph)):
                # if the value is 1 ie the ith node and jth node is connected
                if graph[i][j] == 1:
                    # if it is connected then call dfs function for jth node and color value
                    dfs(graph, colors, j, color)

        # Fill the colors array for each node. (Group nodes into particular group for each node)
        # loop from 0 to length
        for i in range(length):
            # check if the color of the ith node in colors array is -1 ie not set then call dfs for that node 
            if colors[i] == -1:
                dfs(graph, colors, i, color)
                # once dfs is completed then increment the color value
                color +=1 
        
        # define group array which will contain infomation of total number of nodes in each group
        # fill the array initially with 0
        groups = [0] * color
        # loop from 0 to length
        for i in range(length):
            # get the color of the ith node from colors array
            cl = colors[i]
            # increment the value of the groups array at cl th index(color)
            groups[cl] += 1

        # define initGroups array which will contain information of total number of infected node for each group
        initGroups = [0] * color
        # loop in the inital array
        for node in initial:
            # get the color of the infected node from colors array
            c = colors[node]
            # increment the value of the initGroups array with cth index(color)
            initGroups[c] += 1
        
        # define result which will store the result node and set to infinity
        result = float('inf')
        # loop through initial array
        for node in initial:
            # get the color of the node
            col = colors[node]
            # get the count of the infected node for the col color group
            cnt = initGroups[col]
            # check if the count of infected node is equal to 1
            if cnt == 1:
                # if result is inifinity ie it is the first node in the array
                if result == float('inf'):
                    # then set the result to node
                    result = node
                # if it is not first node then
                # check if the total number of the nodes in the col group is greater than the total number of nodes in the value 
                # of the color in the colors array with the result node
                elif groups[col] > groups[colors[result]]:
                    # set the result to node
                    result = node
                # if the values of total number of the nodes in the group then check the value of node and result 
                # check if node value is small than result node value
                elif groups[col] == groups[colors[result]] and node < result:
                    # set the result to node
                    result = node
        
        # check if the result to infinity ie there is no node which can be removed then get the minimum from the initial array
        if result == float('inf'):
            result = min(initial)
        # return result
        return result
