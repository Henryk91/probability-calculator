import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kargs):
    self.contents = []
    for key, value in kargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, drawAmount):
    amount = drawAmount
    if drawAmount > len(self.contents):
      amount = len(self.contents)
    random.shuffle(self.contents)
    random.shuffle(self.contents)
    ret = self.contents[:amount]
    self.contents = self.contents[amount:]
    ret.reverse()
    return ret

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  correct_count = 0
  for i in range(num_experiments):
    new_hat = copy.copy(hat)
    drawn_balls = new_hat.draw(num_balls_drawn)
    match = True
    for key, value in expected_balls.items():
      ball_count = 0
      for ball in drawn_balls:
        if ball == key:
          ball_count += 1
      if ball_count < value:
        match = False
        break
    
    if match == True:
      correct_count +=1
    
  return (correct_count/num_experiments)