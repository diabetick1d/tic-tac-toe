import pygame

def check_win(massive,sign):
    zeroes = 0
    for row in massive:
        zeroes += row.count(0)
        if row.count(sign)==3:
            return sign
    for col in range(3):
        if massive[0][col]==sign and massive[1][col] == sign and massive[2][col]==sign:
            return sign
    if massive[0][0]==sign and massive[1][1] == sign and massive[2][2]==sign:
        return sign
    if massive[0][2]==sign and massive[1][1] == sign and massive[2][0]==sign:
        return sign
    if zeroes == 0:
        return "Piece"
    return False

pygame.init() # Начало игры
FPS = 30; fpsClock = pygame.time.Clock() # Частота обновления экрана
pygame.display.set_caption("Крестики нолики") # Название   
icon = pygame.image.load("c:/python/mini-projects/X-0/icon.png") # Иконка
pygame.display.set_icon(icon)

size_block = 190 # Размер блока
margin = 10 # Отступы
width = height = size_block*3 + margin*4 # Рассчет размеров
screen = pygame.display.set_mode((width,height)) # Размеры

black = (50,50,50)
white = (200,200,200)
fon = (160,160,160)

massive = [[0]*3 for i in range(3)] # Массив для заполнения X or O
query = 0 # Чередования для ходов
game_over = False

running = True
while running:
    fpsClock.tick(FPS)
    screen.fill(fon) 
    if not game_over: # Проверка не закончена игра
        for row in range(3): # Создание игрового поля
            for col in range(3):
                if massive[row][col] == 'o': # если в массиве o, то закращиваем блок в белые, если x, то в чёрные, иначе в полностью белый(пустой блок)
                    color = white
                elif massive[row][col] == "x":
                    color = black
                else:
                    color = (255,255,255)
                x = col * size_block + (col + 1) * margin # Рассчитываем x и y блока
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x,y,size_block-10,size_block-10))
                if color == black: # Рисуем крестик
                    pygame.draw.line(screen,white, (x+10,y+10),(x+size_block-20,y+size_block-20),6)
                    pygame.draw.line(screen,white, (x+size_block-20,y+10),(x+10,y+size_block-20),6)
                elif color == white: # Рисуем нолик
                    pygame.draw.circle(screen,black, (x+size_block//2-5,y+size_block//2-5),size_block//2-8,6)
    
    if (query-1)%2 == 0: # Проверяет кто ходит
        game_over = check_win(massive, "x") # если x
    else:
        game_over = check_win(massive, "o") # если o
    if game_over: # Проверка на конец игры и вывыдо надписи победы или ничьей
        if game_over == "x":
            screen.fill(black)
        if game_over == "o":
            screen.fill(white)
        font = pygame.font.SysFont("stxingka", 80) # Шрифт
        text1 = font.render(game_over,True,(255,255,255))
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2 # Вычисляем центр для надписи
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x,text_y]) # Рисуем надпись

    for event in pygame.event.get():
        if event.type == pygame.quit: # Перестает выполнять если игра закрыта
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN: # закрытие при нажатии ESC
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over: # При нажатии мышью на блок и игра не закончена
            x_mouse,y_mouse = pygame.mouse.get_pos() # получение координат мыши 
            col = x_mouse // (size_block + margin) # вычисление колонки и ряда где находится мышь
            row = y_mouse // (size_block + margin) 
            if massive[row][col] == 0:
                if query%2 == 0:
                    massive[row][col] = "x" # Заполнение X на выбранный блок
                else:
                    massive[row][col] = "o" # Заполнение O на выбранный блок
                query+=1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Перезапуск при нажитии на пробел
            game_over = False
            massive = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(fon)
    pygame.display.update()

