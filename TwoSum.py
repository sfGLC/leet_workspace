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

    def recursive(self, s):
        i = 0
        result = ""
        count = 1
        while i < len(s):
            if i+1 < len(s):
                if s[i] != s[i + 1]:
                    result += str(count) + s[i]
                    count = 0
            else:
                result += str(count) + s[i]
            i += 1
            count += 1

        return result

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        k = 1
        s = "1"#self.recursive("1")

        while k < n:
            s = self.recursive(s)
            k += 1
        return s

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_dict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        left = []
        for c in s:
            if c in p_dict.keys():
                left.append(c)
            elif c in p_dict.values():
                if left == [] or p_dict[left.pop()] != c:
                    return False
            else:
                return False
        return left == []

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        index = 0
        while index < len(strs[0]):
            for s in strs:
                if index >= len(s):
                    break
                if s[index] != strs[0][index]:
                    break
            index += 1
        result = strs[0][0: index]
        return result

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x > y:
            x, y = y, x
        sy = bin(y)
        sx = bin(x)
        l = list(sx)
        for i in range(len(sy) - len(sx)):
            l.insert(2, "0")

        counter = 0
        for i in range(len(sy)):
            if sy[i] != l[i]:
                counter += 1
        return counter

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        val = image[sr][sc]
        if val == newColor:
            return image
        image[sr][sc] = newColor
        if sr - 1 >= 0 and image[sr - 1][sc] == val:
            self.floodFill(image, sr - 1, sc, newColor)
        if sr + 1 < len(image) and image[sr + 1][sc] == val:
            self.floodFill(image, sr + 1, sc, newColor)
        if sc - 1 >= 0 and image[sr][sc - 1] == val:
            self.floodFill(image, sr, sc - 1, newColor)
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == val:
            self.floodFill(image, sr, sc + 1, newColor)

        # def fill(x, y):
        #     image[x][y] = newColor
        #     if x - 1 >= 0 and image[x - 1][y] == val:
        #         fill(x - 1, y)
        #     if x + 1 < m and image[x + 1][y] == val:
        #         fill(x + 1, y)
        #     if y - 1 >= 0 and image[x][y - 1] == val:
        #         fill(x, y - 1)
        #     if y + 1 < m and image[x][y + 1] == val:
        #         fill(x, y + 1)
        #
        # val = image[sr][sc]
        # m = len(image)
        # n = len(image[0])
        # if val == newColor:
        #     return image
        #
        # fill(sr, sc)

        return image

    def merge(self, A, p, q, r):
        left = []
        right = []
        for i in A[p:q + 1]:
            left.append(i)
        for j in A[q + 1:r]:
            right.append(j)
        i = j = 0
        for k in range(p, r):
            if i < len(left) and j < len(right):
                if left[i] < right[j]:
                    A[k] = left[i]
                    i += 1
                else:
                    A[k] = right[j]
                    j += 1


    def mergeSort(self, A, s, e):
        if e - s == 0:
            return
        mid = (e - s) / 2
        self.mergeSort(A, s, s + mid)
        self.mergeSort(A, s + mid + 1, e)
        self.merge(A, s, mid, e)