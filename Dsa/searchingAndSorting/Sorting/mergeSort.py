'''Merge Sort is Like Sorting Piles of Toys:

Merge sort is like having a helper (let's call them Helper Elf) who helps you sort your toys. Here's how Helper Elf can help you:

Take all the toys and divide them into two equal piles.
Ask Helper Elf to sort each pile in the same way (dividing and sorting).
Once both piles are sorted, ask Helper Elf to compare the toys and put them in order.
Now you have a big pile of toys that are in order!'''

# time -> n long n
# space -> n

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left_half = numbers[:middle]
    right_half = numbers[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    sorted_numbers = []
    while left_half and right_half:
        if left_half[0] < right_half[0]:
            sorted_numbers.append(left_half.pop(0))
        else:
            sorted_numbers.append(right_half.pop(0))

    sorted_numbers.extend(left_half)
    sorted_numbers.extend(right_half)

    return sorted_numbers


numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)  # Now the numbers will be sorted: [1, 2, 5, 5, 6, 9]
