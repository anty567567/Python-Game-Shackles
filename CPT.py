import random
import pygame
import sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800, 640))
clock = pygame.time.Clock()


# -------------- TEXT SETTINGS --------------
class Colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARK_CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
TITLE_FONT = pygame.font.SysFont("impact", 40)
DIALOGUE_FONT = pygame.font.SysFont("impact", 18)
DIALOGUE_FONT2 = pygame.font.SysFont("impact", 14)


# -------------- CHARACTER STATS\Variables --------------
character = pygame.Rect(64, 64, 32, 32)
character_hp = 30
maximum_hp = 30
rusty_dagger_dmg = 1
enemy_hp = 30
exp = 0
heal = 3
parry_chance = 20
flee_chance = 10
character_move_up = False
character_move_left = False
character_move_right = False
character_move_down = False
character_x = character.left
character_y = character.top
lvl = 0
door_open = False
battle = 0
wake_up = False
door_accept = False
silver_key = False
key_accept = False
final_stage = 0
character1 = pygame.image.load("Character1.png")
character1_shooting = pygame.image.load("Character1 Shooting.png")
barrel = pygame.image.load("Barrel.png")
fence_closed_upwards = pygame.image.load("Fencelol.png")
fence_open_left = pygame.image.load("Fencelol left.png")
fence_open_right = pygame.image.load("Fencelol right.png")
stone_floor = pygame.image.load("stone floor.png")
fence_open_up = pygame.image.load("Fencelol up.png")
fence_open_down = pygame.image.load("Fencelol down.png")
fence_closed_right = pygame.image.load("Fencelol rightwall.png")
fence_closed_left = pygame.image.load("Fencelol leftwall.png")
fence_open_leftup = pygame.image.load("Fencelol leftup.png")
fence_open_leftdown = pygame.image.load("Fencelol leftdown.png")
logo = pygame.image.load("Fade.png").convert()
fade2 = pygame.image.load("fade2.png").convert()
bed = pygame.transform.rotate(pygame.image.load("Bed.png"), 90)
rock = pygame.image.load("Rock.png")
rock_big = pygame.image.load("Rock_BIG.png")
rock_big_hurt = pygame.image.load("Rock_BIG_HURT.png").convert()
character1_big = pygame.image.load("Character1_BIG.png")
character1_shooting_big = pygame.image.load("Character1 Shooting_BIG.png")
character_heal = pygame.image.load("Heal.png")
heal_aura = pygame.image.load("Heal_aura.png")
rock_mossy = pygame.image.load("Rock_mossy.png")
rock_mossy_big = pygame.image.load("Rock_mossy_BIG.png")
rock_bomb = pygame.image.load("Rock_bomb.png")
rock_bomb_big = pygame.image.load("Rock_bomb_BIG.png")
boulder = pygame.image.load("Boulder.png")
boulder_big = pygame.image.load("Boulder_BIG.png")
boulder_big_hurt = pygame.image.load("Boulder_BIG_hurt.png").convert()
rockboss = pygame.image.load("rockboss.png")
room = [1, 1]
times = 0
enemies = 0
x = 0
y = 0
walls = []
cell_doors = []
doors = []
doors_open_area = []
interact_objects = []
interact_objects_area = []
transfer_rooms_down = []
transfer_rooms_up = []
transfer_rooms_left = []
transfer_rooms_right = []
shooting = False
current_room = []
loaded_game = False
rock_list = []
mossy_rock_list = []
bomb_rock_list = []
boulder_list = []
boss = False
win_game = False


# --------------- NEW GAME ----------------
def reset_to_new_game():
    global TITLE_FONT, enemy_hp, room, character_move_down, character_hp, lvl, exp, maximum_hp, character_move_left, character_move_up, character_move_right, door_open
    global character, battle, wake_up, door_open, door_accept, silver_key, key_accept, shooting, final_stage, character1, character1_shooting, barrel, fence_closed_upwards
    global fence_open_left, fence_open_right, stone_floor, fence_open_up, fence_open_down, fence_closed_right, fence_closed_left, fence_open_leftup, fence_open_leftdown
    global logo, fade2, bed, room, times, enemies, x, y, walls, cell_doors, doors, doors_open_area, interact_objects, interact_objects_area
    global transfer_rooms_down, transfer_rooms_up, transfer_rooms_left, transfer_rooms_right, character_x, character_y, current_room
    global rusty_dagger_dmg, boss, heal, parry_chance, flee_chance, loaded_game, rock_list, mossy_rock_list, bomb_rock_list, boulder_list
    character = pygame.Rect(64, 64, 32, 32)
    character_hp = 30
    maximum_hp = 30
    rusty_dagger_dmg = 1
    enemy_hp = 30
    exp = 0
    heal = 3
    parry_chance = 20
    flee_chance = 10
    character_move_up = False
    character_move_left = False
    character_move_right = False
    character_move_down = False
    character_x = character.left
    character_y = character.top
    lvl = 0
    door_open = False
    battle = 0
    wake_up = False
    door_accept = False
    silver_key = False
    key_accept = False
    boss = False
    final_stage = 0
    room = [1, 1]
    times = 0
    enemies = 0
    x = 0
    y = 0
    walls = []
    cell_doors = []
    doors = []
    doors_open_area = []
    interact_objects = []
    interact_objects_area = []
    transfer_rooms_down = []
    transfer_rooms_up = []
    transfer_rooms_left = []
    transfer_rooms_right = []
    shooting = False
    current_room = []
    loaded_game = False
    rock_list = []
    mossy_rock_list = []
    bomb_rock_list = []
    boulder_list = []


# ---------------- INSTRUCTIONS SCREEN ------------------
def show_instructions():
    global TITLE_FONT
    instructions_screen = TITLE_FONT.render("Instructions", True, (255, 255, 255))

    while True:
        clock.tick(60)

        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

        # Game state changes
        screen.fill((0, 0, 0))
        screen.blit(instructions_screen, (50, 50))
        screen.blit(DIALOGUE_FONT.render("Warning! Pressing \"New Game\" will delete your old game.", True, (255, 255, 255)),
                    (100, 150))
        screen.blit(DIALOGUE_FONT.render("Pressing \"Load Game\" will load your last game.", True, (255, 255, 255)),
                    (100, 200))
        screen.blit(DIALOGUE_FONT.render("Press the \"Esc\" key to escape to the Main Menu at any point in the game.", True, (255, 255, 255)), (100, 250))
        screen.blit(DIALOGUE_FONT.render("To move your character, use the arrow keys.", True, (255, 255, 255)), (100, 300))
        screen.blit(DIALOGUE_FONT.render("Your game is automatically saved when you escape to the Main Menu.", True, (255, 255, 255)),
                    (100, 350))
        screen.blit(DIALOGUE_FONT.render("To interact with an object or select an option, press \"Z\".", True, (255, 255, 255)), (100, 400))
        screen.blit(DIALOGUE_FONT.render("Press \"Esc\" to go back to the Main Menu.", True, (255, 255, 255)), (400, 500))

        # Update display
        pygame.display.update()


