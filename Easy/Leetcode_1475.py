class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        #creating a copy of the original array
        result = list(prices)
        n = len(prices)

        for i in range(n):
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    result[i] = prices[i] - prices[j]
                    break
            

        return result