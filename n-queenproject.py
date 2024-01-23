import pygame
pygame.init()

#setup thông số
clock=pygame.time.Clock()
WIDTH=600
ROW=4
speed=200
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#setup font
font1 = pygame.font.Font(None, 80)
font2 = pygame.font.Font(None, 70)
font3 = pygame.font.Font(None, 50)
font4 = pygame.font.Font(None, 40)
result_font=font1.render('RESULT', True,(255,255,255))
stimulate_font=font2.render('STIMULATE', True,(255,255,255))
setting_font=font2.render('SETTING', True,(255,255,255))
confirm_font=font4.render('Confirm', True,(255,255,255))
done_font=font4.render('Done', True,(255,255,255))
high_font=font4.render('HIGH', True,(255,255,255))
medium_font=font4.render('MEDIUM', True,(255,255,255))
slow_font=font4.render('SLOW', True,(255,255,255))

chat_bot='No Solution'
chat_bot_font=font2.render('Find Solution ....', True,(255,255,255))


#setup đồ họa
win=pygame.display.set_mode((1280,720))
pygame.display.set_caption('N-Queen Visualizer')

queen_img=pygame.image.load('queen.png')
queen_img=pygame.transform.scale(queen_img,(WIDTH//ROW,WIDTH//ROW))

background_img=pygame.image.load('background.png')
background_img=pygame.transform.scale(background_img,(1280,720))

setting_menu=pygame.image.load('setting_menu.png')
setting_menu=pygame.transform.scale(setting_menu,(537,296))

button_result_background=pygame.Rect(820,540,310,110)
button_result=pygame.Rect(825,545,300,100)

button_stimulate_background=pygame.Rect(820,400,310,110)
button_stimulate=pygame.Rect(825,405,300,100)

button_setting_background=pygame.Rect(820,260,310,110)
button_setting=pygame.Rect(825,265,300,100)

button_confirm_background=pygame.Rect(800,570,140,70)
button_confirm=pygame.Rect(805,575,130,60)

button_done_background = pygame.Rect(1000,570,140,70)
button_done = pygame.Rect(1005,575,130,60)

button_high_background=pygame.Rect(750,450,140,70)
button_high=pygame.Rect(755,455,130,60)

button_medium_background = pygame.Rect(925,450,140,70)
button_medium = pygame.Rect(930,455,130,60)

button_slow_background = pygame.Rect(1100,450,140,70)
button_slow = pygame.Rect(1105,455,130,60)

button_done_background2 = pygame.Rect(900,570,140,70)
button_done2 = pygame.Rect(905,575,130,60)

# định nghĩa cho một ô cờ
class Spot:
    def __init__(self,row,col,width,total_rows):
        self.row=row
        self.col=col
        self.x=row * width+30
        self.y=col * width+92
        self.total_rows=total_rows
        self.width=width
        if((row+col)%2==0):
            self.color=WHITE
        else:
            self.color=BLACK
    def get_pos(self):
        return self.row, self.col
    def is_closed(self):
        return self.color == RED
    def is_open(self):
        return self.color == GREEN
    def is_barrier(self):
        return self.color == YELLOW
    def is_checking(self):
        return self.color == BLUE
    def make_closed(self):
        self.color = RED
    def make_open(self):
        self.color = GREEN
    def make_barrier(self):
        self.color = YELLOW
    def make_checking(self):
        self.color = BLUE
    def make_reset(self,row,col):
        if((row+col)%2==0):
            self.color=WHITE
        else:
            self.color=BLACK
    def draw(self,win):
        if self.color == YELLOW:
            if((self.row+self.col)%2==0):
                pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, self.width))
            else:
                pygame.draw.rect(win, BLACK, (self.x, self.y, self.width, self.width))
            win.blit(queen_img,(self.x, self.y))
        else:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    def __lt__(self,other):
        return False
    
#thuật toán
def algorithm(grid):
    sol=solveNQUtil(lambda: draw(win, grid, ROW, WIDTH), grid, 0)
    if not sol:
        print("No Solution")
        return False
    else:
        print("Solution Found")
        return True
