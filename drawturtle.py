import turtle
def draw_pic():
    window= turtle.Screen()
    window.bgcolor("red")
    
    brad=turtle.Turtle()
    turtle.shape("arrow")
    turtle.color("blue")
    turtle.speed(10.5)

    i=0
    item=0

    while i < 4:
      brad.forward(100)
      brad.right(90)
      i = i +1

    while item <37:
  
      brad.right(10)
      a=0
    
      while a < 4:
        brad.forward(100)
        brad.right(90)
        a = a +1
      item= item +1
    
  
    #angie=turtle.Turtle()
    #angie.shape("turtle")
    #angie.color("black")
    #angie.circle(100)

    #love=turtle.Turtle()
    #love.shape("turtle")
    #love.color("yellow")

    #for num in range(3):
      #love.forward(20)
      #love.right(120)


    window.exitonclick()
draw_pic()
    
