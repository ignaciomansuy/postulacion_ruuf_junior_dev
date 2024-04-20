
def grid_size(horizontal_length: int, vertical_length: int, x: int, y: int, cx: int=0, cy: int=0):
  return (x // horizontal_length - cx) * (y // vertical_length - cy)


def get_rects_right(horizontal_length: int, vertical_length: int, x: int, y: int, c: int=0):
  return grid_size( vertical_length, horizontal_length,
                    x - horizontal_length * (x // horizontal_length - c),
                    vertical_length * (y // vertical_length))
  
def get_rects_bottom(horizontal_length: int, vertical_length: int, x: int, y: int, c: int=0):
  return grid_size( vertical_length, horizontal_length,
                    x,
                    y % vertical_length + c * vertical_length)


def helper(horizontal_length: int, vertical_length: int, x: int, y: int):
  # All optimal solutions are made of 1 big grid, and then 0 or 1 column and/or row of little rects rotated in 90°
  big_grid = grid_size(horizontal_length, vertical_length, x, y)
  rects_right_big_grid = get_rects_right(horizontal_length, vertical_length, x, y)
  rects_bottom_big_grid = get_rects_bottom(horizontal_length, vertical_length, x, y)
  
  rects_with_big_grid = rects_right_big_grid + rects_bottom_big_grid + big_grid
  
  # There are some cases were the optimal solution requires to not put the biggest initial grid
  
  rects_right_small_grid = get_rects_right(horizontal_length, vertical_length, x, y, c=1)
  rects_bottom_small_grid = get_rects_bottom(horizontal_length, vertical_length, x, y, c=1)
  
  
  a = [rects_with_big_grid,
    grid_size(horizontal_length, vertical_length, x, y, cx=1) + rects_right_small_grid + rects_bottom_big_grid,
    grid_size(horizontal_length, vertical_length, x, y, cy=1) + rects_right_big_grid + rects_bottom_small_grid,
    grid_size(horizontal_length, vertical_length, x, y, cx=1, cy=1) + rects_right_small_grid + rects_bottom_small_grid,]
    
  
  return max(
    a
  )
  


def max_amount_of_rects_in_rect(a: int, b: int , x: int, y: int):
  
  option1 = helper(a, b, x, y)
  option2 = helper(b, a, x, y)
  
  return option1 if option1 >= option2 else option2
      
    
  
      
    
max_amount_of_rects_in_rect(16, 21, 100, 140)