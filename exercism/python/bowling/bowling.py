class BowlingGame(object):
    def __init__(self):
        self.num_frame = 1
        self.frames = {1: []}
        self.num_throw = 0
        self.fill_balls = False
        self.score_pts = 0

    def new_frame(self):
        self.num_throw = 0
        self.num_frame += 1
        self.frames[self.num_frame] = []
        if self.num_frame > 10:
            raise IndexError("Max. number of frames is 10! (Without fill)")

    def roll(self, pins):
        if pins > 10:
            raise ValueError

        if self.num_frame == 10 and pins == 10:
            self.fill_balls = True

        # if self.num_frame == 10 and self.fill_balls and :
        #     print('tu sam')

        if self.fill_balls and len(self.frames[10]) < 3:
            self.frames[10].append(pins)
            self.num_throw += 1

        if self.num_frame == 10 and self.num_throw == 1 and self.frames[10][0] + pins == 10:
            self.frames[self.num_frame].append(pins)
            self.fill_balls = True

        if not self.fill_balls:
            if self.num_throw == 2:
                self.new_frame()

            if pins == 10 and self.num_frame != 10:
                self.frames[self.num_frame] = [pins]
                self.new_frame()

            else:
                self.frames[self.num_frame].append(pins)
                self.num_throw += 1

    def score(self):
        if self.frames.get(10) and len(self.frames.get(10)) == 1 and sum(self.frames[10]) == 10:
            raise IndexError

        if self.frames.get(10) and len(self.frames.get(10)) == 2 and sum(self.frames[10]) == 20:
            raise IndexError

        if self.frames.get(10) and len(self.frames.get(10)) == 2 and sum(self.frames[10]) == 10:
            raise IndexError

        score = 0
        if len(self.frames) < 10:
            raise IndexError
        print(self.frames)
        for f in self.frames:
            if f == 10 and self.frames[f][0] == 10:
                for sc in self.frames[f]:
                    score += sc
            elif self.frames[f][0] == 10:
                if len(self.frames[f + 1]) > 1:
                    score += 10 + self.frames[f + 1][0] + self.frames[f + 1][1]
                else:
                    score += 10 + self.frames[f + 1][0] + self.frames[f + 2][0]
            else:
                for sc in self.frames[f]:
                    score += sc
        self.score_pts = score
        return self.score_pts


if __name__ == '__main__':
    game = BowlingGame()
    # rolls = [3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]
    # rolls = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    # rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 10]
    # rolls = [10, 10, 10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 6]
    # rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 6, 10]
    rolls = [5, 5, 3, 7, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i,roll in enumerate(rolls):
        game.roll(roll)

    print(game.score())
