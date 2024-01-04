def uncompress(s):
  """
  we have a left and a right
  for thie problem right will represent the letter and left will be times that char
  for
  """
  
  left,right = 0,0
  numbers ='1234567890'
  answer =''
  while right < len(s):
    # incremenet right until it is a character
    if s[right] in numbers:
      right +=1 
    else:
      #here we will add the between s[left:right] that will be the the number of tumnes
      times = int(s[left:right]) # array slice
      answer += f'{s[right]*times}'
      right +=1
      left = right
  return answer