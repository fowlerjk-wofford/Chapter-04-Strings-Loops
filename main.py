counter = 0
even_count = 0
odd_sum = 0

for count in range(7):
  whatever = int(input())
  #if this is even
  if whatever%2 ==  0:
    #increase my count
    even_count = even_count + 1
    print('number is even')
    print('you are on number ' + str(counter))
    counter = counter + 1
  else:
    odd_sum = odd_sum + whatever
    print('number is odd')
    print('you are on number ' + str(counter))
    counter = counter + 1

print('bla' + str(even_count) + 'bla' + str(odd_sum))