def my_tuple_four_sum(len,my_tuple,C):
    result = [0] * 4
    my_tuple = sorted(my_tuple)
    min_four_sum =  float('inf')
    for i in range(len - 3):
        for j in range(len - 2):
            left = j + 1
            right = len - 1
            while left < right:
                tuplesum = my_tuple[i] + my_tuple[j] + my_tuple[left] + my_tuple[right]
            if abs(tuplesum - C) < min_four_sum:
                min_four_sum = abs(tuplesum - C)
                result =[my_tuple[i],my_tuple[j],my_tuple[left],my_tuple[right]]
            if tuplesum > C:
                right -= 1
            else:
                left += 1
            return result
len = int(input())
my_tuple = tuple(int(i) for i in input().split(maxsplit=len))
C = int(input())
result = my_tuple_four_sum(len,my_tuple,C)
print(result)
print(sum(result))



            

    