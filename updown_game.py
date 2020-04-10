from random import *

score = []   #기록을 담을 리스트 생성

while True :
    rightAnswer = randint(1, 100)   #범위가 1에서 100인 랜덤 정수값 생성
    print(rightAnswer)   #코드 확인을 위해 답 출력
    minimum = 1   #숫자 범위
    maximum = 100

    print("UP & DOWN 게임에 오신걸 환영합니다~")
    menu = input("1. 게임시작 2. 기록확인 3. 게임종료\n>>")

    if menu == "1" :
        for game in range(0, 10) :   #10번 반복
            print("%d번째 숫자 입력(%d~%d) : " % ((game + 1), minimum, maximum), end = '')
            answer = int(input())
            game = game + 1

            if answer == rightAnswer :   #만약 정답이면 for문 탈출
                break
            elif answer < rightAnswer : 
                print("UP")
                if answer > minimum :   #만약 범위가 50~100인데 25를 입력한 경우 최소 범위값은 그대로 유지
                    minimum = answer    #답보다 작으면 UP출력 후 답 범위 중 작은 값을 입력값으로 바꿈
            else :                      
                print("DOWN")
                if answer < maximum :
                    maximum = answer        #답보다 크면 DOWN출력 후 답 범위 중 큰 값을 입력값으로 바꿈

        if game == 10 :
            print("입력횟수를 초과하였습니다. 게임오버!")
        else :
            print("정답입니다!!")
            print("%d번째만에 맞추셨습니다." % (game))

            for i in score :    #이전 기록과 비교해서 작으면 최고기록
                if game < i :
                    print("최고기록 갱신~!")
                    break

            score.append(game)  #이번 판 기록을 score에 추가  

    elif menu == "2" :    #기록 출력
        n = 1
        for i in score :
            print(n, i)
            n += 1
            
    elif menu == "3" :
        print("게임을 종료합니다.")
        break
    
    else :
        print("메뉴를 잘못 입력하셨습니다. 다시 입력해주세요.")




