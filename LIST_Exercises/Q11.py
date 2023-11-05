#11. Write a Python function that takes two lists and returns True if they have at least one common member.


def have_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True  # Found a common member
    return False  # No common member found

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

if have_common_member(list1, list2):
    print("The two lists have at least one common member.")
else:
    print("The two lists have no common members.")


