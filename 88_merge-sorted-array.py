def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    nums1 = .... will false, because it actually create new variable (in python), so its not what the question asked (modify nums1 in-place)
    so we have to modify with ===> nums1[0:m+n] or just nums1[:]
    """
    nums1[:] = sorted(nums1[:m] + nums2[:n])
