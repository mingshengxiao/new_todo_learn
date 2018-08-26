# -*- coding: utf-8 -*-

class SortMethods(object):
	def __init__(self, sort_data):
		self.sort_data = sort_data

	def bubble_sort(self):
		u"""
		冒泡排序
		重复遍历要排序的数列，一次比较两个元素，如果顺序错误则交换这两个元素
		"""
		sort_data = self.sort_data
		n = len(sort_data)
		for j in range(n - 1):
			for i in range(0, n - 1 -j):
				if sort_data[i] > sort_data[i + 1]:
					sort_data[i], sort_data[i + 1] = sort_data[i + 1], sort_data[i]
		return sort_data

	def select_sort(self):
		u"""
		选择排序
		首先在未排序序列中找到最小或最大值元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中
		继续寻找最小或最大元素，然放到已排序序列的末尾。
		"""
		sort_data = self.sort_data
		n = len(sort_data)
		for j in range(n - 1):
			min_index = j
			for i in range(j + 1, n):
				if sort_data[min_index] > sort_data[i]:
					min_index = i
			sort_data[j], sort_data[min_index] = sort_data[min_index], sort_data[j]
		return sort_data

	def insert_sort(self):
		u"""
		插入排序
		通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置插入。
		"""
		sort_data = self.sort_data
		n = len(sort_data)
		for j in range(1, n):
			i = j
			while i > 0:
				if sort_data[i] < sort_data[i - 1]:
					sort_data[i], sort_data[i - 1] = sort_data[i - 1], sort_data[i]
					i -= 1
				else:
					break
		return sort_data

	def quick_sort(self, first, last):
		u"""
		快速排序
		通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的素有数据都要小，
		然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行。
		"""
		if first >= last:
			return
		sort_data = self.sort_data
		n = len(sort_data)
		low = first
		high = last
		mid_value = sort_data[low]
		while low < high:
			while low < high and sort_data[high] >= mid_value:
				high -= 1
			sort_data[low] = sort_data[high]
			while low < high and sort_data[low] < mid_value:
				low += 1
			sort_data[high] = sort_data[low]
		sort_data[low] = mid_value
		# 对low左边的列表执行快速排序
		self.quick_sort(first, low - 1)
		# 对low右边的列表进行快速排序
		self.quick_sort(low + 1, last)
		return sort_data

if __name__ == '__main__':
	data = [43,54,36,44,15,86,19,4,8,20]
	print(data)
	sort_method = SortMethods(data)
	print('冒泡排序：' + str(sort_method.bubble_sort()))
	print('选择排序：' + str(sort_method.select_sort()))
	print('插入排序：' + str(sort_method.insert_sort()))
	print('快速排序：' + str(sort_method.quick_sort(0, len(data) - 1)))