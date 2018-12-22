class Solution:
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = 0
        for i in range(len(A)-1):
            if A[i] == B[i]:
                continue

            container = []
            for j in range(i+1, len(A)):
                if A[j] == B[i] and A[j] != B[j]:
                    container.append(j)
                    if A[i] == B[j]:
                        A = A[:i] + A[j] + A[i+1: j] + A[i] + A[j+1:] # swap A[i] and A[j]
                        return 1 + self.kSimilarity(A[i+1:], B[i+1:]) 
            
            times = len(A) - 1

            for j in container:
                A = A[:i] + A[j] + A[i+1: j] + A[i] + A[j+1:] # swap A[i] and A[j]
                times = min(times, 1 + self.kSimilarity(A[i+1:], B[i+1:]))
                A = A[:i] + A[j] + A[i+1: j] + A[i] + A[j+1:] # swap A[i] and A[j]
            
            return times

        return 0

test = Solution()
A = 'aabc'
B = 'abca'
print(test.kSimilarity(A, B))