#ticTacToe1.py

#TTT 설명
print("TicTacToe게임을 소개합니다.")
print("3x3칸에 1줄을 먼저 만드는 사람이 승리합니다.")
print("아래의 표는 돌의 위치를 숫자로 표현 한 것 입니다.")
print("---------")
print("|", 7, 8, 9, "|")
print("|", 4, 5, 6, "|")
print("|", 1, 2, 3, "|")
print("---------")

#TTT반복 트리거 0:반복 1:끝
endGame = False 
#전적 기록 생성(list)
matchHistory = []

#TTT시작
while endGame == False:
    print("게임을 시작합니다.")
    #승자 선별
    winner = False
    #돌의 개수
    numOfStone = 0
    #돌 생성
    stone = 'o'
    #TTT판 생성
    board = ['-'] * 10
    #현재 상황
    print("---------")
    print("|", board[7], board[8], board[9], "|")
    print("|", board[4], board[5], board[6], "|")
    print("|", board[1], board[2], board[3], "|")
    print("---------")
    
    #돌 나두기(게임 끝날 때까지)
    while winner == False:
        #   돌 나두기 안내
        print("원하는 위치에 돌을 나둬주세요")
        #   돌 위치 입력 데이터 선별
        while True:
            inData = input()
            #   입력 데이터 타입 선별
            while not len(inData) == 1 or not "1" <= inData <= "9":
                print("한 자릿수 숫자를 입력해주세요")
                inData = input()
            #   정수로 변환
            LoS = int(inData)
            #   중복 배치 판단
            if board[LoS] == '-':
                break
            else:
                print("빈 자리에 배치해주세요")
        #   돌 배치
        board[LoS] = stone
        #   현재상황
            ##def## stoneChart()
        print("\n---------")
        print("|", board[7], board[8], board[9], "|")
        print("|", board[4], board[5], board[6], "|")
        print("|", board[1], board[2], board[3], "|")
        print("---------")
    
        #승리 조건 검사 / 승리시 게임 끝
        for i in [1, 4, 7]:
            if board[i] == stone and board[i+1] == stone and board[i+2] == stone:
                winner = True #승자 등장!
                
        for i in [1, 2, 3]:
            if board[i] == stone and board[i+3] == stone and board[i+6] == stone:
                winner = True
    
        if board[1] == stone and board[5] == stone and board[9] == stone:
                winner = True
    
        if board[7] == stone and board[5] == stone and board[3] == stone:
                winner = True
    
        ##def## 승자 등장 후 결과 저장 및 출력
        if winner == True:
            print("%s님의 승리." %stone)
            matchHistory.append(stone)
            oWin = matchHistory.count('o')
            xWin = matchHistory.count('x')
            draw = matchHistory.count('-')
            print("o:%s승, x:%s승, 무승부:%s회" % (oWin, xWin, draw))
    
        #돌의 개수 세기
        numOfStone += 1
        
        #9개의 돌을 다 놨을 때
        if numOfStone == 9 and winner == False:
            ##def## 무승부 저장 후 결과 출력
            print("비겼습니다.")
            matchHistory.append('-')
            oWin = matchHistory.count('o')
            xWin = matchHistory.count('x')
            draw = matchHistory.count('-')
            print("o:%s승, x:%s승, 무승부:%s회"  % (oWin, xWin, draw))
            winner = True #승자가 있는건 아니지만 일단 게임은 끝내야지...
            break
    
    ##def## reGame?
        while winner == True:
            print("한 번 더 하시겠습니까?(y/n)")
            reGame = input()
            if reGame == 'y' or reGame == 'Y':
                break
            elif reGame == 'n' or reGame == 'N':
                print("플레이 해주셔서 감사합니다.")
                endGame = True
                break
            else:
                print("\ny 또는 n을 입력해주세요.")
    
        #돌 변경(x=o, o=x)
        if stone == 'o':
            stone = 'x'
        else:
            stone = 'o'




'''
vs 컴퓨터 만들기 
'''

'''
승리 조건 검사하는 도중에 승리가 확정되면 축하 멘트를 넣어야했다.
그러면 가로로 승리 세로로 승리를 검토하는 명령마다 축하 멘트를 넣어야해서 완전히 똑같은 축하멘트를 4번이나 복사 붙어넣기를 해야하는 상황이 되었다.
축하 멘트를 함수로 만들어서 4번 넣는 글자수를 줄여 보기 좋게라고 만들까 라고 생각했다. 하지만 함수는 아직 익숙치 않았다. 매개변수와 인수를 관리하는 것을 못해서 최대한 함수 없이 만들어 보자고 생각했다.
축하멘트를 반복문 밖으로 빼버리고 승리했다는 것을 알려주는 변수를 지정하고 그 변수가 True일때 축하멘트를 넣는 조건문은 만들어서 밖에 빼두었다.
그렇게 해서 쓸때없는 반복멘트를 없앨 수 있었다.
~안의 ~안의 함수 같은 끝도없이 중첩되려는 함수형태에 써먹으면 좋을 것 같다는 생각을 했다.
'''
