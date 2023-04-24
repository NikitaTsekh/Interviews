from typing import List
# Сложность О(n)
#
# Дан список prices
# prices[i] – цена акции в i-тый день.
# Нужно написать функцию, которая возвращает максимальную прибыль (разницу между ценой покупки и ценой продажи в будущем), которую возможно получить
# Если прибыль не может быть получена, вернуть 0
#
# Пример 1:
nums = [7,1,5,3,6,4]
#Output: 5

# Пример 2:
nums = [7,6,4,3,1]
#Output: 0

def sorting_list(nums:List) -> List:
    """
    Returns sorted list
    :param prices:
    :return: int
    """
    nums_ = nums.copy()
    min = 0
    sorted_list = []
    while len(nums_) > 0:
        for i in range(len(nums_)):
            if nums_[i] < min:
                min = i
        sorted_list.append(nums[i])
        nums_.pop(min)

    return sorted_list



def check_function():
    assert sorting_list(nums = [5,4,3,2,1]) == [1,2,3,4,5]
    assert sorting_list(nums = [-1,-2,-4]) == [-4,-2,-1]
    assert sorting_list(nums = [0,0,0]) == [0,0,0]
    assert sorting_list(nums = [7,6,4,3,1]) == [1,3,4,6,7]


check_function()

