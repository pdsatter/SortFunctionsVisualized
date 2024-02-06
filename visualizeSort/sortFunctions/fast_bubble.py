def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

def fast_bubble(array, draw, canvas):
    n = len(array)

    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
                swapped = True
            
            draw(canvas, array, red_pointer_locations=[j,j+1])
        
        if not swapped: 
            return
