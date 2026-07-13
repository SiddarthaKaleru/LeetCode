class Solution(object):
    def minimumSum(self, num):
        arr = [int(i) for i in str(num)]
        arr.sort()
        n1 = arr[0] * 10 + arr[3]
        n2 = arr[1] * 10 + arr[2]
        return n1 + n2