#kiểm tra quân hậu đặt đúng vị trí chưa
def isSafe(draw, grid, row, col):
    temp=grid[row][col].color
    grid[row][col].make_open()
    draw()
    # kiem tra ben trai
    for i in range(col):
        if grid[row][i].is_barrier():
            grid[row][i].make_closed()
            draw()
            grid[row][i].make_barrier()
            draw()
            for j in range(col):
                if j==i :
                    continue
                grid[row][j].make_reset(row,j)
                # draw()
            grid[row][col].make_reset(row,col)
            return False
        if not grid[row][i].is_open():
            grid[row][i].make_checking()
            draw()
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].is_checking():
                grid[i][j].make_reset(i,j)
                # draw()
  
    # kiểm tra đường chéo trái trên
    for i, j in zip(range(row, -1, -1), 
                    range(col, -1, -1)):
        if grid[i][j].is_barrier():
            grid[i][j].make_closed()
            draw()
            grid[i][j].make_barrier()
            draw()
            for i2, j2 in zip(range(row, -1, -1), 
                    range(col, -1, -1)):
                    if i2==i and j2==j:
                        continue
                    grid[i2][j2].make_reset(i2,j2)
                    #draw()
            grid[row][col].make_reset(row,col)
            return False
        if not grid[i][j].is_open():
            grid[i][j].make_checking()
            draw()
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].is_checking():
                grid[i][j].make_reset(i,j)
                # draw()
  
    # kiểm tra đường chéo dưới bên trái
    for i, j in zip(range(row, ROW, 1), 
                    range(col, -1, -1)):
        if grid[i][j].is_barrier():
            grid[i][j].make_closed()
            draw()
            grid[i][j].make_barrier()
            draw()
            for i2, j2 in zip(range(row, ROW, 1), 
                    range(col, -1, -1)):
                    if i2==i and j2==j:
                        continue
                    grid[i2][j2].make_reset(i2,j2)
                    # draw()
            grid[row][col].make_reset(row,col)
            return False
        if not grid[i][j].is_open():
            grid[i][j].make_checking()
            draw()
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].is_checking():
                grid[i][j].make_reset(i,j)
                # draw()
    grid[row][col].color=temp
    return True
#thuật toán giải n quân hậu 
def solveNQUtil(draw, grid, col):
      
    if col >= ROW:
        return True

    for i in range(ROW):
  
        if isSafe(draw, grid, i, col):
            grid[i][col].make_barrier()
            draw()
            if solveNQUtil(draw, grid, col + 1) == True:
                return True
            grid[i][col].make_reset(i,col)
            draw()
    return False

#hàm vẽ lưới
def make_grid(rows,width):
    grid=[]
    if (rows%2==0):
        gap=width//rows
    else:
        gap=width//rows+1
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot=Spot(i,j,gap,rows)
            grid[i].append(spot)
    return grid


#hàm vẽ bảng cờ khi chạy mô phỏng
def draw(win, grid, rows, width):
    win.fill(WHITE)
    win.blit(background_img,(0,0))
    for row in grid:
       for spot in row:
           spot.draw(win)                            
    win.blit(chat_bot_font,(750,400))
    pygame.time.wait(speed)
    pygame.display.flip()

#hàm vẽ bảng cờ cho màn hình chính
def drawbackground(win, grid, rows, width):
    win.fill(WHITE)
    win.blit(background_img,(0,0))

    for row in grid:
       for spot in row:
           spot.draw(win)
       
### Khối hàm hiện kết quả luôn ko hiển thị màn hình
def algorithm2(grid):
    sol=solveNQUtil2(lambda: draw(win, grid, ROW, WIDTH), grid, 0)
    if not sol:
        print("No Solution")
        return False
    else:
        print("Solution Found")
        return True

