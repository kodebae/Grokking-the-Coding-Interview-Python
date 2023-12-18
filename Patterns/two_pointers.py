# Two Pointers

# TIPS:
# If an array is sorted, an efficient way would be to start with one pointer in the beginning and another pointer at the end.
# If array is in ascending order, to get larger sum, increase starting pointer. Smaller sum, decrease end pointer.

# Pair with a target sum

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

# test our code
def main():

    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))

    print(pair_with_targetsum([2, 5, 9, 11], 11))

main()