# ----------------- LEVEL UP----------------------
def level_up():
    global rusty_dagger_dmg, character_hp, heal, parry_chance, flee_chance, maximum_hp, lvl, screen
    level_up_pos = [1, 1]
    level_up_pos_y = 460
    level_up_pos_x = 275
    attack_level = False
    parry_level = False
    heal_level = False
    flee_level = False
    while True:
        clock.tick(60)

        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # Menu Navigation
                if event.key == K_z:
                    if level_up_pos[0] == 1 and level_up_pos[1] == 1:
                        attack_level = True
                    elif level_up_pos[0] == 1 and level_up_pos[1] == 2:
                        parry_level = True
                    elif level_up_pos[0] == 2 and level_up_pos[1] == 1:
                        heal_level = True
                    elif level_up_pos[0] == 2 and level_up_pos[1] == 2:
                        flee_level = True
                elif event.key == K_UP:
                    level_up_pos[1] -= 1
                    level_up_pos_y -= 100
                    if level_up_pos[1] < 1:
                        level_up_pos[1] = 2
                    if level_up_pos_y < 460:
                        level_up_pos_y = 560
                elif event.key == K_DOWN:
                    level_up_pos[1] += 1
                    level_up_pos_y += 100
                    if level_up_pos[1] >= 3:
                        level_up_pos[1] = 1
                    if level_up_pos_y > 560:
                        level_up_pos_y = 460

                elif event.key == K_LEFT:
                    level_up_pos[0] -= 1
                    level_up_pos_x -= 200
                    if level_up_pos[0] < 1:
                        level_up_pos[0] = 2
                    if level_up_pos_x < 275:
                        level_up_pos_x = 475
                elif event.key == K_RIGHT:
                    level_up_pos[0] += 1
                    level_up_pos_x += 200
                    if level_up_pos[0] >= 3:
                        level_up_pos[0] = 1
                    if level_up_pos_x > 475:
                        level_up_pos_x = 275

        if attack_level:
            rusty_dagger_dmg += 1
            maximum_hp += 5
            lvl += 1
            attack_level = False
            break
        if parry_level:
            parry_chance += 5
            maximum_hp += 5
            lvl += 1
            parry_level = False
            break
        if heal_level:
            heal += 1
            maximum_hp += 5
            lvl += 1
            heal_level = False
            break
        if flee_level:
            flee_chance += 5
            maximum_hp += 5
            lvl += 1
            flee_level = False
            break
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (level_up_pos_x, level_up_pos_y), (level_up_pos_x + 20, level_up_pos_y))
        screen.blit(DIALOGUE_FONT.render("Level Attack", True, (255, 255, 255)), (300, 450))
        screen.blit(DIALOGUE_FONT.render("Level Heal", True, (255, 255, 255)), (500, 450))
        screen.blit(DIALOGUE_FONT.render("Level Parry", True, (255, 255, 255)), (300, 550))
        screen.blit(DIALOGUE_FONT.render("Level Flee", True, (255, 255, 255)), (500, 550))
        pygame.display.update()