def isSafe2(draw, grid, row, col):
    temp=grid[row][col].color
    grid[row][col].make_open()
   
    for i in range(col):
        if grid[row][i].is_barrier():
            grid[row][i].make_closed()
            grid[row][i].make_barrier()
            for j in range(col):
                if j==i :
                    continue
                grid[row][j].make_reset(row,j)
            grid[row][col].make_reset(row,col)
            return False
        if not grid[row][i].is_open():
            grid[row][i].make_checking()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].is_checking():
                grid[i][j].make_reset(i,j)
    for i, j in zip(range(row, -1, -1), 
                    range(col, -1, -1)):
        if grid[i][j].is_barrier():
            grid[i][j].make_closed()
            grid[i][j].make_barrier()
            for i2, j2 in zip(range(row, -1, -1), 
                    range(col, -1, -1)):
                    if i2==i and j2==j:
                        continue
                    grid[i2][j2].make_reset(i2,j2)
            grid[row][col].make_reset(row,col)
            return False
        if not grid[i][j].is_open():
            grid[i][j].make_checking()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].is_checking():
                grid[i][j].make_reset(i,j)
    for i, j in zip(range(row, ROW, 1), 
                    range(col, -1, -1)):
        if grid[i][j].is_barrier():
            grid[i][j].make_closed()
            grid[i][j].make_barrier()
            for i2, j2 in zip(range(row, ROW, 1), 
                    range(col, -1, -1)):
                    if i2==i and j2==j:
                        continue
                    grid[i2][j2].make_reset(i2,j2)
            grid[row][col].make_reset(row,col)
            return False
        if not grid[i][j].is_open():
            grid[i][j].make_checking()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].is_checking():
                grid[i][j].make_reset(i,j)
    grid[row][col].color=temp
    return True

def solveNQUtil2(draw, grid, col):
      
    if col >= ROW:
        return True
    for i in range(ROW):
        if isSafe2(draw, grid, i, col):
            grid[i][col].make_barrier()
            if solveNQUtil2(draw, grid, col + 1) == True:
                return True
            grid[i][col].make_reset(i,col)
    return False

#def main(win, WIDTH):
#khởi tạo để chạy chương trình
run = True
running1=True
running2= False
running3 = False
running4=False
active=False
speed1=False
speed2=False
speed3=False
row_num=''
grid=make_grid(ROW,WIDTH)

