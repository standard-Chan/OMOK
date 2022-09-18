# 디자인

import pygame
import numpy as np


# 게임 디자인 설정
class Board():
    def __init__(self):
        # 바둑판
        self.x = 50
        self.y = 50
        self.width = 2
        self.size = 20*19
        self.b_color = (240,230,180) # board_color
        self.board_list = []
        #격자
        self.grid_size = 20
        self.grid_color = (0,0,0)
    
    def drawgrid (self, start_pos_list, end_pos_list, color, width):
        pygame.draw.line(screen, color, start_pos_list, end_pos_list, width)
        return 0;
    
    def newBoardList (self): # 데이터 오목판 리스트 생성
        for i in range(19):
            temp_list = []
            for j in range(19):
                temp_list.append(0)
            self.board_list.append(temp_list[:])
            
    
    
# 배경 디자인
class Design():
    def __init__(self):
        self.screen_color = (255,255,255)
        self.screen_size = (700,600)

        
# 흑돌 백돌
class Ball():
    def __init__(self):
        self.black = {'color':(0,0,0), 'num':1, 'pos':[], 'boardPos':[], 'count':0}
        self.white = {'color':(255,255,255), 'num':2, 'pos':[], 'boardPos':[], 'count':0}
        self.size = 7
    
    def draw(self, position, turn): #turn은 흑돌 백돌 순서
        if turn%2 == 0:
            pygame.draw.circle(screen, self.black['color'], position, self.size)
        if turn%2 == 1:
            pygame.draw.circle(screen, self.white['color'], position, self.size)
        
        
class GameRule():
    pass

class GamePlay():
    def __init__(self):
        pass
    def ballPos_to_boardList(self, ball_pos, board):  # 착수 위치 리스트 인덱스로 반환
        ball_list_pos_x = (ball_pos[0] - board.x)//20
        ball_list_pos_y = (ball_pos[1] - board.y)//20
        ball_boardList_pos = (ball_list_pos_x, ball_list_pos_y)
        return ball_boardList_pos

    def placeBall (self, ball, turn, position):
        if turn%2 == 0:
            if  : # 3 3일때
                print('3 3 이므로 놓을 수 없습니다.')
            elif:
                ball.black['pos'].append(ball_fit_pos (pygame.mouse.get_pos(), board, ball)) # 화면상 좌표
                ball.black['boardPos'].append((gameplay.ballPos_to_boardList(ball_fit_pos (pygame.mouse.get_pos(), board, ball), board))) # 데이터 배열 상 좌표
                board.board_list[ball.black['boardPos'][turn//2][1]][ball.black['boardPos'][turn//2][0]] = ball.black['num'] # board_list에 돌 데이터 입력
        elif turn%2 == 1:
            ball.white['pos'].append(ball_fit_pos (pygame.mouse.get_pos(), board, ball))
            ball.white['boardPos'].append(gameplay.ballPos_to_boardList(ball_fit_pos (pygame.mouse.get_pos(), board, ball), board))
            board.board_list[ball.white['boardPos'][turn//2][1]][ball.white['boardPos'][turn//2][0]] = ball.white['num']
        return 0
    
    def checkBall (self, board, ball):
        for row in range(19):
            ball.black[count]=0
            ball.white[count]=0
            for column in range(19):
                board_data = board.board_list[row][column]
                if board_data == 1:
                    ball.black[count]+=1
                elif board_data == 2:
                    ball.white[count]+=1
                else:
                    ball.black[count]=0
                    ball.white[count]=0
                if ball.black[count] == 5 or ball.white[count] == 5:
                    return print(종료)
        if or : # 가로 5개
        elif or : # 세로 5개
        elif or : # 기울기 + 5개
        elif or : # 기울기 - 5개
    
# 화면 그리기
def draw_screen (screen, design, board, ball, turn):
    screen.fill(design.screen_color)     #화면 색상 변환
    
      #바둑판
    pygame.draw.rect(screen, board.grid_color,[board.x, board.y, board.size, board.size], board.width)
    pygame.draw.rect(screen, board.b_color,[board.x+(board.width*0.5), board.y+(board.width*0.5), board.size-(board.width), board.size-(board.width)])
    
    # 격자
    for vertical_line in range(1,20): # 세로줄
        line_x = board.x + vertical_line*board.grid_size
        board.drawgrid([line_x, board.y], [line_x, board.y+board.size-(board.width*0.5)], board.grid_color, 1)
    for horizontal_line in range(1,20): # 가로줄
        line_y = board.y + horizontal_line * board.grid_size
        board.drawgrid([board.x, line_y], [board.x+board.size-(board.width*0.5), line_y], board.grid_color, 1)
        
   # 바둑알
    for position in ball.black['pos']:
        ball.draw(position, 0)
    for position in ball.white['pos']:
        ball.draw(position, 1)
    
    
# 착수 위치 조정
def ball_fit_pos (position, board, ball):
    x=0; y=0; count=0;
    x_temp = position[0] - board.x
    y_temp = position[1] - board.y

    # 격자 오른쪽 클릭
    if x_temp % board.grid_size <= ball.size:
        x_temp = x_temp//board.grid_size
        if (y_temp) % board.grid_size <= ball.size:
            y_temp = y_temp//board.grid_size
        elif (y_temp) % board.grid_size >= board.grid_size - ball.size:
            y_temp = y_temp//board.grid_size + 1
        else:
            count=1
        x = x_temp*board.grid_size + board.x
        y = y_temp*board.grid_size + board.y
        
    # 격자 왼쪽 클릭
    elif (x_temp) % board.grid_size >= board.grid_size-ball.size:
        x_temp = x_temp//board.grid_size + 1
        if (y_temp) % board.grid_size <= ball.size:
            y_temp = y_temp//board.grid_size
        elif (y_temp) % board.grid_size >= board.grid_size-ball.size:
            y_temp = y_temp//board.grid_size + 1
        else:
            count=1
        x = x_temp*board.grid_size + board.x
        y = y_temp*board.grid_size + board.y
        
    else :
        count =1

    if count == 1:
        print('정확한 위치에 다시 놓아주세요.')
        return 0
        
    return (x,y)

board = Board(); board.newBoardList()
design = Design()
ball = Ball()
gameplay = GamePlay()


turn = 0
### pygame 설정 ----------

#초기화
pygame.init()

# 화면설정
screen = pygame.display.set_mode(design.screen_size)   # 화면 설정 SCREEN
pygame.display.set_caption("OMOK")    # 타이틀바 텍스트 설정

# 실행
running = True

while running :

    draw_screen(screen, design, board, ball, turn)
                
                
    # event
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: # 클릭 event
            if ball_fit_pos (pygame.mouse.get_pos(), board, ball) in ball.black['pos'] or ball_fit_pos (pygame.mouse.get_pos(), board, ball) in ball.white['pos']: # 기존에 착수된 위치에 놓을 시
                print('이미 착수된 위치')
                continue
            elif ball_fit_pos(pygame.mouse.get_pos(), board, ball) == 0:  # 
                print('정확한 위치에 다시 놓아주세요.')
                continue
            gameplay.placeBall(ball, turn, pygame.mouse.get_pos()) # 착수
            turn += 1
            print(np.array(board.board_list))
            
        
            
            
        if event.type == pygame.QUIT: # X표 클릭
            running = False        
     
    pygame.display.flip() # show()


pygame.quit()
