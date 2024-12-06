from util import check_possibilities, make_choice, check_scores, check_totals
import random

class AI:
    def __init__(self, player):
        self.player = player

    def take_turn(self):
        while self.player.rolls_left > 0:
            # Roll dice
            for i in range(len(self.player.numbers)):
                if not self.player.dice_selected[i]:
                    self.player.numbers[i] = random.randint(1, 6)
            self.player.rolls_left -= 1

            # Evaluate possibilities
            self.player.possible = check_possibilities(self.player.possible, self.player.numbers)
            best_choice = self.choose_best_option()

            if best_choice is not None:
                self.player.clicked = best_choice
                self.player.selected_choice = make_choice(best_choice, self.player.selected_choice, self.player.done)
                break

        # Finalize the choice
        if self.player.selected_choice:
            for i in range(len(self.player.selected_choice)):
                if self.player.selected_choice[i]:
                    self.player.done[i] = True
                    self.player.score[i] = check_scores(self.player.selected_choice, self.player.numbers,
                                                        self.player.possible, self.player.current_score)
                    check_totals(self.player.score, self.player.bonus_time, self.player)
                    self.player.selected_choice[i] = False
            self.player.rolls_left = 3
            self.player.dice_selected = [False] * len(self.player.dice_selected)

    def choose_best_option(self):
        # Find the best scoring category that's possible
        best_choice = None
        best_score = 0
        for i in range(len(self.player.possible)):
            if self.player.possible[i] and not self.player.done[i]:
                score = check_scores([True if j == i else False for j in range(len(self.player.possible))],
                                     self.player.numbers, self.player.possible, self.player.current_score)
                if score > best_score:
                    best_score = score
                    best_choice = i
        return best_choice
