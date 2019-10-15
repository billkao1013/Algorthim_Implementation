class LC_1:
	"""docstring for LC_1"""
	@classmethod
	def twoSum(self, nums, target):
		numdict = dict()
		for idx, num in enumerate(nums):
		    if target - num in numdict:
		        return [numdict[target - num], idx]
		    numdict[num] = idx
		return []

if __name__ == '__main__':
	print(LC_1.twoSum([1,2,4,6], 6))