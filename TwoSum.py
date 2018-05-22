class Solution(object):
    def twoSum(self, nums, target):
        # lookup = dict(((v, i) for i, v in enumerate(nums)))
        # return next(((i + 1, lookup.get(target - v) + 1)
        #              for i, v in enumerate(nums)
        #              if lookup.get(target - v, i) != i), None)

        # lookup = {}
        # for cnt, num in enumerate(nums):
        #     if target - num in lookup:
        #         return lookup[target - num], cnt
        #     lookup[num] = cnt



            # d = dict()
        # for i in range(len(nums)):
        #     if len(d[nums[i]]) > 0:
        #         d[nums[i]].append(i)
        #     else:
        #         d[nums[i]] = [i]
        # print d
        # # for i in range(len(nums)):
        # #     v1 = nums[i]
        # #     v2 = target - v1
        # #     if len(d[v2]) > 1:
        #
        #
        # #
        d = dict((n, i) for (i, n) in enumerate(nums))
        print d
        for i in range(len(nums)):
            val1 = nums[i]
            if d.has_key(target - val1) and d[target - val1] != i:
                return [i, d[target - val1]]

        #
        # for i in range(len(nums)):
        #     result = []

        # for i in range(len(d)):
        #     val1 = d[i]
        #     val2 = target - val1
        #     if
        #
        # for val1 in d.values():
        #     val2 = target - val1
        #     if val2 in d.values():
        #         return [d[val1], d[val2]]