def sum_of_two(numbers:list[int], target:int):
    """
    Takes a list of integers and target integer. 
    Returns indexes of the first two numbers from the list that add up to the target value.
        
         Arguments:
             numbers(list[int]): a list of integer values
             target(int): 
            
        Returns:
            list[int]: indexes of the first two numbers that add up to the target value.   
    """
    try:
        assert target == int
        assert -1000 <= target <= 1000
    except AssertionError:
        print("The target must must be an integer within a range of 1000")
     
    try:
        for j in numbers:
            assert j == int
            assert 1000 <= j <= 1000
    except AssertionError:
        print("The list must contain only integers within a range of 1000")
         
    try:
        assert 2 <= len(numbers) <= 1000
    except AssertionError:
        print("The list must not exceed 1000 items")
           
    ref={}
    for i, num in enumerate(numbers):
        if target - num in ref and target - num != num:
            return print ([ref[target - num], i])
        else: ref[num] = i
    print("no pairs found") 
