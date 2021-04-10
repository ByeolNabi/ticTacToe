#ticTacToeFail.py

#변수 관리가 너무 어려워...

#def 입력한 데이터가 올바른지 확인
def LoSJudge():
    global LoS
    while True:
        inData = input("돌을 놓을 숫자를 입력하세요\n")    
        
        if len(inData) == 1 and '1' <= inData <= '9':  
            LoS = int(inData)
            if board[LoS] != '-':
                print("돌이 없는 곳을 선택해 주세요")
            else:
                break
            #돌 위치 Location of Stone
        else:
            print("\n1~9까지의 숫자를 입력해주세요")
                #입력된 데이터 선별 반복
        board[LoS] = stone
            
#def 승리 조건을 달성한 플레이어가 있는지 확인하기
def winnerJudge(stone):
    for i in [1, 4, 7]:
        if board[i] == stone and board[i+1] == stone and board[i+2] == stone:
            print("%s님의 승리." %stone)
            return True
            
    for i in [1, 2, 3]:
        if board[i] == stone and board[i+3] == stone and board[i+6] == stone:
            print("%s님의 승리." %stone)
            return True
        
    if board[1] == stone and board[5] == stone and board[9] == stone:
        print("%s님의 승리." %stone)
        return True

    if board[7] == stone and board[5] == stone and board[3] == stone:
        print("%s님의 승리." %stone)
        return True

#def 틱택토 한 판
def ticTacToe():

    #ttt 틀
    board = ['-'] * 10

    print("---------")
    print("|", board[7], board[8], board[9], "|")
    print("|", board[4], board[5], board[6], "|")
    print("|", board[1], board[2], board[3], "|")
    print("---------") 



    #돌 나두기 그후 돌 종류 변경 + 반복
    stone = 'o'
    numOfTurn = 0
    win = False

    while numOfTurn < 9 and win == False:
        
        LoSJudge()##돌 놓기 입력, 위치 판단
        
        numOfTurn = numOfTurn + 1
        
        print("%d번째 돌" % numOfTurn)
        
        print("---------")
        print("|", board[7], board[8], board[9], "|")
        print("|", board[4], board[5], board[6], "|")
        print("|", board[1], board[2], board[3], "|")
        print("---------\n")#현재상황판
        
        win = winnerJudge(stone)
    while win == True:
        print("한 번 더 하시겠습니까?(y/n)")
        reGame = input()
        if reGame == "y":
            win = False
            ticTacToe()
            #틱택토 초기화
        
        elif reGame == "n":
            win = False
            #전적
        
        else:
            print("y 또는 n을 입력해 주세요\n")

            
        ##밑에 이거를 어디에 넣어야 잘 들어간걸까
    if stone == 'o':
        stone = 'x'
    else:
        stone = 'o'
            #다음에 두어야 할 돌 모양 변환 o면 x로, x면 o로

#시작 설명
print("TicTacToe게임을 소개합니다.")
print("3x3칸에 1줄을 먼저 만드는 사람이 승리합니다.")
print("아래의 표는 돌의 위치를 숫자로 표현 한 것 입니다.")
print("---------")
print("|", 7, 8, 9, "|")
print("|", 4, 5, 6, "|")
print("|", 1, 2, 3, "|")
print("---------")

ticTacToe()


'''
#게임 모드 선택
print("\n게임 모드를 선택합니다.")
print("[1] 1인모드 , [2] 2인모드")


#선택에 따른 분기
while True:
    gameMode = input("\n원하는 게임 모드의 숫자를 입력해주세요")

    if gameMode == "1":
        print("1인 모드를 시작합니다")
        #vs컴퓨터 프로그래밍
        
    elif gameMode == "2":
        print("2인 모드를 시작합니다.")
        #그냥 하면 됨

    else:
        print("숫자 1 또는 2를 입력해주세요")
'''