# ---------------- ENEMY ENCOUNTER ---------------
def battle_sequence():
    global character_hp, rusty_dagger_dmg, screen, enemy_hp, exp, character_move_down, character_move_left, encounter_over
    global character_move_right, win_game, boss, win_game, character_move_up, maximum_hp, door_open, battle_rock, battle_mossy_rock, battle_bomb_rock, battle_boulder
    character_move_up = False
    character_move_left = False
    character_move_right = False
    character_move_down = False
    cage_guard = False
    enemy_intro = False
    enemy_type = 0
    enemy_hp = 2
    enemy_dmg = 1
    timer_attack = 0
    timer_heal = 0
    enemy_attacked = False
    laser_x = 315
    laser_y = 243
    heal_effect = False
    if not door_open:
        enemy_hp = 10
        cage_guard = True
        enemy_dmg = 1
    elif room == [3, 3]:
        boss = True
        enemy_hp = 50
        enemy_dmg = 5
    elif not cage_guard:
        enemy_type = random.choice([0, 0, 1, 2, 3])
        if battle_rock:
            enemy_type = 0
            battle_rock = False
            encounter_over = True
        elif battle_mossy_rock:
            enemy_type = 3
            battle_mossy_rock = False
            encounter_over = True
        elif battle_bomb_rock:
            enemy_type = 1
            battle_bomb_rock = False
            encounter_over = True
        elif battle_boulder:
            enemy_type = 2
            battle_boulder = False
            encounter_over = True
        if room[0] == 1 and room[1] == 1 and not cage_guard:
            enemy_type = 0
        if enemy_type == 0:
            enemy_hp = 5
            enemy_dmg = 2
        elif enemy_type == 1:
            enemy_hp = 1
            enemy_dmg = 10
        elif enemy_type == 2:
            enemy_hp = 20
            enemy_dmg = 1
        elif enemy_type == 3:
            enemy_hp = 15
            enemy_dmg = 2
        enemy_intro = True
    enemy_vulnerable = False
    enemy_heal = 0
    heals = 5
    flee = 100
    # MENU NAVIGATION SYSTEM
    battle_menu_pos = [1, 1]
    battle_menu_pos_y = 460
    battle_menu_pos_x = 275
    while character_hp > 0 and enemy_hp > 0:
        clock.tick(60)

        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # Menu Navigation
                if event.key == K_z:
                    if cage_guard:
                        cage_guard = False
                    elif enemy_intro:
                        enemy_intro = False
                    elif battle_menu_pos[0] == 1 and battle_menu_pos[1] == 1:
                        if not enemy_vulnerable:
                            enemy_attacked = True
                            enemy_hp -= rusty_dagger_dmg
                            character_hp -= enemy_dmg
                        elif enemy_vulnerable:
                            enemy_hp -= rusty_dagger_dmg*3
                            enemy_vulnerable = False
                    elif battle_menu_pos[0] == 1 and battle_menu_pos[1] == 2:
                        parry = random.randint(0, 100)
                        if parry < parry_chance:
                            enemy_vulnerable = True
                        else:
                            character_hp -= enemy_dmg
                            enemy_vulnerable = False
                    elif battle_menu_pos[0] == 2 and battle_menu_pos[1] == 1 and heals > 0:
                        character_hp += heal
                        character_hp -= enemy_dmg
                        heals -= 1
                        enemy_vulnerable = False
                        heal_effect = True
                    elif battle_menu_pos[0] == 2 and battle_menu_pos[1] == 2:
                        flee = random.randint(1, 100)
                        character_hp -= enemy_dmg
                        enemy_vulnerable = False
                elif event.key == K_UP:
                    battle_menu_pos[1] -= 1
                    battle_menu_pos_y -= 100
                    if battle_menu_pos[1] < 1:
                        battle_menu_pos[1] = 2
                    if battle_menu_pos_y < 460:
                        battle_menu_pos_y = 560
                elif event.key == K_DOWN:
                    battle_menu_pos[1] += 1
                    battle_menu_pos_y += 100
                    if battle_menu_pos[1] >= 3:
                        battle_menu_pos[1] = 1
                    if battle_menu_pos_y > 560:
                        battle_menu_pos_y = 460
                elif event.key == K_LEFT:
                    battle_menu_pos[0] -= 1
                    battle_menu_pos_x -= 200
                    if battle_menu_pos[0] < 1:
                        battle_menu_pos[0] = 2
                    if battle_menu_pos_x < 275:
                        battle_menu_pos_x = 475
                elif event.key == K_RIGHT:
                    battle_menu_pos[0] += 1
                    battle_menu_pos_x += 200
                    if battle_menu_pos[0] >= 3:
                        battle_menu_pos[0] = 1
                    if battle_menu_pos_x > 475:
                        battle_menu_pos_x = 275
        if flee < flee_chance:
            break

        if enemy_type == 3 and enemy_hp <= 3 and enemy_heal != 2:
            enemy_hp += 5
            enemy_heal += 1

        # Game state changes
        screen.fill((0, 0, 0))
        # enemy dialogue
        if cage_guard:
            screen.blit(DIALOGUE_FONT2.render("WHAAAAA??? HOW DID YOU GET OUT OF YOUR CELL??? ", True, (255, 255, 255)),
                        (50, 550))
            screen.blit(DIALOGUE_FONT2.render("'Attack' does your damage to the enemy", True, (255, 255, 255)), (400, 100))
            screen.blit(DIALOGUE_FONT2.render("'Heal' heals you, but can only be used 5 times", True, (255, 255, 255)), (400, 150))
            screen.blit(DIALOGUE_FONT2.render("'Parry' gives you a chance to parry your opponent", True, (255, 255, 255)), (400, 200))
            screen.blit(DIALOGUE_FONT2.render("and leave them vulnerable", True, (255, 255, 255)), (400, 215))
            screen.blit(DIALOGUE_FONT2.render("'Flee' gives you a chance to escape battle", True, (255, 255, 255)), (400, 250))
        elif enemy_intro:
            if enemy_type == 0:
                screen.blit(DIALOGUE_FONT2.render("You trip over a rock. It wants to fight!", True, (255, 255, 255)), (50, 550))
            elif enemy_type == 1:
                screen.blit(DIALOGUE_FONT2.render("You encounter a rock. WITH A BOMB!!!", True, (255, 255, 255)), (50, 550))
            elif enemy_type == 2:
                screen.blit(DIALOGUE_FONT2.render("You encounter a boulder.", True, (255, 255, 255)), (50, 550))
            elif enemy_type == 3:
                screen.blit(DIALOGUE_FONT2.render("You encounter a mossy rock.", True, (255, 255, 255)), (50, 550))
        elif not enemy_intro or not cage_guard:
            pygame.draw.line(screen, (255, 255, 255), (battle_menu_pos_x, battle_menu_pos_y),
                             (battle_menu_pos_x + 20, battle_menu_pos_y))
            screen.blit(DIALOGUE_FONT.render("Attack", True, (255, 255, 255)), (300, 450))
            screen.blit(DIALOGUE_FONT.render("Heal", True, (255, 255, 255)), (500, 450))
            screen.blit(DIALOGUE_FONT.render("Parry", True, (255, 255, 255)), (300, 550))
            screen.blit(DIALOGUE_FONT.render("Flee", True, (255, 255, 255)), (500, 550))
            screen.blit(DIALOGUE_FONT.render(("HP" + str(character_hp)), True, (255, 255, 255)), (100, 400))
            screen.blit(DIALOGUE_FONT.render(("ENEMY HP" + str(enemy_hp)), True, (255, 255, 255)), (600, 100))
            if enemy_type == 0:
                if enemy_attacked:
                    timer_attack += 1
                    screen.blit(rock_big, (470, 200, 192, 192))
                    if timer_attack <= 15:
                        screen.blit(character1_shooting_big, (200, 200))
                        pygame.draw.rect(screen, (252, 11, 11), (laser_x, laser_y, 15, 5))
                        laser_x += 3
                    if enemy_attacked and timer_attack >= 15:
                        rock_big_hurt.set_alpha(180)
                        screen.blit(rock_big_hurt, (470, 200, 192, 192))
                        screen.blit(character1_big, (200, 200))
                        laser_x = 315
                    if timer_attack == 45:
                        enemy_attacked = False
                        timer_attack = 0
                else:
                    screen.blit(rock_big, (470, 200))
                    screen.blit(character1_big, (200, 200))

            if enemy_type == 1:
                if enemy_attacked:
                    timer_attack += 1
                    screen.blit(rock_bomb_big, (470, 200, 192, 192))
                    if timer_attack <= 15:
                        screen.blit(character1_shooting_big, (200, 200))
                        pygame.draw.rect(screen, (252, 11, 11), (laser_x, laser_y, 15, 5))
                        laser_x += 3
                    if enemy_attacked and timer_attack >= 15:
                        rock_big_hurt.set_alpha(180)
                        screen.blit(rock_big_hurt, (470, 200, 192, 192))
                        screen.blit(character1_big, (200, 200))
                        laser_x = 315
                    if timer_attack == 45:
                        enemy_attacked = False
                        timer_attack = 0
                else:
                    screen.blit(rock_bomb_big, (470, 200))
                    screen.blit(character1_big, (200, 200))

            if enemy_type == 2:
                if enemy_attacked:
                    timer_attack += 1
                    screen.blit(boulder_big, (460, 180, 192, 192))
                    if timer_attack <= 15:
                        screen.blit(character1_shooting_big, (200, 200))
                        pygame.draw.rect(screen, (252, 11, 11), (laser_x, laser_y, 15, 5))
                        laser_x += 3
                    if enemy_attacked and timer_attack >= 15:
                        boulder_big_hurt.set_alpha(180)
                        screen.blit(boulder_big_hurt, (460, 180, 192, 192))
                        screen.blit(character1_big, (200, 200))
                        laser_x = 315
                    if timer_attack == 45:
                        enemy_attacked = False
                        timer_attack = 0
                else:
                    screen.blit(boulder_big, (460, 180))
                    screen.blit(character1_big, (200, 200))

            if enemy_type == 3:
                if enemy_attacked:
                    timer_attack += 1
                    screen.blit(rock_mossy_big, (470, 200, 192, 192))
                    if timer_attack <= 15:
                        screen.blit(character1_shooting_big, (200, 200))
                        pygame.draw.rect(screen, (252, 11, 11), (laser_x, laser_y, 15, 5))
                        laser_x += 3
                    if enemy_attacked and timer_attack >= 15:
                        rock_big_hurt.set_alpha(180)
                        screen.blit(rock_big_hurt, (470, 200, 192, 192))
                        screen.blit(character1_big, (200, 200))
                        laser_x = 315
                    if timer_attack == 45:
                        enemy_attacked = False
                        timer_attack = 0
                else:
                    screen.blit(rock_mossy_big, (470, 200))
                    screen.blit(character1_big, (200, 200))

        if heal_effect:
            timer_heal += 1
            screen.blit(character_heal, (160, 200))
            screen.blit(heal_aura, (200, 200))
            if timer_heal == 30:
                timer_heal = 0
                heal_effect = False

        if enemy_vulnerable:
            screen.blit(DIALOGUE_FONT.render("ENEMY IS VULNERABLE!", True, (255, 255, 255)), (200, 100))
        if enemy_hp <= 0:
            exp += 10
            if boss:
                win_game = True
            if character_hp > maximum_hp:
                character_hp = maximum_hp
            cage_guard = False
        # Update display
        pygame.display.update()


# ------------- SAVE GAME --------------
def save_game():
    global room, character_x, character_y, character_hp, lvl, exp, rusty_dagger_dmg, heal, flee_chance, parry_chance, door_open
    f = open('load_game.txt', 'w')
    f.write(str(room[0]) + '/')
    f.write(str(room[1]) + '/')
    f.write(str(character.left) + '/')
    f.write(str(character.top) + '/')
    f.write(str(character_hp) + '/')
    f.write(str(lvl) + '/')
    f.write(str(exp) + '/')
    f.write(str(rusty_dagger_dmg) + '/')
    f.write(str(heal) + '/')
    f.write(str(flee_chance) + '/')
    f.write(str(parry_chance) + '/')
    f.write(str(door_open))
    f.close()


