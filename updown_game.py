from random import *

nick = []   #닉네임을 담을 리스트 생성
score = []   #기록을 담을 리스트 생성

def fileRead() :
    try:   #파일 없는 오류 처리하기 위해 try, except문 씀
        fr = open("updownScore.txt", 'r')   #점수 파일 불러오기
        lines = fr.readlines()   #파일을 한 줄씩 읽음

        for i in lines :
            nickScore = i.split(":")  #파일 한줄씩 받아와서 :기준으로 앞,뒤 나눠서 nickScore 리스트에 넣음
            nick.append(nickScore[0])   #":'기준으로 앞은 닉네임 리스트에
            score.append(int(nickScore[1].strip('\n')))   #뒤는 점수 리스트에 넣음, strip함수로 뒤에 따라오는 개행문자 제거
        
        fr.close()   #연 파일 닫기
    
    except FileNotFoundError:   #파일 없으면(예외처리)
        newf = open("updownScore.txt", 'w')    #파일 생성(내용은 없음)
        newf.close()


fileRead()

while True :
    rightAnswer = randint(1, 100)   #범위가 1에서 100인 랜덤 정수값 생성
    print(rightAnswer)   #코드 확인을 위해 답 출력
    minimum = 1   #숫자 범위
    maximum = 100

    print("UP & DOWN 게임에 오신걸 환영합니다~")
    menu = input("1. 게임시작 2. 기록확인 3. 게임종료\n>>")


    if menu == "1" :
        game = 0 #총 게임 수
        while game<10 :   #10번 반복
            print("%d번째 숫자 입력(%d~%d) : " % ((game + 1), minimum, maximum), end = '')
            a = input()

            if a == '' :
                print("값이 입력되지 않았습니다. 다시 입력해주세요.")

            else :
                answer = int(a)
                if answer == rightAnswer :   #만약 정답이면 for문 탈출
                    game = game + 1
                    break

                elif answer < rightAnswer : 
                    print("UP")
                    if answer >= minimum :   #만약 범위가 50~100인데 25를 입력한 경우 최소 범위값은 그대로 유지
                        minimum = answer + 1    #답보다 작으면 UP출력 후 답 범위 중 작은 값을 입력값으로 바꿈
                        game = game + 1   
                    else :
                        print("범위보다 작은 숫자를 입력하셨습니다. 다시 입력해주세요.")   ##피드백2. 범위 밖 숫자 입력시 다시 입력하라는 문장, 게임 카운트 안함.
                        
                else :                      
                    print("DOWN")
                    if answer <= maximum :
                        maximum = answer - 1        #답보다 크면 DOWN출력 후 답 범위 중 큰 값을 입력값으로 바꿈
                        game = game + 1
                    else :
                        print("범위보다 큰 숫자를 입력하셨습니다. 다시 입력해주세요.")

        if game == 10 :
            print("입력횟수를 초과하였습니다. 게임오버!")
        else :
            print("정답입니다!!")
            print("%d번째만에 맞추셨습니다." % (game))

            if len(score) == 0 or game < score[0] :
                    print("최고기록 갱신~!\n")
                    nickname = input("닉네임을 입력하세요 >> ")
                    nick.insert(0, nickname)    #이번 판 기록을 nick에 추가
                    score.insert(0, game)  #이번 판 기록을 score에 추가 ##피드백1. 갱신된 점수 맨 앞으로 오게함(순위) ##피드백3. 최고 기록만 입력

    elif menu == "2" :    #기록 출력
        if len(nick) == 0 :
            print("기록이 없습니다.")

        else :
            for i in range(0, len(nick)) :
                print(i+1, nick[i], score[i])   #순위, 닉네임, 점수 출력
                
    elif menu == "3" :
        print("게임을 종료합니다.")
        fw = open("updownScore.txt", 'w')   #점수 기록을 위해 파일 불러옴, 순위를 뒤에 붙이는 것이 아닌 덮어쓰는 것이기 때문에 옵션 a가 아닌 w를 씀
        for i in range(0, len(nick)) :   #닉네임 갯수만큼 for문 실행
            fw.write("%s:%d" % (nick[i], score[i]))   #닉네임:점수 형식으로 파일에 씀
            fw.write("\n")   #개행문자 입력
        fw.close()   #연 파일 닫기
        break
    
    else :
        print("메뉴를 잘못 입력하셨습니다. 다시 입력해주세요.")




