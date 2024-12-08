time = input('Enter time (24-hour format): ')

[hours, minutes] = time.split(':')

hours_12_format = int(hours)
period = 'am'

if hours_12_format > 12:
  hours_12_format -= 12
  period = 'pm'

print(f'Time in 12-hour format: {hours_12_format}:{minutes}{period}')
