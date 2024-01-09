def LongestWord(sen):
  max_length = 0
  indice = 0
  a = 0
  for i in range(len(sen)):
    if(sen[i].isalpha()):
      a+=1
      if(a > max_length):
        max_length = a
        indice = i
    else:
      a = 0
  print(indice)
  return sen[(indice-a):indice+1:1]


# keep this function call here 
print(LongestWord(input()))