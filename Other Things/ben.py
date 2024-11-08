from random import randint as ri
from time import sleep as slp
talks = 0
rings = 1
while True:
  #main code stuff
  userIn = input("Talk to Ben or call him by typing /call.\n")
  if userIn.lower() == "/call":
    talks = ri(3,10)
    rings = ri(2,4)
    for i in range(rings):
      print("Brrring, brrring")
      slp(1)
    benCallMsg = "Ben?"
    while talks > 0:
      userIn = input("Ben: " + benCallMsg + "\n")
      if "bye" in userIn.lower():
        talks = 0
      elif "?" in userIn:
        if ri(0,1):
          if ri(0,1):
            benCallMsg = "No"
          elif ri(0,1):
            benCallMsg = "Noo"
          else:
            benCallMsg = "Nooo"
        else:
          benCallMsg = "Yes"
      else:
        if ri(0,1):
          if ri(0,1):
            benCallMsg = "Bleh"
          elif ri(0,1):
            benCallMsg = "Blehh"
          else:
            benCallMsg = "Blehhh"
        else:
          if ri(0,1):
            benCallMsg = "Ho ho ho"
          else:
            benCallMsg = "Ho ho ho!"
      talks -= 1
    print("*click*")
    slp(1)
    print()
  else:
    slp(0.25)
    benCopyList = list(userIn.lower())
    benCopyLoops = len(benCopyList)
    for i in range(benCopyLoops):
      if(ri(1,4) == 1):
        benCopyList[i] = ""
    benCopyStr = "".join(benCopyList)
    print()
    print("Ben: " + benCopyStr)