# 题目：使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
def find_point(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        # 已经有序，说明找到旋转点或者原数组没有旋转，可以退出循环
        if nums[left] < nums[right]:
            break
        mid = (left + right) // 2
        # 还在升序序列中，说明旋转点还在右边，改变 left
        # 这里取等于是因为前面的计算 mid 会偏向 left， 即可能 mid = left，所以 left 变化时要加一
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == "__main__":
    print(find_point([4, 5, 6, 7, 0, 1, 2]))
    print(find_point([7, 8, 0, 1, 2, 3, 4]))
    print(find_point([1, 3]))
    print(find_point([3, 1]))
