import pygame


class Button:

    def __init__(self, screen, text, pos, font, bg="black"):
        self.screen = screen
        self.x, self.y = pos
        self.text_value = text
        self.text = text
        self.font = pygame.font.SysFont("Arial", font)
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        self.screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.text, bg="red")
                    
    def button_activity(self):
        a, b = pygame.mouse.get_pos()
        if self.x <= a <= self.x + 110 and self.y <= b <= self.y + 60:
            pygame.draw.rect(self.screen, (227, 207, 87), self)
        else:
            pygame.draw.rect(self.screen, (165, 42, 42), self)
        self.screen.blit(self.surface, (self.x + 1, self.y + 1))
