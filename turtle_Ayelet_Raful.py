
# Turtle Village — Lite (Student Scaffold)
# Focus: loops, decisions, try/except, and small functions.
# Run this file locally (IDLE/Thonny/PyCharm).

# ===>>>  REMOVE PASS IN ALL METHODS TO CODE

# NOTE about Turtle coordinate axis.
# turtle centers the origin (x == 0, y == 0 ) in the center of the canvas
# so if our default screen size is : CANVAS_W, CANVAS_H = 800, 600
#  the corners of your screen are :
# Top-left: (-CANVAS_W/2, CANVAS_H/2) → (-400, 300)
# Top-right: ( CANVAS_W/2, CANVAS_H/2) → ( 400, 300)
# Bottom-left: (-CANVAS_W/2, -CANVAS_H/2) → (-400, -300)
# Bottom-right: ( CANVAS_W/2, -CANVAS_H/2) → ( 400, -300)
"""
Pseudocode:
1. Import the turtle and random libraries
2. Figure out the size and corners of the page and name them with variables
3. Decide out of which shapes you will make the house and what added on elements they will have - sun, door, tree, 2 options for a roof
4. Set the different size options for the house
5. Set the color themes
6. Create a move to function that you can use throughout the program to position the pen at the proper starting point when drawing a shape
   This function uses the turtle library to lift the pen and move it to the proper position
7. Create a function that draws the lines from one point to the next - This will be used to draw the separators between the houses.
    This function calls the move_to  function to move the pen to the proper starting point and then tells where to draw a line to.
8. Create a function that draws a rectangle and fills it - This shape can be used for the door, body of house, roof or trunk of tree.
    This function sets the fill color and pen color and uses the move to function. It also gives instructions of how to draw a rectangle – to go forward(w),
    turn 90 degrees right, draw forward(h)  and turn 90 degrees right. This is in a for loop so that it will run twice to fully draw a rectangle.
9. Create a function that draws a triangle and fills - This shape will be used for the roof.
    In this function the 3 points of the rectangle are defined and the triangle is drawn by commands to go from one point to the next
10. Create a function that draws a circle and fill it - This will be used for the sun and tree.
    This function gives the coordinates of the tree to the move_to function and draws the circle.
11. Create a function that manages the user input for the amount of houses per row and for how many rows.
    This function will handle any input errors using a try and except, and it is within a while loop so that it can reprompt on error.
    There is also an if statement that checks that the user’s input is within the allowed options. If user input is not within allowed options it will reprompt.
12. Create a function that manages the user input for the size, color theme, roof type and sun. This function will handle any input errors using an allowed set
    and while loop to reprompt. It also contains an if statement that checks the user’s input against the allowed list.
    If user input is not in the list – it will reprompt.
13. Create a function that draws the straight column and row separators - use a for loop to do this.
    This function defines the border of the canvas and uses a for loop to draw the horizontal and vertical separators.
    It then calls the draw_line function to draw the lines.
14. Create a function that will draw a house centered within the cell. Within this function the roof will also be drawn. This function will call the
    fill_rect_center to draw the house and if the user selects a triangle rooft it will provide the coordinates and call the fill triangle function.
    If the user chooses a flat roof, it will draw a flat roof using the fill_rect_center function. In this function the door is also drawn using
    the fill_rect_center function.
15. Create a function that will draw a tree and position it at the right place within each cell.
    Setting the width, height, and positon for the tree and using the fill_rect_center function to draw it.
    Also, drawing the canopy using the fill_circle_center function.
16. Create a draw village function that calls all the other functions and that uses a for loop to place the houses in  the grid.
    Within the nested loop, call the draw_house_center function and draw_tree_near function.  Also, define the center of each cell so that houses will be centered.
17. Create a main function that asks the user for his input, and that sets the allowed sets.
    Also, set the window, the size of the property and then call the draw village function
19. Call the main function

"""

import turtle as T
import random

# ---------- constants ----------
CANVAS_W, CANVAS_H = 800, 600
TOP_MARGIN, BOTTOM_MARGIN = 40, 40


# size of houses
SIZES = {
    "s": (120, 80),
    "m": (150, 100),
    "l": (180, 120),
}

'''
How to use Themes : 
# Use a theme like this:
colors = THEMES[theme_key]          # where theme_key is either "pastel" or "primary"
body_c  = colors["body"]            # we then can access the colors for the body of the house
roof_c  = colors["roof"]            # color of the roof of the house 
door_c  = colors["door"]            # door 
win_c   = colors["window"]          # window -- feel free to add or change the colors 
                                    # there is are beautiful pallette choices at coolors.co

# how to apply :
fill_rect_center(cx, cy, w, h, body_c)  # house body
'''
THEMES = {
    "pastel": dict(body="#ffd1dc", roof="#c1e1c1", door="#b5d3e7", window="#fff7ae"),
    "primary": dict(body="red", roof="blue", door="gold", window="#aee3ff"),
}

