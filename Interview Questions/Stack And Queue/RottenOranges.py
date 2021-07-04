from collections import deque

class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
        R=len(grid)
        C=len(grid[0])
        fresh=0
        empty=0
        rotten=deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c]==2:
                    rotten.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        min=0
        while rotten and fresh>0:
            min+=1
            for x in range(len(rotten)):
                x,y=rotten.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == R or yy < 0 or yy == C:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    fresh -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))
        return min if fresh == 0 else -1
#{ 
#  Driver Code Starts


from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends