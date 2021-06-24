#Approach 1: Brute Force
def majorityElement(self, height: List[int]) -> int:
        c=np.unique(np.array(height))
        n=int(len(height)/2)
        for x in c:
            if (height.count(x)>n):
                return (x)
        return ("not found")

#Approach 2: Sorting
def majorityElement(self, height: List[int]) -> int:
        height.sort()
        return height[len(height)//2]

#Approach 3: Hashmaps
def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

#Approach 4:Boyer-Moore Voting Algorithm
def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate