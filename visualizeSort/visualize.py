import time

def clear_canvas(canvas):
    canvas.delete("all")

def get_fill(i, red_pointer_locations, green_pointer_locations):
    if i in red_pointer_locations:
        return 'red'
    if i in green_pointer_locations:
        return 'green'
    return 'blue'

def draw(canvas, array, red_pointer_locations=[], green_pointer_locations=[], margin_top=10, margin_bottom=0, margin_left=10, margin_right=10):
    clear_canvas(canvas)

    max_height = max(array)
    canvas_height = canvas.height() - margin_bottom
    
    rect_width = int((canvas.width()-margin_right-margin_left) / len(array))
    x = margin_left
    y2 = canvas_height


    for i in range(len(array)):

        rect_height = canvas_height * (array[i]/max_height) - margin_top
        y1 = canvas_height - rect_height
        
        x1 = x
        x2 = x + rect_width
        x += rect_width

        canvas.draw_rectangle(x1, y1, x2, y2, fill=get_fill(i, red_pointer_locations, green_pointer_locations))
        
    canvas.update()
    time.sleep(0.5)
    
    

def max(array):
    if array is None: 
        return None
    
    max = array[0]
 
    for i in range(1, len(array)):
        if array[i] > max:
            max = array[i]

    return max