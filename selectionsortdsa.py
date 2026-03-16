n=[9,5,4,6,3,8,2,1]
def selectionsort(nums):
    n=len(nums)
    for i in range(0,n):
        min_ind=i
        for j in range(i+1,n):
            if nums[j]<nums[min_ind]:   
                mini_ind=j
                nums[i],nums[min_ind]=nums[min_ind],nums[i]
                return nums
print(selectionsort(n))
