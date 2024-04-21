
def grid_size(horizontal_length: int, vertical_length: int, x: int, y: int, cx: int=0, cy: int=0):
  return (x // horizontal_length - cx) * (y // vertical_length - cy)


def get_rects_right_to_bottom(horizontal_length: int, vertical_length: int, x: int, y: int, c: int=0):
  return grid_size( vertical_length, horizontal_length,
                    x - horizontal_length * (x // horizontal_length - c),
                    y)
  
def get_rects_bottom(horizontal_length: int, vertical_length: int, x: int, y: int, cx: int=0, cy: int=0):
  return grid_size( vertical_length, horizontal_length,
                    horizontal_length * (x // horizontal_length - cx),
                    y % vertical_length + cy * vertical_length)


def helper(horizontal_length: int, vertical_length: int, x: int, y: int):
  # All optimal solutions are made of 1 big grid, and then 0 or 1 column and/or row of little rects rotated in 90°
  big_grid = grid_size(horizontal_length, vertical_length, x, y)
  
  grid_minus_1_horizontally = grid_size(horizontal_length, vertical_length, x, y, cx=1)
  grid_minus_1_vertically = grid_size(horizontal_length, vertical_length, x, y, cy=1)
  
  amounts_of_columns = x // horizontal_length
  amounts_of_rows = y // vertical_length 
  
  if (x - horizontal_length * amounts_of_columns) // vertical_length == 0 and \
      (x - horizontal_length * (amounts_of_columns - 1)) // vertical_length >= 1:
      grid_minus_1_horizontally += get_rects_right_to_bottom(horizontal_length, vertical_length, x, y, c=1)
      
  temp = get_rects_right_to_bottom(horizontal_length, vertical_length, x, y)
  big_grid += temp
  grid_minus_1_vertically += temp
  
  if (y - vertical_length * amounts_of_rows) // horizontal_length == 0 and \
      (y - vertical_length * (amounts_of_rows - 1) // horizontal_length >= 1):
      grid_minus_1_vertically += get_rects_bottom(horizontal_length, vertical_length, x, y, cy=1)
  
  temp = get_rects_bottom(horizontal_length, vertical_length, x, y)
  big_grid += temp
  grid_minus_1_horizontally += temp
  
  return max(big_grid, grid_minus_1_horizontally, grid_minus_1_vertically)
  


def max_amount_of_rects_in_rect(a: int, b: int , x: int, y: int):
  
  option1 = helper(a, b, x, y)
  option2 = helper(b, a, x, y)
  
  return max(option1, option2)

      
    
max_amount_of_rects_in_rect(16, 21, 105, 133)