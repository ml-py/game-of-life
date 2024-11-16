def count_neighbours( neighbours ):
    return  sum( neighbours )

def is_alive(  was_alive,  num_neighbours  ):
    if  was_alive:        return 2 <= num_neighbours <= 3
    else         :        return      num_neighbours == 3

def get_sixteen_neighbours(  board,  ii,  jj  )-> list :
	result = []
	for  x  in  board[  ii-1  ][  jj-1  :  jj+2        ]:        result.append(x)
	for  x  in  board[  ii    ][  jj-1  :  jj+2  :  2  ]:        result.append(x)
	for  x  in  board[  ii+1  ][  jj-1  :  jj+2        ]:        result.append(x)
	return result

world_size_X,  world_size_Y  = 10, 10
world = [     [ 0 for x in range( world_size_X ) ]
          for         y in range( world_size_Y )    ]

world[5][5] = 1
world[5][6] = 1
world[5][7] = 1

# print( True == 1 )
# print( True is 1 )
""" SyntaxWarning:   "is" with a literal.   Did you mean  "==" ?    print( True is 1 )"""