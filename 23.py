def findMissingNumbers(nums: list) -> list:
    missing_nums = []
    [missing_nums.append(number) for number in range(1, max(nums) + 1) if number not in nums]
    missing_nums.sort()

    return missing_nums


def main():
    print(findMissingNumbers([1, 2, 4, 6]))
    # [3, 5]

    print(findMissingNumbers([4, 8, 7, 2]))
    # [1, 3, 5, 6]

    print(findMissingNumbers([3, 2, 1, 1]))
    # []

    print(findMissingNumbers([5, 5, 5, 3, 3, 2, 1]))
    # [4]

    print(findMissingNumbers([1, 2, 3, 4, 5]))
    # []


if __name__ == "__main__":
    main()