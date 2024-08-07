# About the project

This application is a visualizing tool for sorting algorithms built using Python3 with pygame.

# Guide

### Required setup

- Make sure you have installed [Python 3](https://www.python.org/downloads/) and [pygame](https://youtu.be/Y4Jn0UCqY28?t=163).
- Download the repository, navigate to its directory and run with "python main.py" or "python3 main.py".

### Basic usage

- To select a sorting algorithm click on it; selected button will change its color.
- To run the algorithm click "RUN" (green button).
- While an algorithm is running you can click "FINISH" (blue button) that appeared in place of "RUN" to skip animations of the algorithm"
- To exit the program simply click "X" or use the same shortcut as for any other window on your machine.

### Additional info

- You can shuffle the array by pressing "SHUFFLE" (yellow button)
- You can change the size of the array by clicking: "S" (small), "M" (medium) and "L" (large) buttons; selected button will change its color.
- You can change the animation speed by clicking: "S" (slow), "N" (normal) and "F" (fast) buttons; selected button will change its color.
- You can resize the window as any other on your machine.
- Current settings will be saved to "settings.txt" file.

# About the algorithms

## Sorting algorithms

**Selection sort**: Selection sort repeatedly selects the smallest element from the unsorted portion of the list and moves it to the sorted portion of the list It is an in-place sorting algorithm as it only requires O(1) of additional memory space, but it has a O(n^2) time complexity, making it pretty slow.

**Insertion sort**: Insertion sort iteratively inserts each element of an unsorted list into its correct position in a sorted portion of the list. It is an in-place sorting algorithm as it only requires O(1) of additional memory space, but it has a O(n^2) time complexity, making it pretty slow, but on average it performs better than selection sort.

**Merge sort**: Merge sort is a sorting algorithm that follows the divide-and-conquer approach. It recursively divides the input array into smaller subarrays,sorts those subarrays and then merges them back together to obtain the sorted array. It is **not** an in-place sorting algorithm as it requires O(n) of additional memory space for storing subarrays, but it has a O(n*logn) time complexity, making it much faster than selection or insertion sort.

**Quick sort**: Quick sort is a sorting algorithm that similarly to merge sort follows the divide-and-conquer approach. It repeatedly picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array. It is an in-place sorting algorithm as it only requires O(1) of additional memory space, while also having a O(n*logn) time complexity, making it much faster than selection or insertion sort, making it as fast as merge sort, without requiring additional memory space.

**Tim sort**: Tim Sort is a hybrid sorting algorithm derived from merge sort and insertion sort. It was designed to perform well on many kinds of real-world data. Tim Sort is the default sorting algorithm used by Python’s sorting functions. It is **not** an in-place sorting algorithm as it requires O(n) of additional memory space for storing subarrays (like merge sort), but it has a O(n*logn) time complexity, making it much faster than selection or insertion sort and in cases when the dataset it already partially sorted it is much faster than traditional merge sort or quick sort.
