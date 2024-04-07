
class Button():
    def __init__(self, pos, textInput, font, baseColor, hoveringColor):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.baseColor = baseColor
        self.hoveringColor = hoveringColor
        self.textInput = textInput
        self.text = self.font.render(self.textInput, True, self.baseColor)
        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.text, self.rect)

    def checkForInput(self, position):
        return self.rect.collidepoint(position)

    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.textInput, True, self.hoveringColor)
        else:
            self.text = self.font.render(self.textInput, True, self.baseColor)


