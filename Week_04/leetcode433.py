class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # BFS
        # bank = set(bank)
        # if end not in bank:
        #     return -1
        # change = {
        #     'A': 'CGT',
        #     'C': 'AGT',
        #     'G': 'ACT',
        #     'T': 'ACG'
        # }
        # queue = deque([(start, 0)])
        # while queue:
        #     start, step = queue.popleft()
        #     for i, v in enumerate(start):
        #         for c in change[v]:
        #             new_start = start[:i] + c + start[i+1:]
        #             if new_start == end:
        #                 return step + 1
        #             if new_start in bank:
        #                 queue.append((new_start, step + 1))
        #                 bank.remove(new_start)
        # return -1

        # 双向BFS
        bank = set(bank)
        if end not in bank:
            return -1
        change = {
            'A': 'CGT',
            'C': 'AGT',
            'G': 'ACT',
            'T': 'ACG'
        }
        start_set, end_set = {start}, {end}
        step = 0
        while start_set:
            step += 1
            new_set = set()
            for start in start_set:
                for i, v in enumerate(start):
                    for c in change[v]:
                        new_start = start[:i] + c + start[i+1:]
                        if new_start in end_set:
                            return step
                        if new_start in bank:
                            new_set.add(new_start)
                            bank.remove(new_start)
            start_set = new_set
            if len(end_set) < len(start_set):
                start_set, end_set = end_set, start_set
        return -1