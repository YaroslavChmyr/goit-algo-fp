import turtle

def draw_pifagor_tree(t, length, depth):
    if depth == 0:
        return
    t.forward(length)
    t.left(45)
    draw_pifagor_tree(t, length * 0.7, depth - 1)
    t.right(90)
    draw_pifagor_tree(t, length * 0.7, depth - 1)
    t.left(45)
    t.backward(length)

def main():
    depth = int(input("Введіть рівень рекурсії: "))
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(0, -250)
    turtle.left(90)
    turtle.pendown()
    draw_pifagor_tree(turtle, 150, depth)
    turtle.done()

if __name__ == "__main__":
    main()