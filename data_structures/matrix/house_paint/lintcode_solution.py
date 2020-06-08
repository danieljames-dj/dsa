import sys

class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        minCosts = []
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        cost1 = 0
        cost2 = 0
        costIndex = -1
        for i in range(n):
            newCost1 = sys.maxsize
            newCost2 = sys.maxsize
            newCost1Index = -1
            for j in range(k):
                newCost = costs[i][j] + (cost1 if costIndex != j else cost2)
                if newCost < newCost2:
                    if newCost < newCost1:
                        newCost2 = newCost1
                        newCost1 = newCost
                        newCost1Index = j
                    else:
                        newCost2 = newCost
            cost1 = newCost1
            cost2 = newCost2
            costIndex = newCost1Index
        return min(cost1, cost2)