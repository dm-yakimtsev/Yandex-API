import sys
import pygame
import requests


def get_image(params):
    map_request = f"https://static-maps.yandex.ru/1.x/?{params['ll']}&{params['z']}&{params['size']}&{params['l']}"
    response = requests.get(map_request)

    if not response:
        raise Exception

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


pygame.init()
params = {
    'll': 'll=55.118102,51.766388',
    'z': 'z=19',
    'size': 'size=500,450',
    'l': 'l=sat'
}
size = 500, 450
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
img = pygame.image.load(get_image(params)).convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                params['z'] = f"z={int(params['z'][2:]) + 1}"
                try:
                    params['z'] = f"z={int(params['z'][2:]) + 1}"
                    img = pygame.image.load(get_image(params)).convert()
                except Exception:
                    print("Invalid z")
            elif event.key == pygame.K_DOWN:
                try:
                    params['z'] = f"z={int(params['z'][2:]) - 1}"
                    img = pygame.image.load(get_image(params)).convert()
                except Exception:
                    print("Invalid z")

    screen.fill((0, 0, 0))
    screen.blit(img, (0, 0))
    pygame.display.flip()

pygame.quit()
