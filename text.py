import project_colors


def text_objects(text, font):
    textSurface = font.render(text, True, project_colors.pink)
    return textSurface, textSurface.get_rect()
