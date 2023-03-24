
def goto_setpos_type(lines, turtle_name='t'):
  # turtle_name is name of variable which stores your turtle. by default it will be 't'
  sequence = []
  for points in lines:
    # extracted points nested in the list
    x1, y1, x2, y2 = points[0]
    # add commands to sequence
    sequence.append('{0}.setposition({1},{2})'.format(turtle_name, x1, y1))
    sequence.append('{0}.goto({1},{2})'.format(turtle_name, x2, y2))
  return sequence

def goto_type(lines, turtle_name='t'):
  # turtle_name is name of variable which stores your turtle. by default it will be 't'
  sequence = []
  for points in lines:
    # extracted points nested in the list
    x1, y1, x2, y2 = points[0]
    # add commands to sequence
    sequence.append('{0}.penup()'.format(turtle_name))
    sequence.append('{0}.goto({1},{2})'.format(turtle_name, x1, y1))
    sequence.append('{0}.pendown()'.format(turtle_name))
    sequence.append('{0}.goto({1},{2})'.format(turtle_name, x2, y2))
  return sequence

def move_spin_type(lines, turtle_name='t'):
  # turtle_name is name of variable which stores your turtle. by default it will be 't'
  sequence = []
  for points in lines:
    # extracted points nested in the list
    x1, y1, x2, y2 = points[0]
    # add commands to sequence
    sequence.append('{0}.penup()'.format(turtle_name))
    sequence.append('{0}.right({0}.towards({1},{2}))'.format(turtle_name, x1, y1))
    sequence.append('{0}.forward({0}.distance({1},{2}))'.format(turtle_name, x1, y1))
    sequence.append('{0}.right({0}.towards({1},{2}))'.format(turtle_name, x2, y2))
    sequence.append('{0}.pendown()'.format(turtle_name))
    sequence.append('{0}.forward({0}.distance({1},{2}))'.format(turtle_name, x2, y2))
  return sequence

