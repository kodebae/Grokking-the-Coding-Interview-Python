# Two Pointers

# Understanding the concept:

# Visualize the pointers: Draw diagrams or use online tools to visualize the movement of the pointers and how they interact with the data structure. This can help solidify the logic and identify potential edge cases.
# Grasp the problem type: Analyze the problem and identify whether it involves searching, sorting, finding patterns, or other specific tasks. This helps you choose the appropriate two-pointer technique variation.
# Break down the algorithm: Don't be intimidated by complex-looking solutions. Break them down into smaller steps and understand the purpose of each pointer movement and comparison.

#  Applying the pattern effectively:

# Choose the right direction: Depending on the problem, you might move the pointers from both ends inwards, outwards from the start, or in opposite directions. Analyze the data structure and target to determine the most efficient direction.
# Set clear conditions: Define clear conditions for moving each pointer and for exiting the loop. This ensures the pointers stop at the desired positions and avoid infinite loops.
# Consider edge cases: Test your code on various input scenarios, including empty data, duplicates, extreme values, and specific requirements of the problem.
# Practice explaining your solution: Be able to articulate the purpose of each pointer movement and the logic behind your comparisons. This is crucial for technical interviews and demonstrates your understanding of the algorithm.

# TIPS:
# If an array is sorted, an efficient way would be to start with one pointer in the beginning and another pointer at the end.
# If array is in ascending order, to get larger sum, increase starting pointer. Smaller sum, decrease end pointer.

# Edge Cases for Week 1:
# Two Pointers(Specific edge cases will depend on the exact pattern, but here are some common ones to consider):

# Empty input data: What happens if there are no elements in the data structure?
# Single element input: How does your solution handle data with only one element?
# Duplicates in the data: Does your solution account for duplicate elements and how should it handle them?
# Extreme values: How does your solution behave with very large or very small values (e.g., overflows, underflows)?
# Null or invalid inputs: How should your code handle unexpected or invalid input values?


# Problems:

# Pair with a target sum: A good example of two pointers that start at opposite ends

def pair_with_targetsum(arr, target_sum):

    left, right = 0, len(arr)-1
    
    while(left < right): # The loop iterates as long as left is less than right.

	    current_sum = arr[left] + arr[right] # Inside the loop, we calculate the current sum by adding the elements at left and right indices.

		if current_sum == target_sum: # We found the pair! We return [left, right] to indicate their positions.

	        return [left, right]

		if target_sum > current_sum: # This means the current pair's sum is smaller than the target. We need a pair with a bigger sum, so we increment left to move to the next element on the left side.

			left += 1 # move the left pointer to get a python two_pointers.py
            larger sum

		else: # This means the current pair's sum is larger than the target. We need a pair with a smaller sum, so we decrement right to move to the next element on the right side.

			right -= 1 # move the right pointer to get a smaller sum

	return [-1, -1] #  If the loop finishes iterating without finding any pair whose sum equals the target sum, it means no such pair exists in the array. In this case, we return [-1, -1] to indicate that no valid pair was found.
    # Essentially, [-1, -1] signifies that the search for the desired pair within the given constraints was unsuccessful. This is a commonly used convention in such algorithms to differentiate between a successful lookup and a failed one.

# test our code
def main():

    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))

    print(pair_with_targetsum([2, 5, 9, 11], 11))

main()

# Remove duplicates 

def remove_duplicates(arr):

    next_non_duplicate = 1 # This variable keeps track of the index where the next unique element should be placed, or the index of the next non-duplicate element. Initially, it starts at 1, assuming the first element is unique.

    i = 1 # This variable iterates through the array to compare elements.

    while(i < len(arr)): # The loop iterates as long as i is less than the length of the array. Inside the loop, we compare the element at arr[next_non_duplicate - 1] (previous unique element) with the current element at arr[i].

    if arr[next_non_duplicate - 1] != arr[i]: # if the elements are different, This means we found a unique element. We move it to the position marked by next_non_duplicate by assigning arr[next_non_duplicate] = arr[i].

        arr[next_non_duplicate] = arr[i] # if the elements are duplicates, We simply skip the duplicate element by incrementing i without modifying next_non_duplicate. This leaves the duplicate element unmoved and focuses on finding the next unique element.

        next_non_duplicate += 1 # Then, we increment both next_non_duplicate and i to advance to the next elements.

        i += 1

    return next_non_duplicate # After the loop finishes iterating through the entire array, next_non_duplicate points to the index where the next unique element should be placed (even if it's already empty). Therefore, we return next_non_duplicate as the index of the next non-duplicate element in the array.

