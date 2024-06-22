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

#hit&blowの確認
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
    print('ゲームスタート')
    answer = generator()
    max_count = 10
    count = 0
    while count < max_count:
        count += 1
        num = input('３桁の数字を入力してください')
        guess = [int(num[i]) for i in range(len(num))]
        [hit, blow] = check(guess, answer)
        print("{}: {} Hit, {} Blow".format(num, hit, blow))
        if hit == len(answer):
            print('正解です！おめでとうございます！')
            break
    if count == max_count:
        print('残念...正解は{}でした'.format(answer))

if __name__ == '__main__':
    main()