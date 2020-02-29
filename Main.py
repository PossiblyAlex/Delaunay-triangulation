import tkinter as tk


print("Program is running...")
root = tk.Tk()
canvas = tk.Canvas(root, width=1045, height=554, bg="white")
canvas.pack()

points = []
adjMatrix = []


def add_point(point):
    points.append(point)

    for col in adjMatrix:
        col.append(0)

    tempCol = [0] * len(points)
    adjMatrix.append(tempCol)

    if len(points) > 1:
        adjMatrix[len(points)-2][len(points)-1] = 1

    for x in adjMatrix:
        print(x)


def left_click(event):
    print("Left")
    print(event.x)
    print(event.y)
    x = event.x
    y = event.y

    add_point((x,y))
    print(len(points))
    if len(points) > 2:
        print("todo")
    update()
    """print(points)"""

def update():
    for item in canvas.find_all():
        canvas.delete(item)

    r = 4
    for point in points:
        canvas.create_oval(point[0]-r, point[1]-r, point[0]+r, point[1]+r, fill="red")

    for i, col in enumerate(adjMatrix):
        for j, edge in enumerate(col):
            if edge == 1:
                canvas.create_line(points[i][0], points[i][1], points[j][0], points[j][1])

    canvas.pack()


canvas.bind("<Button-1>", left_click)

root.mainloop()
