import pygame as pg
import kociemba

class Cube():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0,0),pg.FULLSCREEN)
        self.size = self.screen.get_size()
        self.bg_image = pg.image.load('assets/background.png')
        self.running = True
        self.selected_color = (0,0,0)
        self.solution = ["press fill the cube and press 'Solution'"]
        self.font = pg.font.Font('assets/Playball.ttf',50)
        self.face_front = [[(0,0,0), (0,0,0), (0,0,0)],[(0,0,0), (0,0,0), (0,0,0)],[(0,0,0), (0,0,0), (0,0,0)]]
        self.face_right = [[(0,0,0), (0,0,0), (0,0,0)],[(0,0,0), (0,0,0), (0,0,0)],[(0,0,0), (0,0,0), (0,0,0)]]
        self.face_back  = [[(0,0,0), (0,0,0), (0,0,0)],[(0,0,0), (0,0,0), (0,0,0)],[(0,0,0), (0,0,0), (0,0,0)]]
        self.face_left  = [[(0,0,0), (0,0,0), (0,0,0)],[(0,0,0), (0,0,0), (0,0,0)],[(0,0,0), (0,0,0), (0,0,0)]]
        self.face_up    = [[(0,0,0), (0,0,0), (0,0,0)],[(0,0,0), (0,0,0), (0,0,0)],[(0,0,0), (0,0,0), (0,0,0)]]
        self.face_down  = [[(0,0,0), (0,0,0), (0,0,0)],[(0,0,0), (0,0,0), (0,0,0)],[(0,0,0), (0,0,0), (0,0,0)]]
    def display_text(self,text,pos,size = None):
        temp = self.font.render(text,False,(255,255,255))
        if size != None:
            temp = pg.transform.scale(temp,size)
        self.screen.blit(temp, pos)
    def proximity(self,target,pos,error):
        result = False
        if pos[0] + error[0] > target[0] and pos[0] - error[0] < target[0] and\
            pos[1] + error[1] > target[1] and pos[1] - error[1] < target[1] :
            result = True
        return result
    def decode(self,color):
        result = None
        if color == (0,0,0):
            result = '0'
        elif color == self.face_up[1][1]:
            result = 'U'
        elif color == self.face_right[1][1]:
            result = 'R'
        elif color == self.face_front[1][1]:
            result = 'F'
        elif color == self.face_down[1][1]:
            result = 'D'
        elif color == self.face_left[1][1]:
            result = 'L'
        elif color == self.face_back[1][1]:
            result = 'B'
        else:
            result = '0'
        return result
    def encode(self):
        code = ''
        #up
        for i in range(3):
            for j in range(3):
                code += self.decode(self.face_up[2-j][2-i])
        #right
        for i in range(3):
            for j in range(3):
                code += self.decode(self.face_right[2 - j][2 - i])
        #front
        for i in range(3):
            for j in range(3):
                code += self.decode(self.face_front[2 - j][2 - i])
        #down
        for i in range(3):
            for j in range(3):
                code += self.decode(self.face_down[2 - j][2 - i])
        #left
        for i in range(3):
            for j in range(3):
                code += self.decode(self.face_left[2 - j][2 - i])
        #back
        for i in range(3):
            for j in range(3):
                code += self.decode(self.face_back[2 - j][2 - i])
        return code
    def solve(self):
        code = self.encode()
        try:
            solution = kociemba.solve(code)
        except:
            solution = "Invalid Rubic's cube. Please try again! "
        return solution
    def draw_face(self):
        mouse_pos = pg.mouse.get_pos()
        size = self.size[1]/12
        #front
        pos_x = self.size[0] * 3 / 4 - self.size[0] * 3 / 8
        pos_y = self.size[1] * 3 / 4 - self.size[1] * 3 / 12
        for i,layer in enumerate(self.face_front):
            for j,color in enumerate(layer):
                pos = (pos_x - (1+i)*size,pos_y - (1+j)*size)
                pg.draw.rect(self.screen,color,(pos,(size-2,size-2)),0,3)
                pg.draw.rect(self.screen, (250,250,250), ((pos[0]-1,pos[1]-1), (size, size)), 2, 3)
                if self.proximity((pos[0]+size/2,pos[1]+size/2),mouse_pos,(size/2,size/2)):
                    pg.draw.rect(self.screen, (250, 250, 250), ((pos[0]+1, pos[1]+1), (size+2, size+2)), 2, 3)
                    if pg.mouse.get_pressed()[0]:
                        self.face_front[i][j] = self.selected_color
        #right
        pos_x = self.size[0] * 3 / 4 - self.size[0] * 3 / 8 + size*3 + 5
        pos_y = self.size[1] * 3 / 4 - self.size[1] * 3 / 12
        for i, layer in enumerate(self.face_right):
            for j, color in enumerate(layer):
                pos = (pos_x - (1 + i) * size, pos_y - (1 + j) * size)
                pg.draw.rect(self.screen, color, (pos, (size - 2, size - 2)), 0, 3)
                pg.draw.rect(self.screen, (250, 250, 250), ((pos[0] - 1, pos[1] - 1), (size, size)), 2, 3)
                if self.proximity((pos[0] + size / 2, pos[1] + size / 2), mouse_pos, (size / 2, size / 2)):
                    pg.draw.rect(self.screen, (250, 250, 250), ((pos[0] + 1, pos[1] + 1), (size + 2, size + 2)), 2,
                                 3)
                    if pg.mouse.get_pressed()[0]:
                        self.face_right[i][j] = self.selected_color
        #back
        pos_x = self.size[0] * 3 / 4 - self.size[0] * 3 / 8 + size*3*2 + 10
        pos_y = self.size[1] * 3 / 4 - self.size[1] * 3 / 12
        for i, layer in enumerate(self.face_back):
            for j, color in enumerate(layer):
                pos = (pos_x - (1 + i) * size, pos_y - (1 + j) * size)
                pg.draw.rect(self.screen, color, (pos, (size - 2, size - 2)), 0, 3)
                pg.draw.rect(self.screen, (250, 250, 250), ((pos[0] - 1, pos[1] - 1), (size, size)), 2, 3)
                if self.proximity((pos[0] + size / 2, pos[1] + size / 2), mouse_pos, (size / 2, size / 2)):
                    pg.draw.rect(self.screen, (250, 250, 250), ((pos[0] + 1, pos[1] + 1), (size + 2, size + 2)), 2,
                                 3)
                    if pg.mouse.get_pressed()[0]:
                        self.face_back[i][j] = self.selected_color
        #left
        pos_x = self.size[0] * 3 / 4 - self.size[0] * 3 / 8 - size*3 - 5
        pos_y = self.size[1] * 3 / 4 - self.size[1] * 3 / 12
        for i, layer in enumerate(self.face_left):
            for j, color in enumerate(layer):
                pos = (pos_x - (1 + i) * size, pos_y - (1 + j) * size)
                pg.draw.rect(self.screen, color, (pos, (size - 2, size - 2)), 0, 3)
                pg.draw.rect(self.screen, (250, 250, 250), ((pos[0] - 1, pos[1] - 1), (size, size)), 2, 3)
                if self.proximity((pos[0] + size / 2, pos[1] + size / 2), mouse_pos, (size / 2, size / 2)):
                    pg.draw.rect(self.screen, (250, 250, 250), ((pos[0] + 1, pos[1] + 1), (size + 2, size + 2)), 2,
                                 3)
                    if pg.mouse.get_pressed()[0]:
                        self.face_left[i][j] = self.selected_color
        #up
        pos_x = self.size[0] * 3 / 4 - self.size[0] * 3 / 8
        pos_y = self.size[1] * 3 / 4 - self.size[1] * 3 / 12 - size*3 - 5
        for i,layer in enumerate(self.face_up):
            for j,color in enumerate(layer):
                pos = (pos_x - (1+i)*size,pos_y - (1+j)*size)
                pg.draw.rect(self.screen,color,(pos,(size-2,size-2)),0,3)
                pg.draw.rect(self.screen, (250,250,250), ((pos[0]-1,pos[1]-1), (size, size)), 2, 3)
                if self.proximity((pos[0]+size/2,pos[1]+size/2),mouse_pos,(size/2,size/2)):
                    pg.draw.rect(self.screen, (250, 250, 250), ((pos[0]+1, pos[1]+1), (size+2, size+2)), 2, 3)
                    if pg.mouse.get_pressed()[0]:
                        self.face_up[i][j] = self.selected_color
        #down
        pos_x = self.size[0] * 3 / 4 - self.size[0] * 3 / 8
        pos_y = self.size[1] * 3 / 4 - self.size[1] * 3 / 12 + size*3 + 5
        for i,layer in enumerate(self.face_down):
            for j,color in enumerate(layer):
                pos = (pos_x - (1+i)*size,pos_y - (1+j)*size)
                pg.draw.rect(self.screen,color,(pos,(size-2,size-2)),0,3)
                pg.draw.rect(self.screen, (250,250,250), ((pos[0]-1,pos[1]-1), (size, size)), 2, 3)
                if self.proximity((pos[0]+size/2,pos[1]+size/2),mouse_pos,(size/2,size/2)):
                    pg.draw.rect(self.screen, (250, 250, 250), ((pos[0]+1, pos[1]+1), (size+2, size+2)), 2, 3)
                    if pg.mouse.get_pressed()[0]:
                        self.face_down[i][j] = self.selected_color
    def update_face(self,move):
        move_temp = list(move)
        rounds = 1
        if move_temp[-1] == '2':
            move_temp.pop(-1)
            rounds = 2
            if len(move_temp) > 0:
                move = ''.join(move_temp)
            else:
                move = move_temp[0]
        for i in range(rounds):
            if move == 'U':
                left = [self.face_front[0][2],self.face_front[1][2],self.face_front[2][2]]
                front = [self.face_right[0][2],self.face_right[1][2],self.face_right[2][2]]
                right = [self.face_back[0][2],self.face_back[1][2],self.face_back[2][2]]
                back = [self.face_left[0][2],self.face_left[1][2],self.face_left[2][2]]
                self.face_front[0][2],self.face_front[1][2],self.face_front[2][2] = front[0],front[1],front[2]
                self.face_right[0][2],self.face_right[1][2],self.face_right[2][2] = right[0],right[1],right[2]
                self.face_back[0][2],self.face_back[1][2],self.face_back[2][2] = back[0],back[1],back[2]
                self.face_left[0][2],self.face_left[1][2],self.face_left[2][2] = left[0],left[1],left[2]
                d = [self.face_up[0][0],self.face_up[0][1],self.face_up[0][2]]
                l = [self.face_up[0][2],self.face_up[1][2],self.face_up[2][2]]
                u = [self.face_up[2][2],self.face_up[2][1],self.face_up[0][0]]
                r = [self.face_up[2][0],self.face_up[1][0],self.face_up[0][0]]
                self.face_up[0][2], self.face_up[1][2], self.face_up[2][2] = u[0],u[1],u[2]
                self.face_up[2][2], self.face_up[2][1], self.face_up[0][0] = r[0],r[1],r[2]
                self.face_up[2][0], self.face_up[1][0], self.face_up[0][0] = d[0],d[1],d[2]
                self.face_up[0][0], self.face_up[0][1], self.face_up[0][2] = l[0],l[1],l[2]
            elif move == "U'":
                right = [self.face_front[0][2],self.face_front[1][2],self.face_front[2][2]]
                back = [self.face_right[0][2],self.face_right[1][2],self.face_right[2][2]]
                left = [self.face_back[0][2],self.face_back[1][2],self.face_back[2][2]]
                front = [self.face_left[0][2],self.face_left[1][2],self.face_left[2][2]]
                self.face_front[0][2],self.face_front[1][2],self.face_front[2][2] = front[0],front[1],front[2]
                self.face_right[0][2],self.face_right[1][2],self.face_right[2][2] = right[0],right[1],right[2]
                self.face_back[0][2],self.face_back[1][2],self.face_back[2][2] = back[0],back[1],back[2]
                self.face_left[0][2],self.face_left[1][2],self.face_left[2][2] = left[0],left[1],left[2]
                u = [self.face_up[0][0],self.face_up[0][1],self.face_up[0][2]]
                r = [self.face_up[0][2],self.face_up[1][2],self.face_up[2][2]]
                d = [self.face_up[2][2],self.face_up[2][1],self.face_up[0][0]]
                l = [self.face_up[2][0],self.face_up[1][0],self.face_up[0][0]]
                self.face_up[0][2], self.face_up[1][2], self.face_up[2][2] = u[0],u[1],u[2]
                self.face_up[2][2], self.face_up[2][1], self.face_up[0][0] = r[0],r[1],r[2]
                self.face_up[2][0], self.face_up[1][0], self.face_up[0][0] = d[0],d[1],d[2]
                self.face_up[0][0], self.face_up[0][1], self.face_up[0][2] = l[0],l[1],l[2]
            elif move == 'D':
                right = [self.face_front[0][0],self.face_front[1][0],self.face_front[2][0]]
                back = [self.face_right[0][0],self.face_right[1][0],self.face_right[2][0]]
                left = [self.face_back[0][0],self.face_back[1][0],self.face_back[2][0]]
                front = [self.face_left[0][0],self.face_left[1][0],self.face_left[2][0]]
                self.face_front[0][0],self.face_front[1][0],self.face_front[2][0] = front[0],front[1],front[2]
                self.face_right[0][0],self.face_right[1][0],self.face_right[2][0] = right[0],right[1],right[2]
                self.face_back[0][0],self.face_back[1][0],self.face_back[2][0] = back[0],back[1],back[2]
                self.face_left[0][0],self.face_left[1][0],self.face_left[2][0] = left[0],left[1],left[2]
                d = [self.face_down[0][0],self.face_down[0][1],self.face_down[0][2]]
                l = [self.face_down[0][2],self.face_down[1][2],self.face_down[2][2]]
                u = [self.face_down[2][2],self.face_down[2][1],self.face_down[0][0]]
                r = [self.face_down[2][0],self.face_down[1][0],self.face_down[0][0]]
                self.face_down[0][2], self.face_down[1][2], self.face_down[2][2] = u[0],u[1],u[2]
                self.face_down[2][2], self.face_down[2][1], self.face_down[0][0] = r[0],r[1],r[2]
                self.face_down[2][0], self.face_down[1][0], self.face_down[0][0] = d[0],d[1],d[2]
                self.face_down[0][0], self.face_down[0][1], self.face_down[0][2] = l[0],l[1],l[2]
            elif move == "D'":
                left = [self.face_front[0][0],self.face_front[1][0],self.face_front[2][0]]
                front = [self.face_right[0][0],self.face_right[1][0],self.face_right[2][0]]
                right = [self.face_back[0][0],self.face_back[1][0],self.face_back[2][0]]
                back = [self.face_left[0][0],self.face_left[1][0],self.face_left[2][0]]
                self.face_front[0][0],self.face_front[1][0],self.face_front[2][0] = front[0],front[1],front[2]
                self.face_right[0][0],self.face_right[1][0],self.face_right[2][0] = right[0],right[1],right[2]
                self.face_back[0][0],self.face_back[1][0],self.face_back[2][0] = back[0],back[1],back[2]
                self.face_left[0][0],self.face_left[1][0],self.face_left[2][0] = left[0],left[1],left[2]
                u = [self.face_down[0][0],self.face_down[0][1],self.face_down[0][2]]
                r = [self.face_down[0][2],self.face_down[1][2],self.face_down[2][2]]
                d = [self.face_down[2][2],self.face_down[2][1],self.face_down[0][0]]
                l = [self.face_down[2][0],self.face_down[1][0],self.face_down[0][0]]
                self.face_down[0][2], self.face_down[1][2], self.face_down[2][2] = u[0],u[1],u[2]
                self.face_down[2][2], self.face_down[2][1], self.face_down[0][0] = r[0],r[1],r[2]
                self.face_down[2][0], self.face_down[1][0], self.face_down[0][0] = d[0],d[1],d[2]
                self.face_down[0][0], self.face_down[0][1], self.face_down[0][2] = l[0],l[1],l[2]
            elif move == 'R':
                back = [self.face_up[0][0],self.face_up[0][1],self.face_up[0][2]]
                down = [self.face_back[2][0],self.face_back[2][1],self.face_back[2][2]]
                front = [self.face_down[0][0],self.face_down[0][1],self.face_down[0][2]]
                up = [self.face_front[0][0],self.face_front[0][1],self.face_front[0][2]]
                self.face_front[0][0],self.face_front[0][1],self.face_front[0][2] = front[0],front[1],front[2]
                self.face_up[0][0],self.face_up[0][1],self.face_up[0][2] = up[0],up[1],up[2]
                self.face_back[2][0],self.face_back[2][1],self.face_back[2][2] = back[2],back[1],back[0]
                self.face_down[0][0],self.face_down[0][1],self.face_down[0][2] = down[2],down[1],down[0]
                d = [self.face_right[0][0],self.face_right[0][1],self.face_right[0][2]]
                l = [self.face_right[0][2],self.face_right[1][2],self.face_right[2][2]]
                u = [self.face_right[2][2],self.face_right[2][1],self.face_right[0][0]]
                r = [self.face_right[2][0],self.face_right[1][0],self.face_right[0][0]]
                self.face_right[0][2], self.face_right[1][2], self.face_right[2][2] = u[0],u[1],u[2]
                self.face_right[2][2], self.face_right[2][1], self.face_right[0][0] = r[0],r[1],r[2]
                self.face_right[2][0], self.face_right[1][0], self.face_right[0][0] = d[0],d[1],d[2]
                self.face_right[0][0], self.face_right[0][1], self.face_right[0][2] = l[0],l[1],l[2]
            elif move == "R'":
                front = [self.face_up[0][0],self.face_up[0][1],self.face_up[0][2]]
                up = [self.face_back[2][0],self.face_back[2][1],self.face_back[2][2]]
                back = [self.face_down[0][0],self.face_down[0][1],self.face_down[0][2]]
                down = [self.face_front[0][0],self.face_front[0][1],self.face_front[0][2]]
                self.face_front[0][0],self.face_front[0][1],self.face_front[0][2] = front[0],front[1],front[2]
                self.face_up[0][0],self.face_up[0][1],self.face_up[0][2] = up[2],up[1],up[0]
                self.face_back[2][0],self.face_back[2][1],self.face_back[2][2] = back[2],back[1],back[0]
                self.face_down[0][0],self.face_down[0][1],self.face_down[0][2] = down[0],down[1],down[2]
                u = [self.face_right[0][0],self.face_right[0][1],self.face_right[0][2]]
                r = [self.face_right[0][2],self.face_right[1][2],self.face_right[2][2]]
                d = [self.face_right[2][2],self.face_right[2][1],self.face_right[0][0]]
                l = [self.face_right[2][0],self.face_right[1][0],self.face_right[0][0]]
                self.face_right[0][2], self.face_right[1][2], self.face_right[2][2] = u[0],u[1],u[2]
                self.face_right[2][2], self.face_right[2][1], self.face_right[0][0] = r[0],r[1],r[2]
                self.face_right[2][0], self.face_right[1][0], self.face_right[0][0] = d[0],d[1],d[2]
                self.face_right[0][0], self.face_right[0][1], self.face_right[0][2] = l[0],l[1],l[2]
            elif move == "L":
                front = [self.face_up[2][0],self.face_up[2][1],self.face_up[2][2]]
                up = [self.face_back[0][0],self.face_back[0][1],self.face_back[0][2]]
                back = [self.face_down[2][0],self.face_down[2][1],self.face_down[2][2]]
                down = [self.face_front[2][0],self.face_front[2][1],self.face_front[2][2]]
                self.face_front[2][0],self.face_front[2][1],self.face_front[2][2] = front[0],front[1],front[2]
                self.face_up[2][0],self.face_up[2][1],self.face_up[2][2] = up[2],up[1],up[0]
                self.face_back[0][0],self.face_back[0][1],self.face_back[0][2] = back[2],back[1],back[0]
                self.face_down[2][0],self.face_down[2][1],self.face_down[2][2] = down[0],down[1],down[2]
                d = [self.face_left[0][0],self.face_left[0][1],self.face_left[0][2]]
                l = [self.face_left[0][2],self.face_left[1][2],self.face_left[2][2]]
                u = [self.face_left[2][2],self.face_left[2][1],self.face_left[0][0]]
                r = [self.face_left[2][0],self.face_left[1][0],self.face_left[0][0]]
                self.face_left[0][2], self.face_left[1][2], self.face_left[2][2] = u[0],u[1],u[2]
                self.face_left[2][2], self.face_left[2][1], self.face_left[0][0] = r[0],r[1],r[2]
                self.face_left[2][0], self.face_left[1][0], self.face_left[0][0] = d[0],d[1],d[2]
                self.face_left[0][0], self.face_left[0][1], self.face_left[0][2] = l[0],l[1],l[2]
            elif move == "L'":
                back = [self.face_up[2][0],self.face_up[2][1],self.face_up[2][2]]
                down = [self.face_back[0][0],self.face_back[0][1],self.face_back[0][2]]
                front = [self.face_down[2][0],self.face_down[2][1],self.face_down[2][2]]
                up = [self.face_front[2][0],self.face_front[2][1],self.face_front[2][2]]
                self.face_front[2][0],self.face_front[2][1],self.face_front[2][2] = front[0],front[1],front[2]
                self.face_up[2][0],self.face_up[2][1],self.face_up[2][2] = up[0],up[1],up[2]
                self.face_back[0][0],self.face_back[0][1],self.face_back[0][2] = back[2],back[1],back[0]
                self.face_down[2][0],self.face_down[2][1],self.face_down[2][2] = down[2],down[1],down[0]
                u = [self.face_left[0][0],self.face_left[0][1],self.face_left[0][2]]
                r = [self.face_left[0][2],self.face_left[1][2],self.face_left[2][2]]
                d = [self.face_left[2][2],self.face_left[2][1],self.face_left[0][0]]
                l = [self.face_left[2][0],self.face_left[1][0],self.face_left[0][0]]
                self.face_left[0][2], self.face_left[1][2], self.face_left[2][2] = u[0],u[1],u[2]
                self.face_left[2][2], self.face_left[2][1], self.face_left[0][0] = r[0],r[1],r[2]
                self.face_left[2][0], self.face_left[1][0], self.face_left[0][0] = d[0],d[1],d[2]
                self.face_left[0][0], self.face_left[0][1], self.face_left[0][2] = l[0],l[1],l[2]
            elif move == "F":
                right = [self.face_up[0][0],self.face_up[1][0],self.face_up[2][0]]
                down = [self.face_right[2][0],self.face_right[2][1],self.face_right[2][2]]
                left = [self.face_down[0][2],self.face_down[1][2],self.face_down[2][2]]
                up = [self.face_left[0][0],self.face_left[0][1],self.face_left[0][2]]
                self.face_right[2][0],self.face_right[2][1],self.face_right[2][2] = right[0],right[1],right[2]
                self.face_up[0][0],self.face_up[1][0],self.face_up[2][0] = up[2],up[1],up[0]
                self.face_left[0][0],self.face_left[0][1],self.face_left[0][2] = left[0],left[1],left[2]
                self.face_down[0][2],self.face_down[1][2],self.face_down[2][2] = down[2],down[1],down[0]
                d = [self.face_front[0][0],self.face_front[0][1],self.face_front[0][2]]
                l = [self.face_front[0][2],self.face_front[1][2],self.face_front[2][2]]
                u = [self.face_front[2][2],self.face_front[2][1],self.face_front[0][0]]
                r = [self.face_front[2][0],self.face_front[1][0],self.face_front[0][0]]
                self.face_front[0][2], self.face_front[1][2], self.face_front[2][2] = u[0],u[1],u[2]
                self.face_front[2][2], self.face_front[2][1], self.face_front[0][0] = r[0],r[1],r[2]
                self.face_front[2][0], self.face_front[1][0], self.face_front[0][0] = d[0],d[1],d[2]
                self.face_front[0][0], self.face_front[0][1], self.face_front[0][2] = l[0],l[1],l[2]
            elif move == "F'":
                left = [self.face_up[0][0],self.face_up[1][0],self.face_up[2][0]]
                up = [self.face_right[2][0],self.face_right[2][1],self.face_right[2][2]]
                right = [self.face_down[0][2],self.face_down[1][2],self.face_down[2][2]]
                down = [self.face_left[0][0],self.face_left[0][1],self.face_left[0][2]]
                self.face_right[2][0],self.face_right[2][1],self.face_right[2][2] = right[2],right[1],right[0]
                self.face_up[0][0],self.face_up[1][0],self.face_up[2][0] = up[0],up[1],up[2]
                self.face_left[0][0],self.face_left[0][1],self.face_left[0][2] = left[2],left[1],left[0]
                self.face_down[0][2],self.face_down[1][2],self.face_down[2][2] = down[0],down[1],down[2]
                u = [self.face_front[0][0],self.face_front[0][1],self.face_front[0][2]]
                r = [self.face_front[0][2],self.face_front[1][2],self.face_front[2][2]]
                d = [self.face_front[2][2],self.face_front[2][1],self.face_front[0][0]]
                l = [self.face_front[2][0],self.face_front[1][0],self.face_front[0][0]]
                self.face_front[0][2], self.face_front[1][2], self.face_front[2][2] = u[0],u[1],u[2]
                self.face_front[2][2], self.face_front[2][1], self.face_front[0][0] = r[0],r[1],r[2]
                self.face_front[2][0], self.face_front[1][0], self.face_front[0][0] = d[0],d[1],d[2]
                self.face_front[0][0], self.face_front[0][1], self.face_front[0][2] = l[0],l[1],l[2]
            elif move == "B":
                left = [self.face_up[0][2],self.face_up[1][2],self.face_up[2][2]]
                up = [self.face_right[0][0],self.face_right[0][1],self.face_right[0][2]]
                right = [self.face_down[0][0],self.face_down[1][0],self.face_down[2][0]]
                down = [self.face_left[2][0],self.face_left[2][1],self.face_left[2][2]]
                self.face_right[0][0],self.face_right[0][1],self.face_right[0][2] = right[2],right[1],right[0]
                self.face_up[0][2],self.face_up[1][2],self.face_up[2][2] = up[0],up[1],up[2]
                self.face_left[2][0],self.face_left[2][1],self.face_left[2][2] = left[2],left[1],left[0]
                self.face_down[0][0],self.face_down[1][0],self.face_down[2][0] = down[0],down[1],down[2]
                d = [self.face_back[0][0],self.face_back[0][1],self.face_back[0][2]]
                l = [self.face_back[0][2],self.face_back[1][2],self.face_back[2][2]]
                u = [self.face_back[2][2],self.face_back[2][1],self.face_back[0][0]]
                r = [self.face_back[2][0],self.face_back[1][0],self.face_back[0][0]]
                self.face_back[0][2], self.face_back[1][2], self.face_back[2][2] = u[0],u[1],u[2]
                self.face_back[2][2], self.face_back[2][1], self.face_back[0][0] = r[0],r[1],r[2]
                self.face_back[2][0], self.face_back[1][0], self.face_back[0][0] = d[0],d[1],d[2]
                self.face_back[0][0], self.face_back[0][1], self.face_back[0][2] = l[0],l[1],l[2]
            elif move == "B'":
                right = [self.face_up[0][2],self.face_up[1][2],self.face_up[2][2]]
                down = [self.face_right[0][0],self.face_right[0][1],self.face_right[0][2]]
                left = [self.face_down[0][0],self.face_down[1][0],self.face_down[2][0]]
                up = [self.face_left[2][0],self.face_left[2][1],self.face_left[2][2]]
                self.face_right[0][0],self.face_right[0][1],self.face_right[0][2] = right[0],right[1],right[2]
                self.face_up[0][2],self.face_up[1][2],self.face_up[2][2] = up[2],up[1],up[0]
                self.face_left[2][0],self.face_left[2][1],self.face_left[2][2] = left[0],left[1],left[2]
                self.face_down[0][0],self.face_down[1][0],self.face_down[2][0] = down[2],down[1],down[0]
                u = [self.face_back[0][0],self.face_back[0][1],self.face_back[0][2]]
                r = [self.face_back[0][2],self.face_back[1][2],self.face_back[2][2]]
                d = [self.face_back[2][2],self.face_back[2][1],self.face_back[0][0]]
                l = [self.face_back[2][0],self.face_back[1][0],self.face_back[0][0]]
                self.face_back[0][2], self.face_back[1][2], self.face_back[2][2] = u[0],u[1],u[2]
                self.face_back[2][2], self.face_back[2][1], self.face_back[0][0] = r[0],r[1],r[2]
                self.face_back[2][0], self.face_back[1][0], self.face_back[0][0] = d[0],d[1],d[2]
                self.face_back[0][0], self.face_back[0][1], self.face_back[0][2] = l[0],l[1],l[2]
    def button_colors(self, pos, size,color,mouse_pos):
        pos_center = (pos[0] - size[0] / 2, pos[1] - size[1] / 2)
        if self.selected_color == color:
            pg.draw.rect(self.screen, color, (pos_center, size), 0, 10)
            pg.draw.rect(self.screen, (250, 250, 250),((pos_center[0] - 3, pos_center[1] - 3), (size[0] + 3, size[1] + 3)), 4, 10)
        elif self.proximity((pos),mouse_pos,(size[0]/2,size[1]/2)):
            pg.draw.rect(self.screen, color, (pos_center, size), 0, 10)
            pg.draw.rect(self.screen, (150,150,150), ((pos_center[0]-2,pos_center[1]-2), (size[0]+2,size[1]+2)), 4, 10)
            if pg.mouse.get_pressed()[0]:
                self.selected_color = color
        else:
            pg.draw.rect(self.screen, color, (pos_center, size), 0, 10)
    def button(self, pos, size,color,mouse_pos,text):
        pos_center = (pos[0] - size[0] / 2, pos[1] - size[1] / 2)
        if self.proximity((pos),mouse_pos,(size[0]/2,size[1]/2)):
            pg.draw.rect(self.screen, color, (pos_center, size), 0, 10)
            pg.draw.rect(self.screen, (150,150,150), ((pos_center[0]-2,pos_center[1]-2), (size[0]+2,size[1]+2)), 2, 10)
            self.display_text(text, (pos_center[0] + 2, pos_center[1] + 2), (size[0] - 4, size[1] - 4))
            return True
        else:
            pg.draw.rect(self.screen, color, (pos_center, size), 0, 10)
            self.display_text(text, (pos_center[0] + 2, pos_center[1] + 2), (size[0] - 4, size[1] - 4))
            return False
    def image_guid(self):
        move = list(self.solution[0])
        if move[-1] == '2':
            move.pop(-1)
            if len(move) > 0:
                move = ''.join(move)
            else:
                move = move[0]
            self.display_text('x2',(int(self.size[0]/8)+5,int(self.size[0]/16)),(int(self.size[1]/12),int(self.size[1]/12)))
        else:
            move = self.solution[0]
        if move == 'U':
            image = pg.image.load('assets/U.png')
        elif move == "U'":
            image = pg.image.load('assets/Ui.png')
        elif move == 'F':
            image = pg.image.load('assets/F.png')
        elif move == "F'":
            image = pg.image.load('assets/Fi.png')
        elif move == 'R':
            image = pg.image.load('assets/R.png')
        elif move == "R'":
            image = pg.image.load('assets/Ri.png')
        elif move == 'B':
            image = pg.image.load('assets/B.png')
        elif move == "B'":
            image = pg.image.load('assets/Bi.png')
        elif move == 'L':
            image = pg.image.load('assets/L.png')
        elif move == "L'":
            image = pg.image.load('assets/Li.png')
        elif move == 'D':
            image = pg.image.load('assets/D.png')
        elif move == "D'":
            image = pg.image.load('assets/Di.png')
        else:
            image = None
        if image == None:
            pass
        else:
            image = pg.transform.scale(image,(int(self.size[0]/8)+20,int(self.size[0]/8)+40))
            self.screen.blit(image,(0,0))
    def control(self):
        mouse_pos = pg.mouse.get_pos()
        #buttons for selecting colors
        self.button_colors((self.size[0] * 3 / 4 + self.size[0] / 16, self.size[1]*2.5/10), (self.size[1]/8, self.size[1]/8), (250, 0, 0), mouse_pos)  # red
        self.button_colors((self.size[0] * 3 / 4 + self.size[0] / 6, self.size[1]*2.5/10), (self.size[1]/8, self.size[1]/8), (0, 250, 0), mouse_pos)  # green
        self.button_colors((self.size[0] * 3 / 4 + self.size[0] / 16, self.size[1]*4.5/10), (self.size[1]/8, self.size[1]/8), (250, 125, 0), mouse_pos)  # orange
        self.button_colors((self.size[0] * 3 / 4 + self.size[0] / 6, self.size[1]*4.5/10), (self.size[1]/8, self.size[1]/8), (250, 250, 250), mouse_pos)  # white
        self.button_colors((self.size[0] * 3 / 4 + self.size[0] / 16, self.size[1]*6.5/10), (self.size[1]/8, self.size[1]/8), (0, 0, 250), mouse_pos)  # blue
        self.button_colors((self.size[0] * 3 / 4 + self.size[0] / 6, self.size[1]*6.5/10), (self.size[1]/8, self.size[1]/8), (250, 250, 0), mouse_pos)  # yellow
        next_button = self.button((self.size[0] * 7 / 8, self.size[1] * 7 / 8 + 10), (100, 70), (0, 50, 0), mouse_pos,'Next')
        solve_button = self.button((self.size[0] * 3 / 8, self.size[1] * 7 / 8), (150, 70), (0, 50, 0), mouse_pos,'Solution')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYUP:
                self.running = False
            if event.type == pg.VIDEORESIZE:
                self.size = (event.w,event.h)
            if event.type == pg.MOUSEBUTTONUP:
                # solution button
                if solve_button:
                    if self.solve()[0] == 'I':
                        self.solution = [self.solve()]
                    else:
                        self.solution = self.solve().split()
                #next button
                if next_button:
                    if len(self.solution) > 1:
                        self.update_face(self.solution[0])
                        self.solution.pop(0)
                    else:
                        self.update_face(self.solution[0])
                        self.solution = ["solved!"]
    def update(self):
        #background
        image = pg.transform.scale(self.bg_image,(int(self.size[0]*3/4),int(self.size[1]*3/4)))
        self.screen.blit(image,(0,0))
        pg.draw.line(self.screen,(0,150,0),(self.size[0]*3/4,0),(self.size[0]*3/4,self.size[1]*3/4),4)
        pg.draw.line(self.screen, (0, 150, 0), (0,self.size[1] * 3 / 4), ( self.size[0],self.size[1] * 3 / 4), 4)
        self.display_text('Select',(self.size[0]*3/4 + self.size[0] / 32,0))
        self.display_text('color', (self.size[0] * 3 / 4 + self.size[0] / 32, 50))
        self.draw_face()
        self.display_text('your code is ->'+self.encode(),(0, self.size[1] * 3/4 + 10),(int(self.size[0]*3/4)-20,int(self.size[0]*3/150)))
        self.display_text(self.solution[0], (10, self.size[1] * 7 / 8 + 40))
        self.image_guid();
        pg.display.update()
        self.screen.fill((0,0,0))
    def run(self):
        while self.running:
            self.control()
            self.update()
        pg.quit()

if __name__ == '__main__':
    new_cube = Cube()
    new_cube.run()
