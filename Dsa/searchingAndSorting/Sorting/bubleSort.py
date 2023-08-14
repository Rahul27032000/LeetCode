'''Bubble Sort is Like Organizing Your Friends by Height:

Bubble sort is like a game where you compare your friends' heights and swap them if they're not standing in the right order. Here's how you'd do it:

Start from the beginning of the line (the left side).
Look at the first two friends and see who is taller.
If the taller friend is on the left, swap their positions. Now the taller friend is on the right.
Move one step to the right and compare the next pair of friends. Keep doing this until you've compared everyone.
Now the tallest friend is at the far right end of the line. You can think of this as the "bubbliest" friend.
Start again from the beginning, but this time leave out the "bubbliest" friend (the one on the far right).
Keep doing steps 2 to 6 until all your friends are standing in order from shortest to tallest.'''
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


numbers = [5, 2, 9, 1, 5, 6]
bubble_sort(numbers)
print(numbers)  # Now the numbers will be sorted: [1, 2, 5, 5, 6, 9]
