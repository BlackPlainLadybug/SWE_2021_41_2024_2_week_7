from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
	for a in range(len(nums)):
		for b in range(len(nums)):
			if a != b:
				if nums[a]+nums[b]==target:
					return [a,b]