while run:
    if running2:
        chat_bot='No Solution'
        run2=True
        draw(win,grid,ROW,WIDTH)
        if algorithm(grid):
            chat_bot='This is solution'
        drawbackground(win,grid,ROW,WIDTH)
        chat_bot_font2=font2.render(chat_bot, True,(255,255,255))
        while run2:
            clock.tick(10)
            pygame.draw.rect(win,(250,250,250),button_done_background2)
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    run2=False
                    run=False
                if events.type ==pygame.MOUSEBUTTONDOWN:
                    if button_done2.collidepoint(events.pos):
                        run2=False
                        grid=make_grid(ROW,WIDTH)
            a,b=pygame.mouse.get_pos()
            if button_done2.x<=a<=button_done2.x+130 and button_done2.y <=b <= button_done2.y+60:
                pygame.draw.rect(win,(148,170,214),button_done2)
            else:
                pygame.draw.rect(win,(66,120,180),button_done2)
            win.blit(chat_bot_font2,(800,400))
            win.blit(done_font,(button_done2.x+28,button_done2.y+18))
            pygame.display.flip()
        running2=False
        running1=True
        running3=False
        running4=False
    elif running4:
        algorithm2(grid)
        running2=False
        running1=True
        running3=False
        running4=False
    elif running3:
        clock.tick(60)
        drawbackground(win,grid,ROW,WIDTH)
        win.blit(setting_menu,(720,250))
        text_box=pygame.Rect(1050,280,110,50)
        pygame.draw.rect(win,(250,250,250),button_confirm_background)
        pygame.draw.rect(win,(250,250,250),button_done_background)
        pygame.draw.rect(win,(0,0,0),button_high_background)
        pygame.draw.rect(win,(0,0,0),button_medium_background)
        pygame.draw.rect(win,(0,0,0),button_slow_background)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run=False
            if events.type == pygame.MOUSEBUTTONDOWN:
                if text_box.collidepoint(events.pos):
                     active=True
                if button_done.collidepoint(events.pos):
                    running3=False
                    running2=False
                    running1=True
                    running4=False
                if button_confirm.collidepoint(events.pos):
                    ROW=int(row_num)
                    if speed1:
                        speed=50
                    elif speed2:
                        speed=200
                    elif speed3:
                        speed=400
                    else:
                        speed=200
                    grid=make_grid(ROW,WIDTH)
                    queen_img=pygame.image.load('queen.png')
                    queen_img=pygame.transform.scale(queen_img,(WIDTH//ROW,WIDTH//ROW))
                    speed1=False
                    speed2=False
                    speed3=False
                    row_num=''
                if button_high.collidepoint(events.pos):
                    speed1=True
                    speed2=False
                    speed3=False
                if button_medium.collidepoint(events.pos):
                    speed1=False
                    speed2=True
                    speed3=False
                if button_slow.collidepoint(events.pos):
                    speed3=True
                    speed2=False
                    speed1=False
            if events.type == pygame.KEYDOWN:
                if active:
                    if events.key == pygame.K_BACKSPACE:
                        row_num=row_num[:-1]
                    else:
                        row_num += events.unicode
        if active:
            pygame.draw.rect(win,(255,0,0),text_box, 4)
        else:
            pygame.draw.rect(win,(0,0,0),text_box, 4)
            
        surf_row = font3.render(row_num,True,(0,0,0))
        win.blit(surf_row, (text_box.x+10,text_box.y+5))

        a,b=pygame.mouse.get_pos()
        if button_confirm.x<=a<=button_confirm.x+130 and button_confirm.y <=b <= button_confirm.y+60:
            pygame.draw.rect(win,(148,170,214),button_confirm)
        else:
            pygame.draw.rect(win,(66,120,180),button_confirm)
        if button_done.x<=a<=button_done.x+130 and button_done.y <=b <= button_done.y+60:
            pygame.draw.rect(win,(148,170,214),button_done)
        else:
            pygame.draw.rect(win,(66,120,180),button_done)
        if speed1:
            pygame.draw.rect(win,(255,100,95),button_high)
        else:
            pygame.draw.rect(win,(255,156,125),button_high)
        if speed2:
            pygame.draw.rect(win,(255,100,95),button_medium)
        else:
            pygame.draw.rect(win,(255,156,125),button_medium)
        if speed3:
            pygame.draw.rect(win,(255,100,95),button_slow)
        else:
            pygame.draw.rect(win,(255,156,125),button_slow)
        

        win.blit(confirm_font,(button_confirm.x+10,button_confirm.y+18))
        win.blit(done_font,(button_done.x+28,button_done.y+18))
        win.blit(high_font,(button_high.x+28,button_high.y+15))
        win.blit(medium_font,(button_medium.x+10,button_medium.y+15))
        win.blit(slow_font,(button_slow.x+25,button_slow.y+15))
			
        pygame.display.flip()
    elif running1:
        clock.tick(60)
        drawbackground(win,grid,ROW,WIDTH)
            
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run=False
            if events.type == pygame.MOUSEBUTTONDOWN:
                if button_stimulate.collidepoint(events.pos):
                    running2=True
                    running1=False
                    running3=False
                    running4=False
                if button_setting.collidepoint(events.pos):
                    running3=True
                    running1=False
                    running2=False
                    running4=False
                if button_result.collidepoint(events.pos):
                    running4=True
                    running2=False
                    running1=False
                    running3=False
        a,b=pygame.mouse.get_pos()
        pygame.draw.rect(win,(250,250,250),button_result_background)
        pygame.draw.rect(win,(250,250,250),button_stimulate_background)
        pygame.draw.rect(win,(250,250,250),button_setting_background)
        if button_result.x<=a<=button_result.x+300 and button_result.y <=b <= button_result.y+100:
            pygame.draw.rect(win,(148,170,214),button_result)
        else:
            pygame.draw.rect(win,(66,120,180),button_result)
        if button_stimulate.x<=a<=button_stimulate.x+300 and button_stimulate.y <=b <= button_stimulate.y+100:
            pygame.draw.rect(win,(148,170,214),button_stimulate)
        else:
            pygame.draw.rect(win,(66,120,180),button_stimulate)
        if button_setting.x<=a<=button_stimulate.x+300 and button_setting.y <=b <= button_setting.y+100:
            pygame.draw.rect(win,(148,170,214),button_setting)
        else:
            pygame.draw.rect(win,(66,120,180),button_setting)		
        win.blit(result_font,(button_result.x+40,button_result.y+25))
        win.blit(stimulate_font,(button_stimulate.x+10,button_stimulate.y+25))
        win.blit(setting_font,(button_setting.x+40,button_setting.y+25))
        pygame.display.flip()        
pygame.quit()
#main(WIN, WIDTH)