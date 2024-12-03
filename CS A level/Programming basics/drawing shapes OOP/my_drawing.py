from shapes import Triangle, Rectangle, Oval, Paper
rectl = Rectangle()
rectl.set_width(200)
rectl.set_height(200)
rectl.set_color("blue")

lerectl = Rectangle()
lerectl.set_x(100)
lerectl.set_y(100)
lerectl.set_width(50)
lerectl.set_height(150)
lerectl.set_color("yellow")

ovl = Oval()


rectl.draw()
lerectl.draw()
Paper.display()