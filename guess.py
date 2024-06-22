import random

def main():
    #答えの生成
    answer = random.randint(100, 999)

    guess()

def guess():
    max_count = 10
    for i in range(1, max_count + 1):
        print('３桁の数字を入力してください')
        num = int(input())


if __name__ == '__main__':
    main()