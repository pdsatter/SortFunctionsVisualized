# SortFunctionsVisualized
Visualizes sort functions. Allows user inputted source functions along with some base sort functions.

## To use custom sort functions
### Text
Add text at bottom of GUI. Make sure it is written in python, implements draw, and is properly indented.

### Code File
If you want to add a sort functions by file, instead of by text. Follow these instructions:

1. Upload file to folder: sortFunctions
2. Import function to gui
3. Add function to factory: get_sort_function_factory
4. Add to: choices

## Draw Function
Uses to draw on the canvas. Should be called every time canvas needs updated.
### Inputs for draw() function

* canvas: tkinter canvas (or other canvas that implements same interface), which the objects will be drawn on
* array: array that needs sorted
* red_pointer_locations: default is empty. Displays the rectangles at the indexes as red
* green_pointer_locations: default is empty. Displays the rectangles at the index as green
* margin_top, margin_bottom_ margin_left, margin_right: default for bottom is 0. The others are defaulted to 10. Sets the margins of the canvas