# ---------- tiny turtle helpers (provided) ----------
def move_to(x, y):
    '''
    x - position on x coordinate axis
    y - position on y coordinate axis
    '''
    T.penup(); T.goto(x, y); T.pendown()

def draw_line(x1, y1, x2, y2):
    '''
       we draw a line from x1,y1
       x1 - position on x coordinate axis
       y1 - position on y coordinate axis
       
       to x2, y2
       x2 - position on x coordinate axis
       y2 - position on y coordinate axis
       '''
    move_to(x1, y1); T.goto(x2, y2)

def fill_rect_center(cx, cy, w, h, color):
    '''
    cx - center of rectangle x coordinate 
    cy - center of rectangle y coordinate 
    w - width of rectangle 
    h - height of rectangle 
    color - color of rectangle 
    '''
    T.fillcolor(color); T.pencolor("black")
    move_to(cx - w/2, cy + h/2)
    T.begin_fill()
    for _ in range(2):
        T.forward(w); T.right(90); T.forward(h); T.right(90)
    T.end_fill()

def fill_triangle(p1, p2, p3, color):
    """
    Draw a filled triangle defined by three points.
    
    p1 — point 1 (x1, y1)
    p2 — point 2 (x2, y2)
    p3 — point 3 (x3, y3)
    color — fill color for the triangle
    
    Notes:
    - Each point is an (x, y) tuple.
    - Depending on your triangle, some x’s or y’s may be equal (e.g., flat base).
    
    Example:
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    fill_triangle(p1, p2, p3, color)
    """

    T.fillcolor(color); T.pencolor("black")
    move_to(*p1); T.begin_fill()
    T.goto(*p2); T.goto(*p3); T.goto(*p1)
    T.end_fill()

def fill_circle_center(cx, cy, r, color):
    '''
    a circle is defined by 
    cx - the center of your circle, x coordinate 
    cy - center of your circle, y coordinate 
    r - radius 
    color - color of circle 
    '''
    T.fillcolor(color); T.pencolor("black")
    move_to(cx, cy - r)  # turtle draws circles from the bottom
    T.begin_fill(); T.circle(r); T.end_fill()

# ---------- input helpers (complete; you may extend) ----------
def ask_choice_int(prompt, allowed):
    """
    Ask the user for an integer from the allowed set,
    reprompt using a while loop and use a try and except to catch errors.
    This function will check the user input for houses per row and how many houses.
    """


    # Creating a variable that represents what the user input is allowed to be using a set
    allowed_set = set(allowed)
    # Created while loop to check users input
    while True:
        # Using a try and except to catch any bad input from user
        try:
            # Asking the user for a valid number in the allowed list
            val = int(input(prompt + f'{allowed}'))
            # If user input doesn't match an item on the list it will reprompt
            if val not in allowed:
               print("Not allowed in choices")
            else:
                return val

        except ValueError:
            print("That is not a valid number.")



def ask_choice_str(prompt, allowed):
    """
    Asking the user for a string and reprompting using a while loop if there is an error. Using a try and except
    that will print if an incorrect value is entered.
    Prompting for the house size, color theme, roof type and sun


    """
    # converting the allowed list to lowercase to avoid problems with user input
    allowed_lower = [a.lower() for a in allowed]
    # Using a while loop here to check user input for the string values
    while True:
        try:
            # Asking user to input something from the allowed list
            string = input(prompt + f'{allowed}')

            # Converting user input to lowercase and then checking it against the list
            if string.lower() in [a.lower() for a in allowed]:
                # If the user's response is in the list, it will return their response
                return string
            else:
                print("Invalid choice")
                continue
        except TypeError:
            print("Please enter a string")
            continue




def draw_roads(cols, rows, cell_w, cell_h):
    """
    This function draws the separator lines between the rows and columns

    """
    # Defining the borders of the canvas
    top_y = CANVAS_H / 2 - TOP_MARGIN
    bot_y = -CANVAS_H / 2 + BOTTOM_MARGIN
    left_x = -CANVAS_W / 2
    right_x = CANVAS_W / 2



    # Setting the pen color and size
    T.pensize(1); T.pencolor("black")
    # Drawing the horizontal separators using a for loop, so that it can go draw the proper amount of lines
    for r in range(1,rows):
        # multiply row * cell height and then subtract that from the top border to find the proper starting point for the line on the y axis.
        y = top_y - r * cell_h
        # These are the coordinates of where we are drawing the line - start and end point.
        draw_line(left_x,y, right_x,y)

    # Drawing the vertical separations using a for loop
    for c in range(1,cols):
        # Finding the proper starting point for each vertical separation.
        x = left_x + c * cell_w
        # Here are the coordinates of where we are drawing the line - start and end point.
        draw_line(x,top_y, x, bot_y)



