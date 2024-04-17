# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log(m+n)).

def findMedianSortedArrays(nums1, nums2):
    arr = []
    left = 0
    right = 0
    while left < len(nums1) and right < len(nums2):
        if nums1[left] < nums2[right]:
            arr.append(nums1[left])
            left += 1
        else:
            arr.append(nums2[right])
            right += 1
    while left < len(nums1):
        arr.append(nums1[left])
        left += 1
    while right < len(nums2):
        arr.append(nums2[right])
        right += 1
    mid = len(arr) // 2
    return (arr[mid]+arr[mid-1])/2 if len(arr) % 2 == 0 else arr[mid]*1.0
