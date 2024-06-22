import random

#答えの生成
def generator():
    answer = []
    while len(answer) < 3:
        rand = random.randint(0, 9)
        if rand in answer:
            pass
        else:
            answer += [rand]
    return answer

def check(guess, answer):
    hit = 0
    blow = 0
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            hit += 1
        else:
            if guess[i] in answer:
                blow += 1
    return [hit, blow]

def main():
    #答えの生成
    answer = random.randint(100, 999)

    max_count = 10
    for i in range(1, max_count + 1):
        print('３桁の数字を入力してください')
        num = int(input())
        if num == answer:
            print('正解です！おめでとうございます！')
            break




if __name__ == '__main__':
    main()