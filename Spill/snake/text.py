import pygame

class Text:
    def __init__(self, left: int, top: int, width: int, height: int, text: str, font: pygame.font.SysFont,  boxcolor: pygame.color = None, textcolor: pygame.color =(0,0,0), gamestate: str = None) -> None:
        self.rect = pygame.Rect(left, top, width, height)
        self.boxcolor = boxcolor
        self.textcolor = textcolor
        self.font = font
        self.text = text
        self.gamestate = gamestate

    def draw(self, screen):
        if self.boxcolor != None:
            pygame.draw.rect(screen, (0,0,0), (self.rect.left - 2, self.rect.top - 2, self.rect.width + 4, self.rect.height + 4), border_radius=50)
            pygame.draw.rect(screen, self.boxcolor, self.rect, border_radius=50)
        text_surface = self.font.render(self.text, True, self.textcolor)
        text_rect = text_surface.get_rect(center = self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def handle_event(self, event_pos: tuple):
        if self.rect.collidepoint(event_pos):
            return True