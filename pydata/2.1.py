import turtle
import time
import random

delay = 0.1

# 创建窗口屏幕
window = turtle.Screen()
window.title("贪吃蛇游戏")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# 创建蛇头
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# 创建食物
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# 移动函数
def move():
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "Down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "Left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "Right":
        x = head.xcor()
        head.setx(x + 20)

# 移动方向函数
def go_up():
    if head.direction != "Down":
        head.direction = "Up"

def go_down():
    if head.direction != "Up":
        head.direction = "Down"

def go_left():
    if head.direction != "Right":
        head.direction = "Left"

def go_right():
    if head.direction != "Left":
        head.direction = "Right"

# 键盘绑定
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

# 主游戏循环
while True:
    window.update()

    # 碰撞检测
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

    # 吃食物
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # 移动身体
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # 碰撞身体检测
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

    time.sleep(delay)

window.mainloop()