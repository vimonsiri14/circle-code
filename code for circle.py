import turtle

pen = turtle.Turtle()
turtle.title('Vimonsiri Window')
pen.pencolor('black')
pen.pensize(5)

pen.fillcolor('green')
pen.begin_fill()
pen.circle(100)
pen.end_fill()

pen.penup()
pen.goto(-200,-100)

pen.down()
pen.fillcolor('blue')
pen.begin_fill()
pen.circle(100)
pen.end_fill()

pen.penup()
pen.goto(200,-100)

pen.pendown()
pen.fillcolor('red')
pen.begin_fill()
pen.circle(100)
pen.end_fill()

pen.penup()
pen.goto(0,-300)

pen.write('vimonsiri',move = True, align = 'center',
          font = ('chiller', 90, 'normal'))


turtle.done()


