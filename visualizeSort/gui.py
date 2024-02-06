import tkinter as tk
from tkinter import *
from tkCanvas import TKCanvas

from textwrap import dedent

from visualize import draw

from sortFunctions.bubble import bubble
from sortFunctions.fast_bubble import fast_bubble
from sortFunctions.quicksort import quickSort

canvas_width = 1000
canvas_height = 500

DEFAULT_TEXT = dedent("""
# call draw every time pointer moves, with optional params: red_pointer_locations, green_pointer_locations 
# draw(canvas, array) 

# example function, bubble sort
n = len(array)

for i in range(n-1):
    for j in range(0, n-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
        
        draw(canvas, array, red_pointer_locations=[j, j+1], green_pointer_locations=[])
""")

def input_to_int(array):
    for i in range(len(array)):
        array[i] = int(array[i])
    
    return array

def get_sort_function_factory(func_name):
    if func_name == 'Bubble': return bubble
    if func_name == 'Fast Bubble': return fast_bubble
    if func_name == 'Quicksort': return quickSort
    if func_name == 'Custom': return exec_custom_func

    return None

def exec_custom_func(array, draw, canvas):
    custom_code = codeEntry.get("1.0", END)
    exec(custom_code)

def call_sort_function():
    func = get_sort_function_factory(variable.get())
    func(input_to_int(arrayEntry.get().split()), draw, canvas)
 
if __name__ == "__main__":

    root = tk.Tk()

    root.title("Visualize Sort")
    root.geometry(f'{canvas_width+200}x{(canvas_height+700)}')

    canvas = TKCanvas(root, canvas_width, canvas_height)
    canvas.grid(row=0, column=0, columnspan=20)
    
    arrayEntryLabel = tk.Label(root, text="Array: ")
    arrayEntryLabel.grid(row=1, column=0, sticky="nsew")

    arrayEntry = tk.Entry(root)
    arrayEntry.insert(0, "3 9 21 12 62 95 53 58 64 36 35 47 46 76 22 14")
    arrayEntry.grid(row=1, column=1, columnspan=15, sticky="nsew")

    sortButton = tk.Button(root, text="Sort", command=call_sort_function)
    sortButton.grid(row=1, column=17, sticky="nsew")

    choices = ['Bubble', 'Fast Bubble', 'Quicksort', 'Custom']
    variable = StringVar(root)
    variable.set(choices[0])

    sortingFunctionsLabel = tk.Label(root, text="Function: ")
    sortingFunctionsLabel.grid(row=2, column=0, sticky="nsew")

    sortingFunctions = OptionMenu(root, variable, *choices)
    sortingFunctions.grid(row=2, column=1, columnspan=3, sticky="nsew")

    codeEntryLabel = tk.Label(root, text="Custom Sort Function: ")
    codeEntryLabel.grid(row=3, column=0, sticky="nsew")

    codeEntry = tk.Text(root)
    codeEntry.insert(tk.END, DEFAULT_TEXT)
    codeEntry.grid(row=3, column=1, columnspan=50, rowspan=10, sticky="nsew")


    root.mainloop()

    