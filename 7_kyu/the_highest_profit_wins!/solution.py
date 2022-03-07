def min_max(lst):
  low_high = []
  low_position = lst[0]
  high_position = lst[0]
  #setting things up 
  for number in lst: 
        if (number < low_position):
            low_position = number
        if (number > high_position):
            high_position = number # tracked the lowest number AND highest number and assigned them to values
  low_high.extend([low_position, high_position]) # had to use extend since append can only add one value at a time - use square brackets to extend it more than one
  return low_high
