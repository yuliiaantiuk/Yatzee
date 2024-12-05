import random
import pygame

pygame.init()

WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Yahtzee!")
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 18)
background = (128, 128, 128)
white = (255, 255, 255)
black = (0, 0, 0)
game_over = False
rounds_played = 0
total_rounds = 13
players_played = 0
total_played = 2

class Player:
    def __init__(self, name):
        self.name = name
        self.roll = False
        self.rolls_left = 3
        self.dice_selected = [False, False, False, False, False]
        self.selected_choice = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.possible = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.done = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.totals = [0, 0, 0, 0, 0, 0, 0]
        self.clicked = -1
        self.current_score = 0
        self.something_selected = False
        self.bonus_time = False
        self.numbers = [0, 0, 0, 0, 0]

user = Player("User")
computer = Player("Computer")
players = [user, computer]
current_player = players[0]

class Dice:
    def __init__(self, x_pos, y_pos, num, key, player):
        global dice_selected
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.num = num
        self.key = key
        self.die = ''
        self.selected = player.dice_selected[key]
        self.player = player

    def draw(self):
        self.die = pygame.draw.rect(screen, white, [self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.num == 1:
            pygame.draw.circle(screen, black, [self.x_pos + 50, self.y_pos + 50], 10)
        if self.num == 2:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 20], 10)
        if self.num == 3:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 20], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 50, self.y_pos + 50], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 80], 10)
        if self.num == 4:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 20], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 20], 10)
        if self.num == 5:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 20], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 50, self.y_pos + 50], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 20], 10)
        if self.num == 6:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 20], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 50], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 50], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 20], 10)
        if self.selected:
            self.die = pygame.draw.rect(screen, (255, 0, 0), [self.x_pos, self.y_pos, 100, 100], 4, 5)

    def check_click(self, coordinates):
        if self.die.collidepoint(coordinates):
            if self.player.dice_selected[self.key]:
                self.player.dice_selected[self.key] = False
            elif not self.player.dice_selected[self.key]:
                self.player.dice_selected[self.key] = True


class Choice:
    def __init__(self, x_pos, y_pos, text, select, is_possible, is_done, score1, score2):
        global selected_choice
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.select = select
        self.is_possible = is_possible
        self.is_done = is_done
        self.score1 = score1
        self.score2 = score2

    def draw(self):
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos), (self.x_pos + 290, self.y_pos), 2)
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos + 30), (self.x_pos + 290, self.y_pos + 30), 2)

        if not self.is_done:
            if self.is_possible:
                my_text = my_text = font.render(self.text, True, (80, 200, 96))
            elif not self.is_possible:
                my_text = my_text = font.render(self.text, True, (250, 0, 55))
        else:
            my_text = font.render(self.text, True, black)
        if self.select:
            pygame.draw.rect(screen, (20, 35, 30), [self.x_pos, self.y_pos, 155, 30])
        screen.blit(my_text, (self.x_pos + 5, self.y_pos + 10))
        score_text1 = font.render(str(self.score1), True, (0, 0, 255))
        screen.blit(score_text1, (self.x_pos + 165, self.y_pos + 10))
        score_text2 = font.render(str(self.score2), True, (0, 0, 255))
        screen.blit(score_text2, (self.x_pos + 238, self.y_pos + 10))

def draw_static_stuff():
    global game_over
    if game_over:
        restart_txt = font.render('Click to restart', True, white)
        screen.blit(restart_txt, (370, 280))

    roll_txt = font.render('Roll the Dice!', True, white)
    screen.blit(roll_txt, (100, 165))

    rolls_left_txt = font.render('Rolls left this turn: ' + str(current_player.rolls_left), True, white)
    screen.blit(rolls_left_txt, (15, 15))

    accept_txt = font.render('Accept Turn', True, white)
    screen.blit(accept_txt, (390, 165))

    turns_txt = font.render(str(rounds_played), True, white)
    screen.blit(turns_txt, (WIDTH - 20, 15))

    player_txt = font.render(current_player.name, True, white)
    screen.blit(player_txt, (WIDTH - 100, HEIGHT - 40))

    pygame.draw.rect(screen, white, [0, 200, 290, HEIGHT - 200])
    pygame.draw.line(screen, black, (0, 40), (WIDTH, 40), 3)
    pygame.draw.line(screen, black, (0, 200), (WIDTH, 200), 3)
    pygame.draw.line(screen, black, (155, 200), (155, HEIGHT), 3)
    pygame.draw.line(screen, black, (225, 200), (225, HEIGHT), 3)
    pygame.draw.line(screen, black, (290, 200), (290, HEIGHT), 3)

def check_possibilities(possible_lst, numbers_lst):
    possible_lst[0] = True
    possible_lst[1] = True
    possible_lst[2] = True
    possible_lst[3] = True
    possible_lst[4] = True
    possible_lst[5] = True
    possible_lst[12] = True
    max_count = 0

    for i in range (1, 7):
        if numbers_lst.count(i) > max_count:
            max_count = numbers_lst.count(i)

    if max_count >= 3:
        possible_lst[6] = True
        if max_count >= 4:
            possible_lst[7] = True
            if max_count == 5:
                possible_lst[11] = True

    if max_count < 3:
        possible_lst[6] = False
        possible_lst[7] = False
        possible_lst[8] = False
        possible_lst[11] = False
    elif max_count == 3:
        possible_lst[7] = False
        possible_lst[11] = False
        checker = False
        for i in range (len(numbers_lst)):
            if numbers_lst.count(numbers_lst[i]) == 2:
                possible_lst[8] = True
                checker = True
        if not checker:
            possible_lst[8] = False
    elif max_count == 4:
        possible_lst[11] = False

    lowest = 10
    highest = 0
    for i in range(len(numbers_lst)):
        if numbers_lst[i] < lowest:
            lowest = numbers_lst[i]
        if numbers_lst[i] > highest:
            highest = numbers_lst[i]

    if (lowest + 1 in numbers_lst) and (lowest + 2 in numbers_lst) and (lowest + 3 in numbers_lst) and (lowest + 4 in numbers_lst):
        possible_lst[10] = True
    else:
        possible_lst[10] = False

    if ((lowest + 1 in numbers_lst) and (lowest + 2 in numbers_lst) and (lowest + 3 in numbers_lst)) or \
            ((highest - 1 in numbers_lst) and (highest - 2 in numbers_lst) and (highest - 3 in numbers_lst)):
        possible_lst[9] = True
    else:
        possible_lst[9] = False

    return possible_lst

def make_choice(clicked_num, selected_lst, done_lst):
    for i in range(len(selected_lst)):
        selected_lst[i] = False
    if not done_lst[clicked_num]:
        selected_lst[clicked_num] = True
    return selected_lst

def update_game_status():
    global game_over, rounds_played, total_rounds, players_played, total_played
    if players_played >= total_played:
        players_played = 0
        rounds_played += 1
    if rounds_played >= total_rounds:
        game_over = True

def check_scores(selected_choice_lst, numbers_lst, possible_lst, current_score):
    active = 0
    for i in range(len(selected_choice_lst)):
        if selected_choice_lst[i]:
            active = i
    if active == 0:
        current_score = numbers_lst.count(1)
    elif active == 1:
        current_score = numbers_lst.count(2) * 2
    elif active == 2:
        current_score = numbers_lst.count(3) * 3
    elif active == 3:
        current_score = numbers_lst.count(4) * 4
    elif active == 4:
        current_score = numbers_lst.count(5) * 5
    elif active == 5:
        current_score = numbers_lst.count(6) * 6
    elif active == 6 or active == 7:
        if possible_lst[active]:
            current_score = sum(numbers_lst)
        else:
            current_score = 0
    elif active == 8:
        if possible_lst[active]:
            current_score = 25
        else:
            current_score = 0
    elif active == 9:
        if possible_lst[active]:
            current_score = 30
        else:
            current_score = 0
    elif active == 10:
        if possible_lst[active]:
            current_score = 40
        else:
            current_score = 0
    elif active == 11:
        if possible_lst[active]:
            current_score = 50
        else:
            current_score = 0
    elif active == 12:
        current_score = sum(numbers_lst)
    return current_score

