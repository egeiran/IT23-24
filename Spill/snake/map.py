from figure import Figure

class Map():
    def __init__(self, screen, width, height, tile_size) -> None:
        self.screen = screen
        self.width = width
        self.height = height
        self.tile_size = tile_size
    
    def make_map(self):
        map = []
        p = 1
        for i in range(self.width // self.tile_size):
            for o in range(self.width // self.tile_size):
                p = p * -1
                if p == 1:
                    color = (0,255,0)
                else:
                    color = (0,180,0)
                print(i,o)
                figur = Figure(i, o, color, 50)
                figur.rect.width = 50
                map.append(figur)
        return map
        