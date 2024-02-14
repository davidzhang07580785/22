import time

def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("你来到了一个神秘的森林。")
    print_pause("在你的左边有一座黑暗的洞穴。")
    print_pause("在你的右边有一条通往山顶的小径。")
    print_pause("请选择你要前往的方向。")

def choose_path():
    path = input("左边的洞穴（输入 '1'）还是右边的小径（输入 '2'）？")
    if path == '1':
        explore_cave()
    elif path == '2':
        climb_mountain()
    else:
        print_pause("请做出正确的选择。")
        choose_path()

def explore_cave():
    print_pause("你进入了黑暗的洞穴。")
    print_pause("洞穴里充满了各种声音和神秘的气息。")
    print_pause("你感到有点害怕，但你继续前进。")
    print_pause("突然，你看到了一只巨大的龙！")
    print_pause("你没有时间逃跑，龙向你喷出火焰。")
    print_pause("游戏结束！")
    play_again()

def climb_mountain():
    print_pause("你开始攀登陡峭的山顶小径。")
    print_pause("风越来越强，你需要小心前行。")
    print_pause("终于，你到达了山顶。")
    print_pause("你欣赏着壮丽的景色，感到非常满足。")
    print_pause("恭喜你，你成功完成了游戏！")
    play_again()

def play_again():
    choice = input("你想再次玩这个游戏吗？（输入 '是' 或 '否'）")
    if choice.lower() == '是':
        print_pause("好的！再来一次。")
        play_game()
    elif choice.lower() == '否':
        print_pause("谢谢你的游玩！再见。")
    else:
        print_pause("请做出正确的选择。")
        play_again()

def play_game():
    intro()
    choose_path()

play_game()