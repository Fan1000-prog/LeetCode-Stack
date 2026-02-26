class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        myMap = {}

        for i in arr: 
            if i in myMap:
                myMap[i] = myMap[i] + 1
            else:
                myMap[i] = 1

        count = myMap.values()

        return len(count) == len(set(count))

        