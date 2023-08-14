import pygame

pygame.init()

COLOR_INACTIVE = pygame.Color("lightskyblue3")
COLOR_ACTIVE = pygame.Color("dodgerblue2")
FONT = pygame.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, name, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.name = name
        self.text = text
        self.txt_surface = FONT.render(text, True, pygame.Color("forestgreen"))
        self.active = False

    def handle_event(self, event, button):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            if button.rect.collidepoint(event.pos) and button.text_value == "Change color":
                print(f"From input {self.name} cached color: {self.text}")
                self.text = ''
            if button.rect.collidepoint(event.pos) and button.text_value == "Catch values":
                print(f"From input {self.name} cached value: {self.text}")
                self.text = ''
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(150, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def show(self, screen, game_font):
        game_font.render_to(screen, (self.rect.x + 5, self.rect.y - 20), self.name, (255, 250, 240))
        self.txt_surface.blit(self.txt_surface, self.rect)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

