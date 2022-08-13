class Solution:
    def maxArea(self, height: List[int]) -> int:
#         #Get the keys for the dicctionary used
#         n = list(range(len(height)))
        
#         #Build the dict
#         d = dict(zip(n,height))
        
#         #Get the level in which you would start iterations, which is the second highest point
#         max_lvl = sorted(height)[-2]
        
#         #Declare the variable to store the highest volume
#         max_vol = 0 
        
#         #Iterate from the second highest point, since volume need two endpoints. And obtaining the highest volume every level
        
#         while max_lvl > 0:
#             #Using a dict comprenhension obtain the keys for highest endpoints levels
#             x = list({k for k, v in d.items() if v >= max_lvl})
            
#             #Store the volume if it is higher to the past volume
#             if (max_vol) < ((max(x)-min(x))*max_lvl):
#                 max_vol = ((max(x)-min(x))*max_lvl)
            
#             #Lower the volume
#             max_lvl -= 1
        
#         return max_vol
        maxvol = 0
        i,j = 0, len(height)-1

        while i < j:
            if maxvol < ((j - i)*(min(height[i],height[j]))):
                maxvol = ((j - i)*(min(height[i],height[j])))
            if height[i] <= height[j]:
                i +=1
            else:
                j -= 1
        return maxvol