# ------------- LOAD GAME --------------
def load_game():
    global room, character_x, character_y, character_hp, lvl, exp, rusty_dagger_dmg, heal, flee_chance, parry_chance, character, times, loaded_game
    global door_open
    s = open('load_game.txt', 'r')
    load_list = s.read().split('/')
    room[0] = int(load_list[0])
    room[1] = int(load_list[1])
    character_x = int(load_list[2])
    character_y = int(load_list[3])
    character_hp = int(load_list[4])
    lvl = int(load_list[5])
    exp = int(load_list[6])
    rusty_dagger_dmg = int(load_list[7])
    heal = int(load_list[8])
    flee_chance = int(load_list[9])
    parry_chance = int(load_list[10])
    door_open = load_list[11]
    times = 0
    loaded_game = True
    character = pygame.Rect(character_x, character_y, 32, 32)
    play_game()


# ------------- ROOMS --------------
room_one = []
room_one.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_one.append("w q o o o bo b c o o o o o o o o o o o o o o b b w".split())
room_one.append("w q o o o bo bo c o o o o o o o o o o o o o o b b w".split())
room_one.append("w o o o o do do c o o o o o o o o o o o o o o o o w".split())
room_one.append("w c c c c cdl cdr c o o o o o o o o r o o o o o o o w".split())
room_one.append("w b b o o o o o o o o o o o o o o o o o o o o o w".split())
room_one.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_one.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_one.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_one.append("w o o o o o o o o o o o o o o o o o o o o o o o rdu".split())
room_one.append("w o o o o o o o o o o o o o o o o o o o o o o o rdd".split())
room_one.append("w o o o o o o o o o o o o o o o o o o o r o o o w".split())
room_one.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_one.append("w b o o o o o o o o r o o o o o o o o o o o o o w".split())
room_one.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_one.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_one.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_one.append("w o o o o o o o o o o o o o o o o r o o o o o b w".split())
room_one.append("w o b b o o o o o o o o o o o o o o o o o b b b w".split())
room_one.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_two = []
room_two.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_two.append("w b b o o o o o o o o o o o o o o o o o o o b b w".split())
room_two.append("w o o o o o o o o o o o o o o o o o o o o o b b w".split())
room_two.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_two.append("w o o o o o o mr o o o o o o o o o o o r o o o o w".split())
room_two.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_two.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_two.append("w o o r o o o o o o o o o o o o o o o o o o o o w".split())
room_two.append("w o o o o o o o o o o o o o mr o o o o o o o o o w".split())
room_two.append("ldu o o o o o o o o o o o o o o o o o o o o o o o rdu".split())
room_two.append("ldd o o o o o o o o o o o o o o o o o o o o o o o rdd".split())
room_two.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_two.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_two.append("w b o o o o o r o o o o o o o o r o o o o o o o w".split())
room_two.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_two.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_two.append("w b r o o o o o o o o mr o o o o o o o o o o o o w".split())
room_two.append("w o o o o o o o o o o o o o o o o o o o o o o b w".split())
room_two.append("w o b b o o o o o o o o o o o o o o o o o b b b w".split())
room_two.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_three = []
room_three.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_three.append("w b b b o o o o o o o o o o o o o o o o o o b b w".split())
room_three.append("w o o o o o o o o o o o o o o o o o o o o o b b w".split())
room_three.append("w o o o o r o o o o o o o o o o o o o o o o o o w".split())
room_three.append("w o o o o o o o o o o o o o o mr o o o o o o o o w".split())
room_three.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_three.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_three.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_three.append("w o o o o o o r o o o o o o o o o o br o o o o o w".split())
room_three.append("ldu o o o o o o o o o o o o o o o o o o o o o o o rdu".split())
room_three.append("ldd o o o o o o o o o o o o o o o o o o o o o o o rdd".split())
room_three.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_three.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_three.append("w b o o o o o o o o o o o o o o o o o r o o o o w".split())
room_three.append("w o o o o o mr o o o o o o o o o o o o o o o o o w".split())
room_three.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_three.append("w b o o o o o o o o o br o o o o o o o o o o o o w".split())
room_three.append("w o o o o o o o o o o o o o o o o o o o o o o b w".split())
room_three.append("w o b b o o o o o o o o o o o o o o o o o b b b w".split())
room_three.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_four = []
room_four.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_four.append("w b b b b o o o o o o o o o o o o o o o o o b b w".split())
room_four.append("w o o o o o o o o o o o o o r o o o o o o o b b w".split())
room_four.append("w o o o bdr o o o o o o o o o o o o o o o o o o o w".split())
room_four.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_four.append("w b o o o o o o o o o o o o o o o o o o o mr o o w".split())
room_four.append("w b o o o o o o o r o o o o o o o o o o o o o o w".split())
room_four.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_four.append("w o o o o o o o o o o o o o o r o o o o o o o o w".split())
room_four.append("ldu o o o o o o o o o o o o o o o o o o o o o o o rdu".split())
room_four.append("ldd o o o o o o o o o o o o o o o o o o o o o o o rdd".split())
room_four.append("w o o br o o o o o o o o o o o o o o o o o o o o w".split())
room_four.append("w b o o o o o o o o o o o o o o o o o o o bdr o o w".split())
room_four.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_four.append("w o o o o o o o o o o mr o o o o o r o o o o o o w".split())
room_four.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_four.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_four.append("w o o o o o o o o o o o o o o o o o o o o o o b w".split())
room_four.append("w o b b o o o o br o o o o o o o o o o o o b b b w".split())
room_four.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_five = []
room_five.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_five.append("w b b b b b o o o o o o o o o o o o o o o o b b w".split())
room_five.append("w o o o o o o o o o o o o o o o o o o o mr o b b w".split())
room_five.append("w o o o o o bdr o o o o o o o o o o o o o o o o o w".split())
room_five.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_five.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_five.append("w b o o o o o o o o o o o o bdr o o o o o o o o o w".split())
room_five.append("w o o mr o o o o o o o o o o o o o o o o o o o o w".split())
room_five.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_five.append("ldu o o o o o o o o o o o o o o o o bdr o o o o o o w".split())
room_five.append("ldd o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_five.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_five.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_five.append("w b o o bdr o o o o o o o o o o o o o o o o o o o w".split())
room_five.append("w o o o o o o o o o o o o o o o o o o o bdr o o o w".split())
room_five.append("w o o o o o o o o o o o o r o o o o o o o o o o w".split())
room_five.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_five.append("w o o o o o o o o bdr o o o o o o o o o o o o o b w".split())
room_five.append("w o b b o o o o o o o o o o o o o o o o o b b b w".split())
room_five.append("w w w w w w w w w w w w ddl ddr w w w w w w w w w w w".split())
room_six = []
room_six.append("w w w w w w w w w w w w udl udr w w w w w w w w w w w".split())
room_six.append("w b b b b b o o o o o o o o o o o o o o o o b b w".split())
room_six.append("w o o o o b o o o o o o o o o o o o o o o o b b w".split())
room_six.append("w o o o o o o o o bdr o o o o o o o o br o o o o o w".split())
room_six.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_six.append("w b o br o o o o o o o o o bdr o o o o o o o o o o w".split())
room_six.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_six.append("w o o o o o o o o o o o o o o o o o o o o r o o w".split())
room_six.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_six.append("ldu o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_six.append("ldd o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_six.append("w o o o o o o r o o o o o o o br o o o o o o o o w".split())
room_six.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_six.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_six.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_six.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_six.append("w br o o o o o o r o o o o o o o o br o o o o o o w".split())
room_six.append("w o o o o o o o o o o o o o o o o o o o o o o b w".split())
room_six.append("w o b b o o o o o o o o o o o o o o o o o b b b w".split())
room_six.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_seven = []
room_seven.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_seven.append("w b b b b b o o o o o o o o o o o o o o o o b b w".split())
room_seven.append("w o o o b b o o o o o o o o o o o o r o o o b b w".split())
room_seven.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_seven.append("w o o bdr o o o o o o o o o o o o o o o o o o o o w".split())
room_seven.append("w b o o o o o o o o o o br o o o o o o o o o o o w".split())
room_seven.append("w b o o o o o r o o o o o o o o o o o mr o o o o w".split())
room_seven.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_seven.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_seven.append("ldu o o o o o mr o o o o o o o o o o o o br o o o o rdu".split())
room_seven.append("ldd o o o o o o o o o o o o o o o o o o o bdr o o o rdd".split())
room_seven.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_seven.append("w b o o o o o o o o o o o mr o o o o o o o o mr o w".split())
room_seven.append("w b o o o r o o o o o o o o o o o o o o o o o o w".split())
room_seven.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_seven.append("w o o o o o o o o o o r o o o o o o o o o o o o w".split())
room_seven.append("w b mr o o o o o o o o o o o o o o o o o o o o o w".split())
room_seven.append("w o o o o o o o o o o o o o o o o o o bdr o o o b w".split())
room_seven.append("w o b b o o o o o o o o o o o o o o o o o b b b w".split())
room_seven.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_eight_noboss = []
room_eight_noboss.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_eight_noboss.append("w b b b b b o o o o o o o o o o o o o o o o b b w".split())
room_eight_noboss.append("w o o b b b o o o o o o o o o o o br o o o o b b w".split())
room_eight_noboss.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_noboss.append("w o o bdr o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_noboss.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_noboss.append("w b o o o o o o o o o o o o o o o o o o bdr o o o w".split())
room_eight_noboss.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_noboss.append("w o o o o o o o o o bdr o o o o o o o o o o o o o w".split())
room_eight_noboss.append("ldu o o o bdr o o o o o o o o o o o o o o r o o o o rdu".split())
room_eight_noboss.append("ldd o o o o o o o o o o o o o o o o o o o o o o o rdd".split())
room_eight_noboss.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_noboss.append("w b o o o o o o o o o o o o br o o o o o o o o o w".split())
room_eight_noboss.append("w b o o mr o o o o o o o o o o o o o o o o o o o w".split())
room_eight_noboss.append("w o o o o o o r o o o o o o o o o r o o o o o o w".split())
room_eight_noboss.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_noboss.append("w b o o o o o o o o o o bdr o o o o br o o o o o o w".split())
room_eight_noboss.append("w o o o o o o o o o o o o o o o o o o o o o o b w".split())
room_eight_noboss.append("w o b b bdr o o o o o o o o o o o o o o o o b b b w".split())
room_eight_noboss.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_eight_boss = []
room_eight_boss.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_eight_boss.append("w b b b b b o o o o o o o o o o o o o o o o b b w".split())
room_eight_boss.append("w o o b b b o o o o o o o o o o o o o o o o b b w".split())
room_eight_boss.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_boss.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_boss.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_boss.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_boss.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_boss.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_boss.append("ldu o o o o o o o o o o o o o o o o o o o o o o o rdu".split())
room_eight_boss.append("ldd o o o o o o o o o o o o o o o o o o o o o o o rdd".split())
room_eight_boss.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_boss.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_boss.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_boss.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_boss.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_boss.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_eight_boss.append("w o o o o o o o o o o o o o o o o o o o o o o b w".split())
room_eight_boss.append("w o b b o o o o o o o o o o o o o o o o o b b b w".split())
room_eight_boss.append("w w w w w w w w w w w w ddl ddr w w w w w w w w w w w".split())
room_nine = []
room_nine.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_nine.append("w b b b b b o o o o o o o o o o o o o o o o b b w".split())
room_nine.append("w o b b b b o o o o o o o o o o o o o o bdr o b b w".split())
room_nine.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_nine.append("w o o o o o o o o bdr o o o o o o o o o o o o o o w".split())
room_nine.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_nine.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_nine.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_nine.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_nine.append("ldu o o o o o o o o bdr o o o o o o o o o o o o o o rdu".split())
room_nine.append("ldd o o o o o o o o bdr o o o o o o o o o o o o o o rdd".split())
room_nine.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_nine.append("w b o o o o o o o o o o o o o o o o o o mr o o o w".split())
room_nine.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_nine.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_nine.append("w o o o o o o o o o mr o o o o o o o o o o o o o w".split())
room_nine.append("w b o o o o o o o o o o o o o o o o o o bdr o o o w".split())
room_nine.append("w o o o o o o o o o o o o o o o o o o o o o o b w".split())
room_nine.append("w o b b o o o o o o o o o o o o o o o o o b b b w".split())
room_nine.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_ten = []
room_ten.append("w w w w w w w w w w w w udl udr w w w w w w w w w w w".split())
room_ten.append("w b b b b b o o o o o o o o o o o o o o o o b b w".split())
room_ten.append("w b b b b b o o o o o o o o o o o o o o o o b b w".split())
room_ten.append("w o o o o o o o o bdr o o o o o o o mr o o o o o o w".split())
room_ten.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_ten.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_ten.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_ten.append("w o o o o mr o o o o o o o o o o o o o o o o o o w".split())
room_ten.append("w o o o o o o o o o o o o o o o o o o mr o o o o w".split())
room_ten.append("w o o o o o o o o o o bdr o o o o o o o o o o o o rdu".split())
room_ten.append("w o o o o o o o o o o o o o o o o o o o o o o o rdd".split())
room_ten.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_ten.append("w b o o o mr o o o o o o o o o o bdr o o o o o o o w".split())
room_ten.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_ten.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_ten.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_ten.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_ten.append("w o o o o o bdr o o o o o o o o o o o o o o o o b w".split())
room_ten.append("w o b b o o o o o o o o o o o o o o o o o b b b w".split())
room_ten.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())
room_boss = []
room_boss.append("w w w w w w w w w w w w udl udr w w w w w w w w w w w".split())
room_boss.append("w o o o o o o o o o o o o o o o o o o o o o b b w".split())
room_boss.append("w o o o o o o o o o o o o o o o o o o o o o b b w".split())
room_boss.append("w o o b b o o b b b b o o o o b b b b o b b o o w".split())
room_boss.append("w o o b o o o o o o o o o o o o o o o o o b o o w".split())
room_boss.append("w b o b o o o o o o o o o o o o o o o o o b o o w".split())
room_boss.append("w b o o o o o o o o o o o o o o o o o o o o o o w".split())
room_boss.append("w o o o o o o o o o o o o o o o o o o o o o o o w".split())
room_boss.append("w o o b o o o o o o o o o o o o o o o o o b o o w".split())
room_boss.append("w o o b o o o o o bdr bdr bdr mr mr bdr bdr bdr o o o o b o o w".split())
room_boss.append("w o o b o o o o o bdr o o o o o o bdr o o o o b o o w".split())
room_boss.append("w o o b o o o o o bdr o o o o o o bdr o o o o b o o w".split())
room_boss.append("w b o o o o o o o bdr o o o o o o bdr o o o o o o o w".split())
room_boss.append("w b o o b o o o o o bdr bdr bdr bdr bdr bdr o o o o b o o o w".split())
room_boss.append("w o o o o b o o o o o o o o o o o o o b o o o o w".split())
room_boss.append("w o o o o b o b o o o o o o o o o b o b o o o o w".split())
room_boss.append("w b o o o o b o o o b b b b b o o o b o o o o o w".split())
room_boss.append("w o o o o o o o o b o o o o o b o o o o o o o b w".split())
room_boss.append("w o b b o o o o o o o o o o o o o o o o o b b b w".split())
room_boss.append("w w w w w w w w w w w w w w w w w w w w w w w w w".split())


# ---------------- END GAME -------------------
def end_game():
    while True:
        clock.tick(60)

        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_z:
                    pygame.quit()
                    sys.exit()
        screen.blit(TITLE_FONT.render("Shackles", True, (255, 255, 255)), (325, 100))
        screen.blit(TITLE_FONT.render("Press Z to finish", True, (255, 255, 255)), (275, 250))


# ---------------- PLAY GAME ------------------
def play_game():
    global TITLE_FONT, enemy_hp, room, character_move_down, character_hp, lvl, exp, maximum_hp, character_move_left, character_move_up, character_move_right, door_open
    global character, battle, wake_up, door_open, door_accept, silver_key, key_accept, shooting, final_stage, character1, character1_shooting, barrel, fence_closed_upwards
    global fence_open_left, fence_open_right, stone_floor, fence_open_up, fence_open_down, fence_closed_right, fence_closed_left, fence_open_leftup, fence_open_leftdown
    global logo, fade2, bed, room, times, enemies, x, y, walls, cell_doors, doors, doors_open_area, interact_objects, interact_objects_area
    global transfer_rooms_down, transfer_rooms_up, transfer_rooms_left, transfer_rooms_right, character_x, character_y, current_room, loaded_game
    global rock_list, mossy_rock_list, bomb_rock_list, win_game, boulder_list, battle_rock, battle_mossy_rock, battle_bomb_rock, battle_boulder, encounter_over, boulder, rockboss
    if not loaded_game:
        reset_to_new_game()
    battle_rock = False
    battle_mossy_rock = False
    battle_bomb_rock = False
    battle_boulder = False
    encounter_over = False
    pygame.mixer.music.load("Game_Music.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1.0)
    while True:
        clock.tick(60)

        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    save_game()
                    return
                elif event.key == K_z and not wake_up:
                    wake_up = True
                # --------- CHARACTER ACTIONS ----------
                if wake_up:
                    if event.key == K_RIGHT:
                        character_move_right = True
                    elif event.key == K_LEFT:
                        character_move_left = True
                        if room[0] != 1 and room[1] != 1:
                            battle += 1
                    elif event.key == K_UP:
                        character_move_up = True
                        if room[0] != 1 and room[1] != 1:
                            battle += 1
                    elif event.key == K_DOWN:
                        character_move_down = True
                        if room[0] != 1 and room[1] != 1:
                            battle += 1
                    elif event.key == K_z and character.collidelist(doors_open_area) != -1 and silver_key:
                        battle_sequence()
                        door_open = True
                        silver_key = False
                    elif event.key == K_z and door_open:
                        door_accept = True
                    elif event.key == K_z and silver_key:
                        key_accept = True
                    elif event.key == K_z and character.collidelist(interact_objects_area) != -1:
                        silver_key = True
                    elif event.key == K_SPACE:
                        shooting = True
                    elif event.key == K_f:
                        enemy_hp = 0

            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    character_move_right = False
                if event.key == K_LEFT:
                    character_move_left = False
                if event.key == K_UP:
                    character_move_up = False
                if event.key == K_DOWN:
                    character_move_down = False
                if event.key == K_SPACE:
                    shooting = False

        # ---------- CHARACTER MOVEMENT ----------
        if character_move_right:
            character.move_ip(3, 0)
        if character_move_left:
            character.move_ip(-3, 0)
        if character_move_up:
            character.move_ip(0, -3)
        if character_move_down:
            character.move_ip(0, 3)

        for wall in walls:
            if character.colliderect(wall):
                if character_move_up:
                    character.move_ip(0, 3)
                if character_move_down:
                    character.move_ip(0, -3)
                if character_move_left:
                    character.move_ip(3, 0)
                if character_move_right:
                    character.move_ip(-3, 0)

        if not door_open:
            for door in cell_doors:
                if character.colliderect(door):
                    if character_move_up:
                        character.move_ip(0, 3)
                    if character_move_down:
                        character.move_ip(0, -3)
                    if character_move_left:
                        character.move_ip(3, 0)
                    if character_move_right:
                        character.move_ip(-3, 0)

        if not enemy_hp <= 0:
            for door in doors:
                if character.colliderect(door):
                    if character_move_up:
                        character.move_ip(0, 3)
                    if character_move_down:
                        character.move_ip(0, -3)
                    if character_move_left:
                        character.move_ip(3, 0)
                    if character_move_right:
                        character.move_ip(-3, 0)

        for object in interact_objects:
            if character.colliderect(object):
                if character_move_up:
                    character.move_ip(0, 3)
                if character_move_down:
                    character.move_ip(0, -3)
                if character_move_left:
                    character.move_ip(3, 0)
                if character_move_right:
                    character.move_ip(-3, 0)

        # ENCOUNTERS
        if encounter_over:
            for rockie in rock_list:
                if pygame.Rect(character.left, character.top, 32, 32).colliderect(rockie):
                    character.move_ip(16, 16)
                if pygame.Rect(character.right, character.top, 32, 32).colliderect(rockie):
                    character.move_ip(-16, 16)
                if pygame.Rect(character.left, character.bottom, 32, 32).colliderect(rockie):
                    character.move_ip(16, -16)
                if pygame.Rect(character.right, character.bottom, 32, 32).colliderect(rockie):
                    character.move_ip(-16, -16)
            for mrockie in mossy_rock_list:
                if pygame.Rect(character.left, character.top, 32, 32).colliderect(mrockie):
                    character.move_ip(16, 16)
                if pygame.Rect(character.right, character.top, 32, 32).colliderect(mrockie):
                    character.move_ip(-16, 16)
                if pygame.Rect(character.left, character.bottom, 32, 32).colliderect(mrockie):
                    character.move_ip(16, -16)
                if pygame.Rect(character.right, character.bottom, 32, 32).colliderect(mrockie):
                    character.move_ip(-16, -16)
            for brockie in bomb_rock_list:
                if pygame.Rect(character.left, character.top, 32, 32).colliderect(brockie):
                    character.move_ip(16, 16)
                if pygame.Rect(character.right, character.top, 32, 32).colliderect(brockie):
                    character.move_ip(-16, 16)
                if pygame.Rect(character.left, character.bottom, 32, 32).colliderect(brockie):
                    character.move_ip(16, -16)
                if pygame.Rect(character.right, character.bottom, 32, 32).colliderect(brockie):
                    character.move_ip(-16, -16)
            for cboulder in boulder_list:
                if pygame.Rect(character.left, character.top, 32, 32).colliderect(cboulder):
                    character.move_ip(16, 16)
                if pygame.Rect(character.right, character.top, 32, 32).colliderect(cboulder):
                    character.move_ip(-16, 16)
                if pygame.Rect(character.left, character.bottom, 32, 32).colliderect(cboulder):
                    character.move_ip(16, -16)
                if pygame.Rect(character.right, character.bottom, 32, 32).colliderect(cboulder):
                    character.move_ip(-16, -16)
            encounter_over = False

        if character.collidelist(rock_list) != -1:
            battle_rock = True
            battle_sequence()
        elif character.collidelist(mossy_rock_list) != -1:
            battle_mossy_rock = True
            battle_sequence()
        elif character.collidelist(bomb_rock_list) != -1:
            battle_bomb_rock = True
            battle_sequence()
        elif character.collidelist(boulder_list) != -1:
            battle_boulder = True
            battle_sequence()

        # SWITCHING ROOMS
        if character.collidelist(transfer_rooms_down) != -1:
            room[1] += 1
            interact_objects = []
            interact_objects_area = []
            walls = []
            doors = []
            cell_doors = []
            rock_list = []
            mossy_rock_list = []
            bomb_rock_list = []
            boulder_list = []
            times = 0
            character = pygame.Rect(400, 64, 32, 32)
            # FADE BETWEEN SCREENS
            for i in range(256):
                screen.blit(fade2, (0, 0))
                logo.set_alpha(i)
                screen.blit(logo, (0, 0))
                pygame.display.flip()
            for i in range(256):
                screen.fill((0, 0, 0))
                fade2.set_alpha(i)
                screen.blit(fade2, (0, 0))
                pygame.display.flip()
        elif character.collidelist(transfer_rooms_right) != -1:
            room[0] += 1
            interact_objects = []
            interact_objects_area = []
            walls = []
            doors = []
            cell_doors = []
            rock_list = []
            mossy_rock_list = []
            bomb_rock_list = []
            boulder_list = []
            times = 0
            character = pygame.Rect(-32, 300, 32, 32)
            # FADE BETWEEN SCREENS
            for i in range(256):
                screen.blit(fade2, (0, 0))
                logo.set_alpha(i)
                screen.blit(logo, (0, 0))
                pygame.display.flip()
            for i in range(256):
                screen.fill((0, 0, 0))
                fade2.set_alpha(i)
                screen.blit(fade2, (0, 0))
                pygame.display.flip()
        elif character.collidelist(transfer_rooms_left) != -1:
            room[0] -= 1
            interact_objects = []
            interact_objects_area = []
            walls = []
            doors = []
            cell_doors = []
            rock_list = []
            mossy_rock_list = []
            bomb_rock_list = []
            boulder_list = []
            times = 0
            character = pygame.Rect(800, 300, 32, 32)
            # FADE BETWEEN SCREENS
            for i in range(256):
                screen.blit(fade2, (0, 0))
                logo.set_alpha(i)
                screen.blit(logo, (0, 0))
                pygame.display.flip()
            for i in range(256):
                screen.fill((0, 0, 0))
                fade2.set_alpha(i)
                screen.blit(fade2, (0, 0))
                pygame.display.flip()
        elif character.collidelist(transfer_rooms_up) != -1:
            room[1] -= 1
            interact_objects = []
            interact_objects_area = []
            walls = []
            doors = []
            cell_doors = []
            rock_list = []
            mossy_rock_list = []
            bomb_rock_list = []
            boulder_list = []
            times = 0
            character = pygame.Rect(64, 64, 32, 32)
            # FADE BETWEEN SCREENS
            for i in range(256):
                screen.blit(fade2, (0, 0))
                logo.set_alpha(i)
                screen.blit(logo, (0, 0))
                pygame.display.flip()
            for i in range(256):
                screen.fill((0, 0, 0))
                fade2.set_alpha(i)
                screen.blit(fade2, (0, 0))
                pygame.display.flip()

        # ----------- CHECKING FOR CLEAR NORMAL LEVEL -----------
        if final_stage == 0:
            if not (enemies == 0 and room == [1, 2]):
                boss_appear_condition = False
            else:
                boss_appear_condition = True
                final_stage = 1

            # ----------- Obstacle Placement -----------
        # RECT PLACEMENT
        if room[0] == 1 and room[1] == 1:
            current_room = room_one
        elif room[0] == 2 and room[1] == 1:
            current_room = room_two
        elif room[0] == 3 and room[1] == 1:
            current_room = room_three
        elif room[0] == 4 and room[1] == 1:
            current_room = room_four
        elif room[0] == 5 and room[1] == 1:
            current_room = room_five
        elif room[0] == 5 and room[1] == 2:
            current_room = room_six
        elif room[0] == 4 and room[1] == 2:
            current_room = room_seven
        elif room[0] == 3 and room[1] == 2 and not boss_appear_condition:
            current_room = room_eight_noboss
        elif room[0] == 3 and room[1] == 2 and boss_appear_condition:
            current_room = room_eight_boss
        elif room[0] == 2 and room[1] == 2:
            current_room = room_nine
        elif room[0] == 1 and room[1] == 2:
            current_room = room_ten
        elif room[0] == 3 and room[1] == 3:
            current_room = room_boss
            battle = 0

        # RECT DRAWING
        for row in current_room:
            for tile in row:
                if tile == "w":
                    walls.append(pygame.Rect(x, y, 32, 32))
                elif tile == "c":
                    walls.append(pygame.Rect(x, y, 32, 32))
                elif tile == "cdl":
                    cell_doors.append(pygame.Rect(x, y, 32, 32))
                elif tile == "cdr":
                    cell_doors.append(pygame.Rect(x, y, 32, 32))
                elif tile == "do":
                    doors_open_area.append(pygame.Rect(x, y + 16, 32, 16))
                elif tile == "rdu":
                    doors.append(pygame.Rect(x, y, 32, 32))
                    transfer_rooms_right.append(pygame.Rect(x + 64, y, 32, 32))
                elif tile == "rdd":
                    doors.append(pygame.Rect(x, y + 16, 32, 16))
                    transfer_rooms_right.append(pygame.Rect(x + 64, y, 32, 32))
                elif tile == "b":
                    interact_objects.append(pygame.Rect(x, y, 32, 32))
                elif tile == "bo":
                    interact_objects_area.append(pygame.Rect(x, y, 32, 16))
                elif tile == "q":
                    walls.append(pygame.Rect(x, y, 32, 32))
                elif tile == "ldu":
                    doors.append(pygame.Rect(x, y, 32, 32))
                    transfer_rooms_left.append(pygame.Rect(x - 64, y, 32, 32))
                elif tile == "ldd":
                    doors.append(pygame.Rect(x, y + 16, 32, 16))
                    transfer_rooms_left.append(pygame.Rect(x - 64, y, 32, 32))
                elif tile == "ddl":
                    doors.append(pygame.Rect(x, y, 32, 32))
                    transfer_rooms_down.append(pygame.Rect(x, y + 64, 32, 32))
                elif tile == "ddr":
                    doors.append(pygame.Rect(x, y, 32, 32))
                    transfer_rooms_down.append(pygame.Rect(x, y + 64, 32, 32))
                elif tile == "udl":
                    doors.append(pygame.Rect(x, y, 32, 32))
                    transfer_rooms_up.append(pygame.Rect(x, y - 64, 32, 32))
                elif tile == "udr":
                    doors.append(pygame.Rect(x, y, 32, 32))
                    transfer_rooms_up.append(pygame.Rect(x, y - 64, 32, 32))
                elif tile == "r":
                    rock_list.append(pygame.Rect(x, y, 32, 32))
                elif tile == "mr":
                    mossy_rock_list.append(pygame.Rect(x, y, 32, 32))
                elif tile == "br":
                    bomb_rock_list.append(pygame.Rect(x, y, 32, 32))
                elif tile == "bdr":
                    boulder_list.append(pygame.Rect(x, y, 32, 32))
                x += 32
            x = 0
            y += 32
        y = 0
        times = 1
        for row in current_room:
            for tile in row:
                if tile == "w":
                    pygame.draw.rect(screen, (0, 0, 0), ((x, y), (32, 32)))
                elif tile == "b":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    screen.blit(barrel, ((x, y), (32, 32)))
                elif tile == "c":
                    pygame.draw.rect(screen, (64, 64, 64), ((x, y), (32, 32)))
                elif tile == "o":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                elif tile == "cdl":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    if not door_open:
                        screen.blit(fence_closed_upwards, ((x, y), (32, 32)))
                    else:
                        screen.blit(fence_open_left, ((x, y), (32, 32)))
                elif tile == "cdr":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    if not door_open:
                        screen.blit(fence_closed_upwards, ((x, y), (32, 32)))
                    else:
                        screen.blit(fence_open_right, ((x, y), (32, 32)))
                elif tile == "ddl":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    if not enemy_hp <= 0:
                        screen.blit(fence_closed_upwards, ((x, y), (32, 32)))
                    else:
                        screen.blit(fence_open_left, ((x, y), (32, 32)))
                elif tile == "ddr":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    if not enemy_hp <= 0:
                        screen.blit(fence_closed_upwards, ((x, y), (32, 32)))
                    else:
                        screen.blit(fence_open_right, ((x, y), (32, 32)))
                elif tile == "rdu":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    if not enemy_hp <= 0:
                        screen.blit(fence_closed_right, ((x, y), (32, 32)))
                    else:
                        screen.blit(fence_open_up, ((x, y), (32, 32)))
                elif tile == "rdd":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    if not enemy_hp <= 0:
                        screen.blit(fence_closed_right, ((x, y), (32, 32)))
                    else:
                        screen.blit(fence_open_down, ((x, y), (32, 32)))
                elif tile == "ldu":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    if not enemy_hp <= 0:
                        screen.blit(fence_closed_left, ((x, y), (32, 32)))
                    else:
                        screen.blit(fence_open_leftup, ((x, y), (32, 32)))
                elif tile == "ldd":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    if not enemy_hp <= 0:
                        screen.blit(fence_closed_left, ((x, y), (32, 32)))
                    else:
                        screen.blit(fence_open_leftdown, ((x, y), (32, 32)))
                elif tile == "udl":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    if not enemy_hp <= 0:
                        screen.blit(fence_closed_upwards, ((x, y), (32, 32)))
                    else:
                        screen.blit(fence_open_left, ((x, y), (32, 32)))
                elif tile == "udr":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    if not enemy_hp <= 0:
                        screen.blit(fence_closed_upwards, ((x, y), (32, 32)))
                    else:
                        screen.blit(fence_open_right, ((x, y), (32, 32)))
                elif tile == "do":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                elif tile == "bo":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                elif tile == "q":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    screen.blit(bed, ((x, y), (32, 32)))
                elif tile == "r":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    screen.blit(rock, ((x, y), (32, 32)))
                elif tile == "mr":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    screen.blit(rock_mossy, ((x, y), (32, 32)))
                elif tile == "br":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    screen.blit(rock_bomb, ((x, y), (32, 32)))
                elif tile == "bdr":
                    screen.blit(stone_floor, ((x, y), (32, 32)))
                    screen.blit(boulder, ((x, y), (32, 32)))
                x += 32
            x = 0
            y += 32
        y = 0

        # ------------------- CHARACTER DEATH ---------------------------
        if character_hp <= 0:
            room = [1, 1]
            character = pygame.Rect(64, 64, 32, 32)
            character_hp = maximum_hp
            times = 0
            character_move_left = False
            character_move_right = False
            character_move_up = False
            character_move_down = False
            enemy_hp = 0
            interact_objects = []
            interact_objects_area = []
            walls = []
            doors = []
            cell_doors = []
            wake_up = False
        if battle > 500:
            battle_sequence()
            battle = 0
        if exp >= 10 + (int(lvl))*10:
            level_up()
            exp = 0
        if not wake_up:
            screen.blit(DIALOGUE_FONT.render("You wake up in a cell, unable to remember anything.", True,
                                             (255, 255, 255)), (50, 550))
            screen.blit(DIALOGUE_FONT2.render("Move UP: Arrow Key UP", True, (255, 255, 255)), (350, 30))
            screen.blit(DIALOGUE_FONT2.render("Move DOWN: Arrow Key UP", True, (255, 255, 255)), (350, 55))
            screen.blit(DIALOGUE_FONT2.render("Move LEFT: Arrow Key UP", True, (255, 255, 255)), (350, 80))
            screen.blit(DIALOGUE_FONT2.render("Move RIGHT: Arrow Key UP", True, (255, 255, 255)), (350, 105))
            screen.blit(DIALOGUE_FONT.render("(Press Z To Continue)", True, (255, 255, 255)), (350, 130))
        if not key_accept and silver_key:
            screen.blit(DIALOGUE_FONT.render("You found a Silver Key", True, (255, 255, 255)), (100, 550))
        if not door_accept and door_open:
            screen.blit(DIALOGUE_FONT.render("You opened the cell door", True, (255, 255, 255)), (100, 550))
        if win_game:
            end_game()

        # --------- Load Character Image ----------
        if shooting:
            screen.blit(character1_shooting, character)
        else:
            screen.blit(character1, character)
        # Update display
        pygame.display.update()

# ---------------- MENU SCREEN ------------------
title = TITLE_FONT.render("Main Menu", True, (255, 255, 255))
intro = True
Menu_pos = 0
Menu_y_pos = 275
pygame.mixer.music.load("Menu_Music.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(1.0)
while True:
    clock.tick(60)

    # event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            # Menu Navigation
            if event.key == K_z or event.key == K_SPACE:
                if Menu_pos == 0 and not intro:
                    loaded_game = False
                    play_game()
                elif Menu_pos == 1 and not intro:
                    enemy_hp = 0
                    load_game()
                elif Menu_pos == 2 and not intro:
                    show_instructions()
                elif Menu_pos == 3 and not intro:
                    pygame.quit()
                    sys.exit()
                intro = False
            elif event.key == K_UP:
                Menu_pos -= 1
                Menu_y_pos -= 50
                if Menu_pos < 0:
                    Menu_pos = 3
                if Menu_y_pos < 275:
                    Menu_y_pos = 430
            elif event.key == K_DOWN:
                Menu_pos += 1
                Menu_y_pos += 50
                if Menu_pos > 3:
                    Menu_pos = 0
                if Menu_y_pos > 430:
                    Menu_y_pos = 275

    # Game state changes
    screen.fill((0, 0, 0))
    if not intro:
        screen.blit(TITLE_FONT.render("Shackles", True, (255, 255, 255)), (325, 100))
        screen.blit(TITLE_FONT.render("New Game", True, (255, 255, 255)), (300, 250))
        screen.blit(TITLE_FONT.render("Load Game", True, (255, 255, 255)), (300, 300))
        screen.blit(TITLE_FONT.render("Instructions", True, (255, 255, 255)), (300, 350))
        screen.blit(TITLE_FONT.render("Exit Game", True, (255, 255, 255)), (300, 400))
        # MENU NAVIGATION SYSTEM
        pygame.draw.line(screen, (255, 255, 255), (283, Menu_y_pos), (288, Menu_y_pos))
    if intro:
        screen.blit(TITLE_FONT.render("Shackles", True, (255, 255, 255)), (325, 100))
        screen.blit(TITLE_FONT.render("Press Z to start", True, (255, 255, 255)), (275, 250))
    # Update display
    pygame.display.update()

