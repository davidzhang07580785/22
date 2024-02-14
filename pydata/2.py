import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("猜一个1到100之间的数字: "))
        attempts += 1

        if guess < number:
            print("太小了，请再试一次！")
        elif guess > number:
            print("太大了，请再试一次！")
        else:
            print("恭喜你，猜对了！")
            print("你用了", attempts, "次猜对了。")
            break

guess_number()