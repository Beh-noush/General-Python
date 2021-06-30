from IPython.display import clear_output


def playboard(play_list):
  a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9 = play_list
  print( f'|__{a_1}__|__{a_2}__|__{a_3}__|\n|__{a_4}__|__{a_5}__|__{a_6}__|\n|__{a_7}__|__{a_8}__|__{a_9}__|' )
  
  def user_choice( range, user ):
  choice = 'incorrect'
  within_range = False
  while not choice.isdigit() or within_range == False:
    choice = input(f'{user} Enter a number in {range}')
    if choice.isdigit():
      if int(choice) in range:
        within_range = True
      else:
        print('Your number is not within the range.')
    else:
      print('The input should be a number.')
  return int(choice)

def is_game_won(play_board, marker_1, marker_2):
  num_1, num_2,num_3,num_4,num_5,num_6,num_7,num_8,num_9 = play_board
  win_1 = num_1 == num_2 == num_3  
  win_2 = num_1 == num_4 == num_7 
  win_3 = num_3 == num_6 == num_9  
  win_4 = num_7 == num_8 == num_9   
  win_5 = num_1 == num_5 == num_9  
  win_6 = num_3 == num_5 == num_7  
    
  game_won = win_1 or win_2 or win_3 or win_4 or win_5 or win_6
  if game_won:
    if (win_1 or win_2 or win_5) and num_1 == marker_1:
      winner = marker_1
      #print(f'{player_1}  has won.')
    elif (win_1 or win_2 or win_5) and num_1 == marker_2:
      winner = marker_2
      #print(f'{player_2}  has won.')
    elif (win_3 or win_6) and num_3 == marker_1:
      winner = marker_1
      #print(f'{player_1}  has won.')
    elif (win_3 or win_6) and num_3 == marker_2:
      winner = marker_2
      #print(f'{player_2}  has won.')
    elif win_4 and num_7 == marker_1:
      winner = marker_1
      #print(f'{player_1} has won.')
    else:
      winner = marker_2
      #print(f'{player_2} won.')
  else:
    winner = 'no_winner'
  return (game_won, winner)#tuple(game_won, winner)


player_1 = input("Entre le nom du premier joueur!\n")
player_2 = input("Entre le nom du deuxiem joueur!\n")
players_list = [player_1, player_2]
markers = ['X' , 'O']
positions = list(range(1,10))
play_array = list(range(1,10))

playboard(play_array)
m = 'non_valid'
while  m not in markers:
  m = input(f'{player_1} choisit son marqueur: X ou O. ')
  
marker_1 = m
markers.remove(m)
marker_2 = markers[0]
marker_list = [marker_1, marker_2]
print(f'{player_1} a {m}\n{player_2} a {markers[0]}.')

game_on = True
while game_on:
  for player, marker in zip(players_list, marker_list):
    posit = user_choice(positions, player)
    play_array[posit-1] = marker
    clear_output()
    playboard(play_array)
    positions.remove(posit)

    game_won = is_game_won(play_array , marker_1, marker_2)
    game_off = len(positions)==0 or game_won[0]
    if game_won[0]:
      if game_won[1] == marker:
        print(f"{player} a gagne.")
      else:
        print(f"{player} a gagne.")
    if game_off:
      break
  if game_off:
    break
print("Game is over!" )

