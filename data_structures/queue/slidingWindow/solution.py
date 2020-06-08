class Deque:
	def __init__(self):
		self.array = []
	
	def insertBack(self, value):
		self.array.append(value)
	
	def deleteFront(self):
		self.array.pop(0)
	
	def deleteBack(self):
		self.array.pop()
	
	def getBack(self):
		return self.array[-1]
	
	def getFront(self):
		return self.array[0]
	
	def getCount(self):
		return len(self.array)

class Solution:
    
    def getLastElDeque(self, arr, deque):
	    return arr[deque.getBack()]
    
    def insertIntoDequeAfterPopping(self, nums, i, deque):
        while deque.getCount() > 0 and nums[i] > nums[deque.getBack()]:
            deque.deleteBack()
        deque.insertBack(i)

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = Deque()
        for i in range(k-1):
            self.insertIntoDequeAfterPopping(nums, i, deque)
        result = []
        for i in range(k-1, len(nums)):
            self.insertIntoDequeAfterPopping(nums, i, deque)
            front = deque.getFront()
            result.append(nums[front])
            if front == i+1-k:
                deque.deleteFront()
        return result