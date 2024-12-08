print('SURVEY')
interested_in_cs = input('Are you interested in computer science? (y/n): ') == 'y'
playing_games = input('Do you like playing computer games? (y/n): ') == 'y'
has_instagram = input('Do you have an Instagram account? (y/n): ') == 'y'

print('SURVEY RESULTS')
print(f'Interested in computer science: {'Yes' if interested_in_cs else 'No'}')
print(f'Playing computer games: {'Yes' if playing_games else 'No'}')
print(f'Has an Instagram account: {'Yes' if has_instagram else 'No'}')
