import random
from dice import *
from choice import *
from util import *
from player import *
from ai import *

rounds_played = 0
players_played = 0
user = Player("User")
computer = Player("Computer")
players = [user, computer]
current_player = players[0]
game_over = False

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


if __name__ == '__main__':
    running = True
    while running:
        timer.tick(fps)
        screen.fill(background)

        restart_btn = pygame.draw.rect(screen, black, [1000, 1000, 2000, 3000])

        if game_over:
            restart_btn = pygame.draw.rect(screen, black, [300, 275, 280, 30])
            restart_txt = font.render('Click to restart', True, white)
            screen.blit(restart_txt, (370, 280))
            draw_game_result()

        roll_btn = pygame.draw.rect(screen, black, [10, 160, 280, 30])
        accept_btn = pygame.draw.rect(screen, black, [310, 160, 280, 30])

        draw_static_stuff(current_player, rounds_played)

        die1 = Dice(10, 50, current_player.numbers[0], 0, current_player)
        die2 = Dice(130, 50, current_player.numbers[1], 1, current_player)
        die3 = Dice(250, 50, current_player.numbers[2], 2, current_player)
        die4 = Dice(370, 50, current_player.numbers[3], 3, current_player)
        die5 = Dice(490, 50, current_player.numbers[4], 4, current_player)

        dice = [die1, die2, die3, die4, die5]

        ones = Choice(0, 200, '1s', current_player.selected_choice[0], current_player.possible[0],
                      current_player.done[0], user.score[0], computer.score[0])
        twos = Choice(0, 230, '2s', current_player.selected_choice[1], current_player.possible[1],
                      current_player.done[1], user.score[1], computer.score[1])
        threes = Choice(0, 260, '3s', current_player.selected_choice[2], current_player.possible[2],
                        current_player.done[2], user.score[2], computer.score[2])
        fours = Choice(0, 290, '4s', current_player.selected_choice[3], current_player.possible[3],
                       current_player.done[3], user.score[3], computer.score[3])
        fives = Choice(0, 320, '5s', current_player.selected_choice[4], current_player.possible[4],
                       current_player.done[4], user.score[4], computer.score[4])
        sixes = Choice(0, 350, '6s', current_player.selected_choice[5], current_player.possible[5],
                       current_player.done[5], user.score[5], computer.score[5])
        upper_total1 = Choice(0, 380, 'Upper Score', False, False, True, user.totals[0], computer.totals[0])
        upper_bonus = Choice(0, 410, 'Bonus if >= 63', False, False, True, user.totals[1], computer.totals[1])
        upper_total2 = Choice(0, 440, 'Upper Total', False, False, True, user.totals[2], computer.totals[2])
        three_kind = Choice(0, 470, '3 of Kind', current_player.selected_choice[6], current_player.possible[6],
                            current_player.done[6], user.score[6], computer.score[6])
        four_kind = Choice(0, 500, '4 of Kind', current_player.selected_choice[7], current_player.possible[7],
                           current_player.done[7], user.score[7], computer.score[7])
        full_house = Choice(00, 530, 'Full House', current_player.selected_choice[8], current_player.possible[8],
                            current_player.done[8], user.score[8], computer.score[8])
        small_straight = Choice(0, 560, 'Sm. Straight', current_player.selected_choice[9], current_player.possible[9],
                                current_player.done[9], user.score[9], computer.score[9])
        large_straight = Choice(0, 590, 'Lg. Straight', current_player.selected_choice[10], current_player.possible[10],
                                current_player.done[10], user.score[10], computer.score[10])
        yahtzee = Choice(0, 620, 'YAHTZEE', current_player.selected_choice[11], current_player.possible[11],
                         current_player.done[11], user.score[11], computer.score[11])
        chance = Choice(0, 650, 'Chance', current_player.selected_choice[12], current_player.possible[12],
                        current_player.done[12], user.score[12], computer.score[12])
        bonus = Choice(0, 680, 'YAHTZEE Bonus', False, False, True, user.totals[3], computer.totals[3])
        lower_total1 = Choice(0, 710, 'Lower Total', False, False, True, user.totals[4], computer.totals[4])
        lower_total2 = Choice(0, 740, 'Upper Total', False, False, True, user.totals[5], computer.totals[5])
        grand_total = Choice(0, 770, 'Grand Total', False, False, True, user.totals[6], computer.totals[6])

        current_player.possible = check_possibilities(current_player.possible, current_player.numbers)
        current_player.current_score = check_scores(current_player.selected_choice, current_player.numbers,
                                                    current_player.possible, current_player.current_score)

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
                        current_player.selected_choice = make_choice(current_player.clicked,
                                                                     current_player.selected_choice,
                                                                     current_player.done)

                if roll_btn.collidepoint(event.pos) and current_player.rolls_left > 0:
                    current_player.roll = True
                    current_player.rolls_left -= 1

                if accept_btn.collidepoint(
                        event.pos) and current_player.rolls_left < 3 and current_player.something_selected:
                    if current_player.score[11] == 50 and current_player.done[11] and current_player.possible[11]:
                        current_player.bonus_time = True
                    for i in range(len(current_player.selected_choice)):
                        if current_player.selected_choice[i]:
                            current_player.done[i] = True
                            current_player.score[i] = current_player.current_score
                            check_totals(current_player.score, current_player.bonus_time, current_player)
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
                    players_played, rounds_played, game_over = update_game_status(players_played, rounds_played, game_over)

                if game_over and restart_btn.collidepoint(event.pos):
                    restart_game()

        if current_player.roll:
            for num in range(len(current_player.numbers)):
                if not current_player.dice_selected[num]:
                    current_player.numbers[num] = random.randint(1, 6)
            current_player.roll = False

        pygame.display.flip()
    pygame.quit()
