def task_solution(nums: list, k: int):
    left, right = 0
    current_sum = 0

    while right < len(nums):
        current_sum += nums[right]
        if current_sum > k:
            current_sum -= nums[left]
            left += 1
        right += 1



        
    

print(task_solution([2,5,6,7,9,1,2,3,4,5,6,1,2,3,4,5,6], 10))

# Check if two lists are rotations of each other