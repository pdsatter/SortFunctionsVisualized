# template: https://www.geeksforgeeks.org/python-program-for-quicksort/

def partition(array, low, high, draw, canvas):
 
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
 
            (array[i], array[j]) = (array[j], array[i])
            draw(canvas, array, red_pointer_locations=[i,j], green_pointer_locations=[high+1, low-1])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    draw(canvas, array, red_pointer_locations=[i,j], green_pointer_locations=[high+1, low-1])
 
    return i + 1 
 
def quickSort(array, draw, canvas, low=0, high=None):
    if high is None: high = len(array)-1

    if low < high:
        pi = partition(array, low, high, draw, canvas)

        quickSort(array, draw, canvas, low, pi - 1)
        quickSort(array,draw, canvas,  pi + 1, high)