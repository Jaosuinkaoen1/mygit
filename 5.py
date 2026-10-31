"""中文命令行猜数字游戏，运行方式：python 5.py。"""

import random


def play_round():
    """进行一局游戏；猜中返回 True，主动退出返回 False。"""
    secret = random.randint(1, 100)
    attempts = 0
    print("\n我想好了一个 1～100 的整数，来猜猜看！")

    while True:
        answer = input("请输入数字（输入 q 退出）：").strip()
        if answer.lower() == "q":
            return False

        try:
            guess = int(answer)
        except ValueError:
            print("输入无效，请输入 1～100 的整数。本次不计次数。")
            continue

        if not 1 <= guess <= 100:
            print("数字超出范围，请输入 1～100 的整数。本次不计次数。")
            continue

        attempts += 1
        if guess > secret:
            print("猜大了，再小一点！")
        elif guess < secret:
            print("猜小了，再大一点！")
        else:
            print(f"恭喜猜中了！答案是 {secret}，你一共猜了 {attempts} 次。")
            return True


def wants_replay():
    """询问是否开始新一局，无效选项会重新询问。"""
    while True:
        answer = input("再玩一局吗？（y/是：继续，n/否/q：退出）：").strip().lower()
        if answer in ("y", "yes", "是"):
            return True
        if answer in ("n", "no", "否", "q"):
            return False
        print("请输入 y 或 n，也可以输入 q 退出。")


def main():
    print("欢迎玩猜数字！不限猜测次数，随时输入 q 或按 Ctrl+C 退出。")
    try:
        while play_round():
            if not wants_replay():
                break
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C 或终端输入结束时，友好退出，不显示异常堆栈。
        print()
    print("游戏结束，再见！")


if __name__ == "__main__":
    main()
