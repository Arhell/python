import random

x = random.randint(1, 100)
user_num = 0
cnt = 0

while True:
  user_num = int(input('Some text some text'))
  cnt += 1 # cnt = cnt + 1
  if user_num == x:
    print(f'Some text {cnt}')
    if input('Some text' == 'y'):
      x = random.randint(1, 100)
      cnt = 0
    else:
      print('some text')
      break

    print('some text')
    break

  elif user_num > x:
    print('Some text')

  else:
    print('Some text')




