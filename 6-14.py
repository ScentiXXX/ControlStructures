facebook = input('Facebook (Y/N): ') == 'Y'
twitter = input('Twitter (Y/N): ') == 'Y'
instagram = input('Instagram (Y/N): ') == 'Y'

if facebook + twitter + instagram >= 2:
  print('You are a good influencer!')
