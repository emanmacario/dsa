from random import randint

def search(nums, target):
    r = find_rotation_index(nums)

    result = binary_search(nums, target, 0, r-1)
    if result > -1:
        return result

    result = binary_search(nums, target, r, len(nums)-1)

    return result


def binary_search(A, target, L, R):
    result = -1
    while L <= R:
        M = (L + R) // 2
        if A[M] == target:
            return M
        elif A[M] < target:
            L = M + 1
        else:
            R = M - 1
    return result


def find_rotation_index(A):
    """
    Finds rotation index in a cyclically sorted array
    """
    L, R = 0, len(A) - 1
    while L < R:
        M = (L + R) // 2
        if A[M] > A[R]:
            L = M + 1
        else:
            R = M

    return L


if __name__ == '__main__':
    sorted_A = sorted(set(randint(0, 20) for _ in range(8)))
    r = randint(1, len(sorted_A))
    cyclic_A = sorted_A[r:] + sorted_A[:r]
    print('Cyclic A: ' + ''.join(f'{n:3} ' for n in cyclic_A))
    print('Indexes : ' + ''.join(f'{i:3} ' for i in range(len(cyclic_A))))
    print(f'Rotation Index: {find_rotation_index(cyclic_A)}')
    print('---')
    target = randint(0, 20)
    print(f'Target: {target}')
    print(f'Index:  {search(cyclic_A, target)}')
    