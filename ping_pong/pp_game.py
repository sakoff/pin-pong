from pygame import*


class GameSprite(sprite.Sprite):
    '''psrent_class for other classes'''
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y, ):
        '''констркутор класса'''
        super().__init__()

        '''каждый спрайт хранит св-во изображения'''
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        ''''''
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        '''method for paint platform'''
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    ''''''
    def move_right(self):
        '''move right'''
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 5:
            self.rect.y += self.speed

    def move_left(self):
        '''move left'''
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 5:
            self.rect.y += self.speed


#игровая сцена
win_width = 600
win_height = 500
window = display.set_mde(win_width, win_height)

back = (200, 255, 255)
window.fill(back)


racket1 = Player('racket.png', 30, 200, 4, 50, 150 )
racket2 = Player('racket.png', 520, 200, 4, 50, 150 )
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50 )

font,init()
font = font.Font(None, 35)
lose1 = font.render('ИГРОК 1 ПРОИГРАЛ', True, (149, 0, 0))
lose2 = font.render('ИГРОК 2 ПРОИГРАЛ', True, (149, 0, 0))

#Флаги. отвеч за сост игры



