def check_totals(score_lst, bonus):
    current_player.totals[0] = score_lst[0] + score_lst[1] + score_lst[2] + score_lst[3] + score_lst[4] + score_lst[5]
    if current_player.totals[0] >= 63:
        current_player.totals[1] = 35
    else:
        current_player.totals[1] = 0
    current_player.totals[2] = current_player.totals[0] + current_player.totals[1]
    if bonus:
        current_player.totals[3] += 100
    current_player.totals[4] = score_lst[6] + score_lst[7] + score_lst[8] + score_lst[9] + score_lst[10] + score_lst[11] + score_lst[12] + current_player.totals[3]
    current_player.totals[5] = current_player.totals[2]
    current_player.totals[6] = current_player.totals[4] + current_player.totals[5]

def restart_game():
    global game_over
    global rounds_played
    global players_played
    global user
    global computer
    global players
    global current_player

    user = Player("User")
    computer = Player("Computer")
    players = [user, computer]
    current_player = players[0]

    game_over = False
    rounds_played = 0
    players_played = 0

def draw_game_result():
    winner = "No one"
    if user.totals[-1] > computer.totals[-1]:
        winner = "User "
    elif computer.totals[-1] > user.totals[-1]:
        winner = "Computer "
    win_txt = font.render(winner + "wins!", True, white)
    screen.blit(win_txt, (390, 230))

