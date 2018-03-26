# Uses python3
import sys

def canPartitionN(nums, n):
    def dfs(nums, target, used, todo, lookup):
        if lookup[used] is None:
            targ = (todo-1)%target + 1
            lookup[used] = any(dfs(nums, target, used | (1<<i), todo-num, lookup) \
                                for i, num in enumerate(nums) \
                                if ((used>>i) & 1) == 0 and num <= targ)
        return lookup[used]
    
    total = sum(nums)
    if total%n or max(nums) > total//n:
        return 0
    lookup = [None] * (1 << len(nums))
    lookup[-1] = True
    if dfs(nums, total//n, 0, total, lookup):
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    nums, *A = list(map(int, input.split()))
    print(canPartitionN(A, 3))