# Notes: This algorithm operates in-place by modifying the original array. It doesn't create a new array without duplicates.

# This algorithm has the following space and time complexity:

 # Space Complexity: O(1)

# The algorithm only uses two additional variables (next_non_duplicate and i) to track positions in the array. This is considered constant space complexity since it doesn't depend on the input size.
# Time Complexity: O(n)

# The loop iterates through the entire array once (n times), comparing each element with the previous unique element. This leads to a linear time complexity (O(n)).

# test our code 
def main():

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))

print(remove_duplicates([2, 2, 2, 11]))

# This code removes duplicates from an array but may not address some edge cases. Some potential edge cases to consider:
# Empty array: The function assumes the array has at least one element. If the array is empty, the loop won't run, and next_non_duplicate remains at 1, which might be misleading. You could add a check before the loop and handle the empty case explicitly.
# All elements are duplicates: If all elements in the array are the same, the loop will continue iterating, but no elements will be swapped. This will result in next_non_duplicate pointing to the last element, which might not be desired. You could modify the logic to stop the loop early if no element has been swapped after a certain number of iterations.
# Negative indices: The function assumes the next_non_duplicate index starts at 1. If you allow negative indices to represent empty positions, you might need additional checks to ensure valid index manipulation.
# Overflow: If the array is very large and next_non_duplicate approaches the maximum integer value, adding 1 might cause an overflow error. You could use alternative data structures or calculations to avoid this issue.


# squaring a sorted array: This function uses a two-pointer approach to compare and place elements in the desired order while efficiently calculating and storing their squares

def make_squares(arr):

	n = len(arr) # n: Stores the length of the array.

	squares = [0 for x in range(n)] # Creates an empty array of size n to store the squared elements.

	highestSquareIdx = n - 1 # Points to the last index where a square should be placed (initially at n-1) or the last element in the array.

	left, right = 0, n - 1 # left, points to the first element in the original array, right points to the last.

	while left <= right: # The loop iterates as long as left is less than or equal to right. Inside the loop, we calculate the squares of the elements at left and right indices.

		leftSquare = arr[left] * arr[left] 

		rightSquare = arr[right] * arr[right]

		if leftSquare > rightSquare: # If leftSquare > rightSquare: This means the square of the left element is bigger. We place it in the highest remaining position (squares[highestSquareIdx]) and advance left to the next element.If leftSquare <= rightSquare: This means the square of the right element is bigger or equal. We place it in the highest remaining position and move right one step back.

			squares[highestSquareIdx] = leftSquare 

			left += 1

		else: 

			squares[highestSquareIdx] = rightSquare

			right -= 1

			highestSquareIdx -= 1 # After placing the chosen square, we decrement highestSquareIdx to point to the next available position.

	return squares # After the loop finishes, the squares array contains the original elements squared and sorted in ascending order.

def main():

	print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))

	print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))

main()

# Notes: Squaring in "non-decreasing" order, means that the array is sorted in ascending value, but the values can contain duplicates. 
# Empty array: If the input array is empty, the loop won't run, and you might need to handle this case explicitly by returning an empty array or a different indication.
# All elements the same: If all elements in the array are the same, the loop will continue iterating, but no values will be swapped. This will result in the squares array filled with the same squared value multiple times, which might not be the desired outcome. You could modify the logic to break the loop early if no element has been chosen after a certain number of iterations.
# Overflow: With very large integers or negative values, calculating the squares could potentially lead to integer overflows. Consider using alternative data structures like unsigned integers or performing checks to avoid overflows during calculation.
# Special corner cases: Depending on the specific implementation and requirements, you might need to consider additional edge cases like handling the first and last elements separately, dealing with zero values, or ensuring consistent behavior for extreme negative values.
# Negative numbers and sorting order: This algorithm sorts the squared values, which might differ from the original order if negative numbers are present. Depending on your desired sorting behavior for negative numbers, you might need to adjust the comparison logic within the loop or modify the final output after finishing the square placement.