running = True
while running:
    timer.tick(fps)
    screen.fill(background)

    restart_btn = pygame.draw.rect(screen, black, [1000, 1000, 2000, 3000])

    if game_over:
        restart_btn = pygame.draw.rect(screen, black, [300, 275, 280, 30])
        draw_game_result()
    roll_btn = pygame.draw.rect(screen, black, [10, 160, 280, 30])
    accept_btn = pygame.draw.rect(screen, black, [310, 160, 280, 30])

    draw_static_stuff()

    die1 = Dice(10, 50, current_player.numbers[0], 0, current_player)
    die2 = Dice(130, 50, current_player.numbers[1], 1, current_player)
    die3 = Dice(250, 50, current_player.numbers[2], 2, current_player)
    die4 = Dice(370, 50, current_player.numbers[3], 3, current_player)
    die5 = Dice(490, 50, current_player.numbers[4], 4, current_player)

    ones = Choice(0, 200, '1s', current_player.selected_choice[0], current_player.possible[0], current_player.done[0], user.score[0], computer.score[0])
    twos = Choice(0, 230, '2s', current_player.selected_choice[1], current_player.possible[1], current_player.done[1], user.score[1], computer.score[1])
    threes = Choice(0, 260, '3s', current_player.selected_choice[2], current_player.possible[2], current_player.done[2], user.score[2], computer.score[2])
    fours = Choice(0, 290, '4s', current_player.selected_choice[3], current_player.possible[3], current_player.done[3], user.score[3], computer.score[3])
    fives = Choice(0, 320, '5s', current_player.selected_choice[4], current_player.possible[4], current_player.done[4], user.score[4], computer.score[4])
    sixes = Choice(0, 350, '6s', current_player.selected_choice[5], current_player.possible[5], current_player.done[5], user.score[5], computer.score[5])
    upper_total1 = Choice(0, 380, 'Upper Score', False, False, True, user.totals[0], computer.totals[0])
    upper_bonus = Choice(0, 410, 'Bonus if >= 63', False, False, True, user.totals[1], computer.totals[1])
    upper_total2 = Choice(0, 440, 'Upper Total', False, False, True, user.totals[2], computer.totals[2])
    three_kind = Choice(0, 470, '3 of Kind', current_player.selected_choice[6], current_player.possible[6], current_player.done[6], user.score[6],computer.score[6])
    four_kind = Choice(0, 500, '4 of Kind', current_player.selected_choice[7], current_player.possible[7], current_player.done[7], user.score[7], computer.score[7])
    full_house = Choice(00, 530, 'Full House', current_player.selected_choice[8], current_player.possible[8], current_player.done[8], user.score[8], computer.score[8])
    small_straight = Choice(0, 560, 'Sm. Straight', current_player.selected_choice[9], current_player.possible[9], current_player.done[9], user.score[9], computer.score[9])
    large_straight = Choice(0, 590, 'Lg. Straight', current_player.selected_choice[10], current_player.possible[10], current_player.done[10], user.score[10], computer.score[10])
    yahtzee = Choice(0, 620, 'YAHTZEE', current_player.selected_choice[11], current_player.possible[11], current_player.done[11], user.score[11], computer.score[11])
    chance = Choice(0, 650, 'Chance', current_player.selected_choice[12], current_player.possible[12], current_player.done[12], user.score[12], computer.score[12])
    bonus = Choice(0, 680, 'YAHTZEE Bonus', False, False, True, user.totals[3], computer.totals[3])
    lower_total1 = Choice(0, 710, 'Lower Total', False, False, True, user.totals[4], computer.totals[4])
    lower_total2 = Choice(0, 740, 'Upper Total', False, False, True, user.totals[5], computer.totals[5])
    grand_total = Choice(0, 770, 'Grand Total', False, False, True, user.totals[6], computer.totals[6])

    current_player.possible = check_possibilities(current_player.possible, current_player.numbers)
    current_player.current_score = check_scores(current_player.selected_choice, current_player.numbers, current_player.possible, current_player.current_score)

    if True in current_player.selected_choice:
        current_player.something_selected = True

    die1.draw()
    die2.draw()
    die3.draw()
    die4.draw()
    die5.draw()

    ones.draw()
    twos.draw()
    threes.draw()
    fours.draw()
    fives.draw()
    sixes.draw()
    upper_total1.draw()
    upper_bonus.draw()
    upper_total2.draw()
    three_kind.draw()
    four_kind.draw()
    full_house.draw()
    small_straight.draw()
    large_straight.draw()
    yahtzee.draw()
    chance.draw()
    bonus.draw()
    lower_total1.draw()
    lower_total2.draw()
    grand_total.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            die1.check_click(event.pos)
            die2.check_click(event.pos)
            die3.check_click(event.pos)
            die4.check_click(event.pos)
            die5.check_click(event.pos)

            if 0 <= event.pos[0] <= 155:
                if 200 <= event.pos[1] <= 380 or 470 <= event.pos[1] <= 680:
                    if 200 < event.pos[1] <= 230:
                        current_player.clicked = 0
                    if 230 < event.pos[1] <= 260:
                        current_player.clicked = 1
                    if 260 < event.pos[1] <= 290:
                        current_player.clicked = 2
                    if 290 < event.pos[1] <= 320:
                        current_player.clicked = 3
                    if 320 < event.pos[1] <= 350:
                        current_player.clicked = 4
                    if 350 < event.pos[1] <= 380:
                        current_player.clicked = 5
                    if 470 < event.pos[1] <= 500:
                        current_player.clicked = 6
                    if 500 < event.pos[1] <= 530:
                        current_player.clicked = 7
                    if 530 < event.pos[1] <= 560:
                        current_player.clicked = 8
                    if 560 < event.pos[1] <= 590:
                        current_player.clicked = 9
                    if 590 < event.pos[1] <= 620:
                        current_player.clicked = 10
                    if 620 < event.pos[1] <= 650:
                        current_player.clicked = 11
                    if 650 < event.pos[1] <= 680:
                        current_player.clicked = 12
                    current_player.selected_choice = make_choice(current_player.clicked, current_player.selected_choice, current_player.done)


            if roll_btn.collidepoint(event.pos) and current_player.rolls_left > 0:
                current_player.roll = True
                current_player.rolls_left -= 1

            if accept_btn.collidepoint(event.pos) and current_player.rolls_left < 3 and current_player.something_selected:
                if current_player.score[11] == 50 and current_player.done[11] and current_player.possible[11]:
                    current_player.bonus_time = True
                for i in range(len(current_player.selected_choice)):
                    if current_player.selected_choice[i]:
                        current_player.done[i] = True
                        current_player.score[i] = current_player.current_score
                        check_totals(current_player.score, current_player.bonus_time)
                        current_player.selected_choice[i] = False
                for i in range(len(current_player.dice_selected)):
                    current_player.dice_selected[i] = False
                current_player.numbers = [7, 18, 29, 30, 41]
                current_player.something_selected = False
                current_player.rolls_left = 3
                players_played += 1
                if current_player == players[0]:
                    current_player = players[1]
                else:
                    current_player = players[0]
                update_game_status()

            if game_over and restart_btn.collidepoint(event.pos):
                    restart_game()

    if current_player.roll:
        for num in range(len(current_player.numbers)):
            if not current_player.dice_selected[num]:
                current_player.numbers[num] = random.randint(1, 6)
        current_player.roll = False

    pygame.display.flip()
pygame.quit()