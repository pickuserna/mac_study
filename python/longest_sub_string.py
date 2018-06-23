# -*-coding: utf-8 -*-
def kSmallestPairs(nums1, nums2, k):
	cur_a_sum = None
	next_a_sum = None

	foront_indexes = [0 for i in range(len(nums1))]
	for idx in range(len(nums1)-1):
		a = nums1[idx]
		index_a = front_indexes[idx]
		if index_a > len(nums2):
			continue
		cur_a_sum = a + nums2[index_a]
		next_a = nums[idx+1] 
		index_next_a = front_indexes[idx+1]
		next_a_sum =