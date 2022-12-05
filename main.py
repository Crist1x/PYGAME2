import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30


    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (x * self.cell_size + self.left,
                                 y * self.cell_size + self.top,
                                 self.cell_size, self.cell_size), 1)
    
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        x, y = (mouse_pos[0] - self.left) // self.cell_size, \
        (mouse_pos[1] - self.top) // self.cell_size
        if self.width >= x + 1 > 0 and self.height >= y + 1 > 0:
            return x + 1, y + 1

    def on_click(self, cell_coords):
        print("Была выбрана ячейка:", cell_coords)


def main():
    pygame.init()
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Клетчатое поле')
    board = Board(5, 7)
    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приёма и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
            # РЕАКЦИЯ НА ОСТАЛЬНЫЕ СОБЫТИЯ
            # ...
        # отрисовка и изменение свойств объектов
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
