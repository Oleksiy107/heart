import turtle

# Creating a turtle object (pen)
pen = turtle.Turtle()

# Defining a method to draw the curve of the heart
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

# Defining a method to draw a full heart
def heart():
    # Set the fill color to red
    pen.fillcolor('red')

    # Start filling the color
    pen.begin_fill()

    # Draw the left line
    pen.left(140)
    pen.forward(113)

    # Draw the left curve
    curve()
    pen.left(120)

    # Draw the right curve
    curve()

    # Draw the right line
    pen.forward(112)

    # End filling the color
    pen.end_fill()

# Defining a method to display a message inside or below the heart
def txt():
    # Move turtle to the air (to avoid drawing a line)
    pen.up()

    # Set position where the message will be written (below the heart)
    pen.setpos(-0, 95)

    # Move the turtle to the ground (ready to write)
    pen.down()

    # Set the text color to lightgreen
    pen.color('lightgreen')

    # Write the message in a specified font style and size
    pen.write("З Днем святого Валентина", align="center", font=("Verdana", 12, "bold"))

# Defining a method to display a longer message below the heart
def txt2():
    # Move turtle to the air
    pen.up()

    # Set initial position for the first line of text (below the heart)
    pen.setpos(-70, 280)

    # Move the turtle to the ground
    pen.down()

    # Set the text color to lightgreen
    pen.color('lightgreen')

    # Write the first line of text
    pen.write("Кохана, ти – найдорожча людина у моєму житті.", align="left", font=("Verdana", 10, "bold"))

    # Move to the next line
    pen.up()
    pen.setpos(-70, 260)
    pen.down()

    # Write the second line of text
    pen.write("Кожен день поруч із тобою робить мене щасливішим.", align="left", font=("Verdana", 10, "bold"))

    # Move to the next line
    pen.up()
    pen.setpos(-70, 240)
    pen.down()

    # Write the third line of text
    pen.write("Ти моя ніжність, моя підтримка і моє натхнення.", align="left", font=("Verdana", 10, "bold"))

    # Move to the next line
    pen.up()
    pen.setpos(-70, 220)
    pen.down()

    # Write the fourth line of text
    pen.write("Я вдячний долі за тебе і хочу, щоб ти завжди усміхалася.", align="left", font=("Verdana", 10, "bold"))

    # Move to the next line
    pen.up()
    pen.setpos(-70, 200)
    pen.down()

    # Write the fifth line of text
    pen.write("З Днем святого Валентина, моя любов!", align="left", font=("Verdana", 10, "bold"))

# Drawing the heart
heart()

# Writing text inside the heart
txt()

# Writing a longer message below the heart
txt2()

# Hide the turtle
pen.ht()

# Keep the window open
turtle.done()
