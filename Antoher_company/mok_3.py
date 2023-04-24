from typing import List
# Дан список двоичных значений (0,1) nums и целое число k.
# Нужно написать функцию, которая возвращает максимальную длину последовательных единиц в списке,
# при условии, что вы можете заменить не более k нулей (K<=len(nums)).
#
# Пример 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
#
# Пример 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10

def max_length(nums:List,k:int) -> List:
    """
    Returns sorted list
    :param prices:
    :return: int
    """
    max_count =0
    count =0
    gap =0
    max_gap = 0
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
            gap = 0
        else:
            if count > max_count:
                max_count = count

            count =0
            gap +=1

            if gap < k:

                count+=1
            if gap > max_gap:
                max_gap = gap
    if count > max_count:
        max_count = count
    return sum(nums)





max_length(nums=[1,0,0,1,0],k=4)
max_length(nums=[0,0,1,0],k=3)




#[2,3,2]  k =3 else

[]


def check_function():
    assert max_length(nums = [1,1,1,0,0,0,1,1,1,1,0],k=2) == 6
    assert max_length(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],k = 3) == 10


#check_function()

