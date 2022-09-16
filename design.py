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
    
class Design():
    def __init__(self):
        self.screen_color = (255,255,255)
        self.screen_size = (700,600)
    
    
    
board = Board()
design = Design()

    
    
### pygame 설정 ----------

#초기화
pygame.init()

# 화면설정
screen = pygame.display.set_mode(design.screen_size)   # 화면 설정 SCREEN
pygame.display.set_caption("OMOK")    # 타이틀바 텍스트 설정

# 실행
running = True

while running :
    screen.fill(design.screen_color)     #화면 색상 변환
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: # 클릭시 좌표 반환
            print(pygame.mouse.get_pos())
            
            
        if event.type == pygame.QUIT: # X표 누를 시 발생
            running = False
    
    #오목판
    pygame.draw.rect(screen,black,[board.x, board.y, board.size, board.size], board.width)
    pygame.draw.rect(screen, board.b_color,[board.x+(board.width*0.5), board.y+(board.width*0.5), board.size-(board.width), board.size-(board.width)])
    # 격자
    for vertical_line in range(1,20): # 세로줄
        line_x = board.x + vertical_line*board.grid_size
        board.drawgrid([line_x, board.y], [line_x, board.y+board.size-(board.width*0.5)], board.grid_color, 1)
    for horizontal_line in range(1,20): # 가로줄
        line_y = board.y + horizontal_line * board.grid_size
        board.drawgrid([board.x, line_y], [board.x+board.size-(board.width*0.5), line_y], board.grid_color, 1)
        
     
    

    pygame.display.flip() # show()


pygame.quit()
