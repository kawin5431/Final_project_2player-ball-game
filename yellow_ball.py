import turtle
import random

class YellowBall:
    def __init__(self, boundary_width, boundary_height, spawn_area):
        self.radius = 20  # Increased size of the yellow ball
        self.color = "yellow"
        self.boundary_width = boundary_width
        self.boundary_height = boundary_height
        self.spawn_area = spawn_area  # (x_min, x_max, y_min, y_max)
        self.x = 0
        self.y = 0
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.shape("IMG_3329-removebg-preview.gif")
        self.turtle.shapesize(stretch_wid=self.radius/10, stretch_len=self.radius/10)
        self.turtle.hideturtle()
        self.turtle.pensize(0)  # Remove any outline or pen size

    def spawn(self):
        """Randomly spawn the yellow ball within the spawn area."""
        x_min, x_max, y_min, y_max = self.spawn_area
        self.x = random.randint(x_min, x_max)
        self.y = random.randint(y_min, y_max)
        self.turtle.goto(self.x, self.y)
        self.turtle.showturtle()

    def hide(self):
        """Hide the yellow ball."""
        self.turtle.hideturtle()
        self.x, self.y = None, None
