class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = collections.Counter(nums)
        # res = [(k, v) for k, v in count.items()]
        # res.sort(key=lambda x: x[1], reverse=True)
        # return [i[0] for i in res][:k]

        return [i[0] for i in collections.Counter(nums).most_common(k)]

        # frq = defaultdict(list)
        # for key, cnt in Counter(nums).items():
        #     frq[cnt].append(key)
        # res = []
        # for times in range(len(nums), 0, -1):
        #     if times in frq:
        #         res.extend(frq[times])
        #         if len(res) >= k: return res[:k]