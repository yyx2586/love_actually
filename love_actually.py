import getpass

roles = set(["diors", "bitch", "truelove", "goddess", "matchmaker"])
while True:
  print("New game!")
  print("Valid roles:")
  print(roles)
  selected = []
  for i in range(1, 7):
    print("Player " + str(i))
    while True:
      role = getpass.getpass("Enter your role: ")
      if role in roles:
        selected.append(role)
        break
      else:
        print "invalid role"
  #print selected
  while True:
    print("Enter two player ids to see if they are matched")
    while True:
      first = int(raw_input("First player id: "))
      if first in range(1, 7):
        break
    while True:
      second = int(raw_input("Second player id: "))
      if second in range(1, 7):
        break
    first = selected[first-1]
    second = selected[second-1] 
    if (first == "goddess" and second == "truelove") or (first == "truelove" and second == "goddess"):
      print "Congratulations! True love wins! Bitches go die!"
      break
    elif (first == "diors" and second == "bitch") or (first == "bitch" and second == "diors"):
      print "Diors has found a bitch! They will now leave the game and live happily after!"
    elif (first == "bitch" and second == "truelove") or (first == "truelove" and second == "bitch"):
      print "I'm sorry! Bitches have sabotaged true love! Bitches win!"
      break
    else:
      print "Unsuccessful link"
  
  print
  print 
