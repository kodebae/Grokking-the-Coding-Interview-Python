# Two Pointers

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

# Note: This algorithm operates in-place by modifying the original array. It doesn't create a new array without duplicates.

# This algorithm has the following space and time complexity:

 # Space Complexity: O(1)

# The algorithm only uses two additional variables (next_non_duplicate and i) to track positions in the array. This is considered constant space complexity since it doesn't depend on the input size.
# Time Complexity: O(n)

# The loop iterates through the entire array once (n times), comparing each element with the previous unique element. This leads to a linear time complexity (O(n)).

# test our code 
def main():

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))

print(remove_duplicates([2, 2, 2, 11]))
