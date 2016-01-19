from random import randrange

'''Based on an entry in ‘Graphic Design Manual’, by Armin Hofmann (see p. 57)'''

# Name
SERIES_NAME = "6_Shapes"

# Target Size
PAPER_SIZE = "A4"

# Number of Shapes on Page
xShapes = 2
yShapes = 3

# Margin between Shapes
MARGIN_x = 12
MARGIN_y = 18

# Origin (lower left)
ORIGIN_x = 32
ORIGIN_y = 32

# Number of Squares in Shape
NUM_CASES = 3

# Dimension of Squares in Shape
SIDE = 24

WIDTH = xShapes * (NUM_CASES * SIDE + MARGIN_x) + ORIGIN_x
HEIGHT = yShapes * (NUM_CASES * SIDE + MARGIN_y) + ORIGIN_y

print "Width: ",
print WIDTH
print "Height: ",
print HEIGHT

# draw line of squares in shape, rows in shape, shapes in row

def draw_shape_row(ORIGIN_x, ORIGIN_y, SIDE):
    for a in range(NUM_CASES):
        col = randrange(0,2)
        cmykFill(col,col,col,col)
        rect(ORIGIN_x + SIDE * a, ORIGIN_y, SIDE, SIDE)
  
def draw_shape(ORIGIN_x, ORIGIN_y, SIDE):
    for b in range(NUM_CASES):
        draw_shape_row(ORIGIN_x, ORIGIN_y + b * SIDE, SIDE)

def draw_row_of_shapes(ORIGIN_x, ORIGIN_y, SIDE):
    for c in range(xShapes):
        draw_shape(ORIGIN_x, ORIGIN_y, SIDE)
        # move one column in
        ORIGIN_x += SIDE * NUM_CASES + MARGIN_x

def draw_multiple_rows_of_shapes(ORIGIN_x, ORIGIN_y, SIDE):
    for d in range(yShapes):       
        draw_row_of_shapes(ORIGIN_x, ORIGIN_y, SIDE)
        # move one row up
        ORIGIN_y += SIDE * NUM_CASES + MARGIN_y

newPage(PAPER_SIZE)

'''
# Test
draw_multiple_rows_of_shapes(ORIGIN_x, ORIGIN_y, SIDE)
'''

# Production
for foo in range(1,11):
    draw_multiple_rows_of_shapes(ORIGIN_x, ORIGIN_y, SIDE)
    saveImage(["~/Desktop/" + SERIES_NAME + "_" + PAPER_SIZE + "_" + str(foo) + ".pdf"])