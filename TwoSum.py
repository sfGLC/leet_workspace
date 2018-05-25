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

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        strSet = [0, 1]
        index = 0
        i = 0
        while i < len(s):
            char = s[i]
            substr = s[strSet[0]:i]
            if s[i] in s[strSet[0]:i]:

                i = strSet[0] + s[strSet[0]:i].index(s[i])
                v1 = s.index(s[strSet[0]:i])
                v2 = substr.index(s[i])
                # strSet = list()
                i+= 1
                strSet[0] = i
                continue
            else:
                i += 1
                if result < i - strSet[0]:
                    result = i - strSet[0]


        # for i in range(0, len(s)):
        #     char = s[i]
        #     substr = s[strSet[0]:i]
        #     if s[i] in s[strSet[0]:i]:
        #         if result < i - strSet[0]:
        #             result = i - strSet[0]
        #         i = s.index(s[strSet[0]:i]) + s[strSet[0]:i].index(s[i])
        #         v1 = s.index(s[strSet[0]:i])
        #         v2 = substr.index(s[i])
        #         # strSet = list()
        #         strSet[0] = i
                # strSet[1] = i+1
                # i += 1
            # else:
            #     strSet[1] = i
        return result

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        y = x
        if x < 0:
            y = -x
        l = list()
        while y:
            l.append(y % 10)
            y = y / 10
        l.reverse()
        result = 0
        while l:
            result = result * 10 + l.pop()
        if x < 0:
            result = -result
        return result

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            l = list()
            while x:
                l.append(x % 10)
                x = x / 10
            for i in range(len(l) / 2):
                if l[i] != l[-(i+1)]:
                    return False
        return True

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        print s
        if len(s) == 0:
            return ""
        l = list()
        cycle = numRows + numRows - 2
        for i in range(numRows):
            l.append([])
        j = 0
        print l
        print cycle
        while j < len(s):
            for n in range(cycle):
                if n >= numRows:
                    n = numRows - n - 2
                if j < len(s):
                    l[n].append(s[j])
                j += 1
        print l
        result = ""
        for i in range(numRows):
            while len(l[i]):
                result += l[i].pop(0)
        return result