#Approach 1: Brute Force
def trap(self, height: List[int]) -> int:
        l=len(height)
        tot=0
        for i in range(l):
            left=height[i]
            for j in range(i):
                left=max(height[j],left)
            right=height[i]
            for j in range(i,l):
                right=max(right,height[j])
            tot=tot+(min(left,right)-height[i])
        return tot

#Approach 2: Dynamic Programming
def trap(self, height: List[int]) -> int:
        l=len(height)
        tot=0
        left=[0]*l
        right=[0]*l
        left[0]=height[0]
        right[l-1]=height[l-1]
        for i in range(1,l):
            left[i] = max(left[i-1], height[i])
        for i in range(l-2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        for i in range(0, l):
            tot += min(left[i], right[i]) - height[i]
        return tot

#Approach 3: 2-pointers(Best)
def trap(self, height: List[int]) -> int:
        l=len(height)
        left=0
        right=l-1
        leftmax=0
        rightmax=0
        tot=0
        while left<right:
            if rightmax<=leftmax:
                tot += max(0, rightmax-height[right])
                rightmax = max(rightmax, height[right])
                right -= 1
            else:
                tot += max(0, leftmax-height[left])
                leftmax = max(leftmax, height[left])
                left+=1
        return tot