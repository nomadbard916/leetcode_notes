def sliding_window(nums):
    left = 0
    right = 0
    window = []

    # Doesn’t this sliding window framework also use a nested while loop? Why is the time complexity O(N)?

    # Simply put, the pointers left and right never move backward (their values only increase), so each element in the string/array enters the window once and exits the window once. No element enters and exits the window multiple times, so the time complexity is proportional to the length of the string/array.

    # In contrast, the brute-force solution with nested for loops has the j pointer move backward, which causes some elements to enter and exit the window multiple times, leading to a time complexity of 𝑂 ( 𝑁 squrare).
    while right < len(nums):
        curr_r_elm = nums[right]
        window.append(curr_r_elm)

        # manipulating window data

        # Expand the window
        right += 1

        while left < right and needs_shrink(window):
            curr_l_elm = nums[left]
            window.remove(curr_l_elm)

            # manipulating window data

            # shrink the window
            left += 1

    return result


def needs_shrink(window):
    # Define your shrinking condition here
    pass


# Example usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
result = sliding_window(nums)
