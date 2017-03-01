import turtle 

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    pointer = turtle.Turtle()
    pointer.shape("turtle")
    pointer.color("yellow")
    pointer.speed(2)
    for i in range(1,37):
        draw_square(pointer)
        pointer.right(10)
        
    
    window.exitonclick()

draw_art()