def draw_house_centered(cx, cy, size_key, theme_key, roof_style):
    """
    Drawing a house within each cell that is centered at cx, cy (the cell's center)
    """
    # width/height
    w, h = SIZES[size_key]
    colors = THEMES[theme_key]

    # Here we are filling the rectangle and giving it the proper coordinates
    fill_rect_center(cx, cy, w, h, colors['body'])

    # This is the point of the roof apex
    yT = cy + h / 2
    # Here we draw a triangle if the user selected that for the roof shape
    if roof_style == "triangle":
        # Setting the 3 different points of the triangle
        p1 = (cx - w/2, cy + h/2)
        p2 = (cx, yT + 0.5*h)
        p3 = (cx + w/2, cy + h/2)
        # Calling the fill triangle function to draw the triangle
        fill_triangle(p1,p2,p3,colors['roof'])
    # If the user selects flat, we draw a flat roof using the function for drawing rectangles
    else:
        fill_rect_center(cx -.5, cy + h / 1.6, w, h * .25, colors['roof'])


    # Here we are positioning a door, which also uses the rectangle function which is centered on x = cx
    fill_rect_center(cx, cy-h/5, w*.3, h*.6, colors['door'])




def draw_tree_near(cx, cy, size_key):
    """Drawing a small tree near the house that can be on either side of the house."""
    # Drawing the trunk
    w, h = SIZES[size_key]
    # Setting the trunks width and height
    tw, th = w*0.10, h*0.40
    # Placing the tree to either the left or right of the house randomly
    side = random.choice([-1, 1])
    # Setting the coordinate of where the trunk should be drawn from
    tx = cx + side * (w*0.45)
    ty = cy - h*0.5 + th/2
    # Drawing the trunk of the tree by calling the fill_rect_center function
    fill_rect_center(tx, ty, tw, th, "brown")

    # Setting a radius for the circle in order to set the circle's size
    r = w*.15


    # Drawing the canopy for the tree, and positioning it by calling the fill_circle_center function.
    fill_circle_center(tx, cy, r, "green")


def draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style):
    """ Calculate the cell sizes, draw the roads and use a nested for loop to draw the grid for the houses."""
    # Setting the cell width and height
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows


    # Calling the draw roads function
    draw_roads(cols,rows, cell_w, cell_h)

    # Creating a nested loop that will place the houses in the proper cells - create a grid and draw the houses
    for r in range(rows):
        for c in range(cols):
            # Calculating the center within each cell- x coordinate and y coordinate
            cx = -CANVAS_W / 2 + (c + 0.5) * cell_w

            cy = CANVAS_H / 2 - TOP_MARGIN - (r + 0.5) * cell_h



            # Calling the draw_house_centered function
            draw_house_centered(cx, cy, size_key, theme_key, roof_style,)

            # Calling the draw_tree_near function
            draw_tree_near(cx, cy, size_key)
        print()

    # Drawing a sun if user answers "y"
    if sun_flag == 'y':
        # Setting the size and center of circle
        r = 35
        cx = CANVAS_W / 2 - r - 20
        cy = CANVAS_H / 2 - r - 20
        # Calling fill_circle_center to draw the sun
        fill_circle_center(cx, cy, r, "yellow")


def main():
    """ The main function asks the user for input and calls the draw_village function"""
    print("Welcome to Turtle Village — Lite!")
    cols = ask_choice_int("How many houses per row?", [2, 3])
    rows = ask_choice_int("How many rows?", [2])
    size_key = ask_choice_str("House size", ["S","M","L"]).lower()
    theme_key = ask_choice_str("Color theme", ["pastel","primary"]).lower()
    roof_style = ask_choice_str("Roof type", ["triangle","flat"]).lower()
    sun_flag = ask_choice_str("Draw a sun?", ["y","n"]).lower()

    # window
    T.setup(CANVAS_W, CANVAS_H); T.speed(0); T.tracer(False)

    # Setting the size of the property
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows


    # Calling the draw village function with inputs
    draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style)
    # Finalizing
    T.tracer(True); T.hideturtle(); T.done()

if __name__ == "__main__":
    main()
