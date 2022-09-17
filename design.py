import pygame

# 게임 디자인 설정
class Board():
    def __init__(self):
        # 바둑판
        self.x = 50
        self.y = 50
        self.width = 2
        self.size = 20*19
        self.b_color = (240,230,180) # board_color
        #격자
        self.grid_size = 20
        self.grid_color = (0,0,0)
    
    def drawgrid (self, start_pos_list, end_pos_list, color, width):
        pygame.draw.line(screen, color, start_pos_list, end_pos_list, width)
        return 0;
    
    
# 배경 디자인
class Design():
    def __init__(self):
        self.screen_color = (255,255,255)
        self.screen_size = (700,600)

        
# 흑돌 백돌
class Ball():
    def __init__(self):
        self.black = {'color':(0,0,0), 'num':0, 'pos':[]}
        self.white = {'color':(255,255,255), 'num':1, 'pos':[]}
        self.size = 7
    
    def draw(self, position, turn): #turn은 흑돌 백돌 순서
        if turn%2 == 0:
            pygame.draw.circle(screen, self.black['color'], position, self.size)
        if turn%2 == 1:
            pygame.draw.circle(screen, self.white['color'], position, self.size)
        
    
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
    return (x,y)


board = Board()
design = Design()
ball = Ball()
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
                print('착수된 위치')
                continue
            elif turn%2 == 0:
                ball.black['pos'].append(ball_fit_pos (pygame.mouse.get_pos(), board, ball))
            else:
                ball.white['pos'].append(ball_fit_pos (pygame.mouse.get_pos(), board, ball))
            turn += 1
            
            
        if event.type == pygame.QUIT: # X표 클릭
            running = False        
     
    pygame.display.flip() # show()


pygame.quit()
