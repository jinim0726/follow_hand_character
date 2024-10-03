from pico2d import *
import random

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
# xlenght : 64 / ylenght : 64

quit = False
character_x = 800 // 2
character_y = 600 // 2
character_speed = 0.1
character_dir = 0
hand_x = 800 // 2
hand_y = 600 // 2
frame = 0

def catch_hand():
    global character_x, character_y, hand_x, hand_y
    if 2 > character_x - hand_x and -2 < character_x - hand_x and 2 > character_y - hand_y and -2 < character_y - hand_y:
        return True
    else:
        return False
    

def move_hand():
    global hand_x, hand_y
    hand_x = random.randint(0, 800)
    hand_y = random.randint(0, 600)

def move_character():
    global character_x, character_y, character_speed, character_dir, hand_x, hand_y
    if character_x - hand_x < 0:
        character_dir = 0
    elif character_x - hand_x > 0:
        character_dir = 2
    else:
        if character_y - hand_y < 0:
            character_dir = 3
        elif character_y - hand_y > 0:
            character_dir = 1
        else:
            character_dir = 1
    character_x = character_x + character_speed * (hand_x - character_x)
    character_y = character_y + character_speed * (hand_y - character_y)
    
def stop_file():
    global quit
    events = get_events()
    for event in events:
        # fill here
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                quit = True

# fill here
while not quit:
    clear_canvas()
    grass.draw(400, 90)
    hand.draw(hand_x, hand_y)
    character.clip_draw(frame*64, character_dir*64 , 64, 64, character_x, character_y, 100, 100)
    update_canvas()
    stop_file()
    if catch_hand():
        move_hand()
    move_character()
    frame = (frame + 1) % 8
    delay(0.05)
    #게임종료 : ESC

close_canvas()

