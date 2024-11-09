import turtle
import random
class Polygon():
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size
    

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()


    def get_new_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    
class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, border_size, level, reduction_ratio):
        super().__init__(num_sides, size, orientation, location, color, border_size)
        self.level = level
        self.reduction_ratio = reduction_ratio

    def reposition(self):
        turtle.penup()
        turtle.forward(self.size * (1 - self.reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.size * (1 - self.reduction_ratio)/2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]

        self.size *= self.reduction_ratio

    def draw_another_polygon(self):
        while self.level > 0:
            super().draw_polygon()
            self.size = self.size * self.reduction_ratio
            self.location[0] += self.size * (1 - self.reduction_ratio) / 2
            self.location[1] += self.size * (1 - self.reduction_ratio) / 2

            super().draw_polygon()
            self.level -= 1

class Run:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
    
    def run_turtle(self):
        select = int(input('Which art do you want to generate? Enter a number between 1 to 9 inclusive: '))
        for i in range(30):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = Polygon.get_new_color()
            border_size = random.randint(1, 10)
            reduction_ratio = 0.618
            num_levels = 2

            if select == 1:
                num_sides = random.randint(3,3)
                polygon = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon.draw_polygon()
            elif select == 2:
                num_sides = random.randint(4,4)
                polygon = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon.draw_polygon()
            elif select == 3:
                num_sides = random.randint(5,5)
                polygon = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon.draw_polygon()
            elif select == 4:
                num_sides = random.randint(3,5)
                polygon = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon.draw_polygon()
            elif select == 5:
                num_sides = random.randint(3,3)
                polygon = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio)
                polygon.draw_another_polygon()
            elif select == 6:
                num_sides = random.randint(4,4)
                polygon = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio)
                polygon.draw_another_polygon()
            elif select == 7:
                num_sides = random.randint(5,5)
                polygon = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio)
                polygon.draw_another_polygon()
            elif select == 8:
                num_sides = random.randint(3,5)
                polygon = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio)
                polygon.draw_another_polygon()
            elif select == 9:
                num_sides = random.randint(3,5)
                embedded = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio)
                embedded.draw_another_polygon()
                polygon = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon.draw_polygon()
        
        turtle.done()

if __name__ == "__main__":
    app = Run()
    app.run_turtle()
