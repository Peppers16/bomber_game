import pygame as pg
import sys

pg.init()

PX_P_BLOCK = 20
SCREEN_HEIGHT_BLOCKS = 30

BUILDING_COLR = (0, 0, 255)
PLANE_COLR = (255, 0, 0)
BG_COLR = (0, 0, 0)

FRAMES = 10


class Skyline:
    def __init__(self, height_list: list, screen: pg.Surface = None):
        self.screen = screen
        self.buildings = [Building(height=h, index=i, skyline=self) for i, h in enumerate(height_list)]
        self.plane = Plane(skyline=self)


class Building:
    def __init__(self, height: int, index: int, skyline: Skyline):
        self.skyline = skyline
        self.height = height
        self.index = index
        self.rect = pg.Rect(
            self.index * PX_P_BLOCK  # left
            , (SCREEN_HEIGHT_BLOCKS-self.height) * PX_P_BLOCK  # top
            , PX_P_BLOCK  # width
            , self.height * PX_P_BLOCK  # height
        )
        self.skyline.screen.fill(BUILDING_COLR, self.rect)


class Plane:
    def __init__(self, skyline: Skyline):
        self.x = 0
        self.y = SCREEN_HEIGHT_BLOCKS
        self.rect = pg.Rect(0, 0, PX_P_BLOCK, PX_P_BLOCK)
        self.skyline = skyline
        self.skyline.screen.fill(PLANE_COLR, self.rect)

    def move(self):
        self.x += 1
        if self.x > len(self.skyline.buildings)-1:
            self.x = 0
            self.y -= 1
        self._update_screen()

    def _update_screen(self):
        self.skyline.screen.fill(BG_COLR, self.rect)
        self.rect = pg.Rect(
            self.x * PX_P_BLOCK
            , (SCREEN_HEIGHT_BLOCKS - self.y) * PX_P_BLOCK
            , PX_P_BLOCK, PX_P_BLOCK
        )
        self.skyline.screen.fill(PLANE_COLR, self.rect)


def main(height_list: list):
    clock = pg.time.Clock()
    screen = pg.display.set_mode((len(height_list) * PX_P_BLOCK, SCREEN_HEIGHT_BLOCKS*PX_P_BLOCK))
    skyline = Skyline(height_list=height_list, screen=screen)
    pg.display.update()
    while True:
        for event in pg.event.get():  # check one event, leave other events on the queue
            if event.type == pg.QUIT:
                sys.exit()
        skyline.plane.move()
        pg.display.update()
        clock.tick(FRAMES)


if __name__ == '__main__':
    main([10, 8, 5, 3, 1, 0, 11, 15, 2, 0, 5])
