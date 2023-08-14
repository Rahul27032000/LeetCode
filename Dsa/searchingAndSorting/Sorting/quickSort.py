'''

Imagine Sorting Your Colorful Balls:

Imagine you have a bunch of colorful balls, and you want to arrange them in order. You can't swap them directly, 
but you have a special helper called the Swapper Friend who can help!

Quick Sort is Like Dividing and Swapping:

Quick sort is like playing a sorting game with your Swapper Friend. Here's how you can play:

You pick one ball as the "special ball." It can be any ball.
Divide all the other balls into two piles: one with smaller colors and one with bigger colors compared to the special ball.
Give the two piles to your Swapper Friend.
Swapper Friend uses magic to sort each pile by playing the sorting game again.
Now you have the smaller pile, the special ball, and the bigger pile in order!'''


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    smaller = []
    bigger = []

    for num in numbers[1:]:
        if num <= pivot:
            smaller.append(num)
        else:
            bigger.append(num)

    smaller = quick_sort(smaller)
    bigger = quick_sort(bigger)

    return smaller + [pivot] + bigger

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)  # Now the numbers will be sorted: [1, 2, 5, 5, 6, 9]
