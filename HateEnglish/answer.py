# 영어를 숫자로 바꿔야함
# 영어리스트를 만들어서 numbers의 해당 영어를 인덱스 값으로 바꿔
# 그걸 다시 숫자로...
def solution(numbers):
    nums = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    for i, nums in enumerate(nums):
        numbers = numbers.replace(nums, str(i))
    return int(numbers)