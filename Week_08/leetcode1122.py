class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 自定义比较函数
        # d = {v: i for i, v in enumerate(arr2)}
        # return sorted(arr1, key=lambda v: d.get(v, len(arr2) + v))

        d = Counter(arr1)
        res = []
        for v in arr2:
            res.extend([v] * d.pop(v))
        # res.extend(sorted(v for v, i in d.items() for _ in range(i)))
        res.extend(v for v, n in sorted(d.items()) for _ in range(n))
        return res