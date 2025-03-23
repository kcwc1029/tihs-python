import pygame
import sys
import random

CYAN = (  0, 255, 255)
GRAY = ( 96,  96,  96)

MAZE_W = 11
MAZE_H = 9
maze = []
for y in range(MAZE_H):
    maze.append([0]*MAZE_W)

def make_maze():
    XP = [ 0, 1, 0,-1]
    YP = [-1, 0, 1, 0]

    #周圍的牆壁
    for x in range(MAZE_W):
        maze[0][x] = 1
        maze[MAZE_H-1][x] = 1
    for y in range(1, MAZE_H-1):
        maze[y][0] = 1
        maze[y][MAZE_W-1] = 1

    #內部為一片空白的狀態
    for y in range(1, MAZE_H-1):
        for x in range(1, MAZE_W-1):
            maze[y][x] = 0

    #柱子
    for y in range(2, MAZE_H-2, 2):
        for x in range(2, MAZE_W-2, 2):
            maze[y][x] = 1

    #於柱子的上下左右建立牆壁
    for y in range(2, MAZE_H-2, 2):
        for x in range(2, MAZE_W-2, 2):
         d = random.randint(0, 3)
         if x > 2: # 從第二欄的柱子開始，不在左側建立牆壁
             d = random.randint(0, 2)
         maze[y+YP[d]][x+XP[d]] = 1

def main():
    pygame.init()
    pygame.display.set_caption("產生迷宮")
    screen = pygame.display.set_mode((528, 432))
    clock = pygame.time.Clock()

    make_maze()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    make_maze()

        for y in range(MAZE_H):
            for x in range(MAZE_W):
                W = 48
                H = 48
                X = x*W
                Y = y*H
                if maze[y][x] == 0: # 通道
                    pygame.draw.rect(screen, CYAN, [X, Y, W, H])
                if maze[y][x] == 1: # 牆壁
                    pygame.draw.rect(screen, GRAY, [X, Y, W, H])

        pygame.display.update()
        clock.tick(2)

if __name__ == '__main__':
    main()
