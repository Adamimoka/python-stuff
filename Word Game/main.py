import pygame
import math
import random
with open("word_list_file.txt") as f: # Fix file opening
  word_list = f.readlines
pygame.init()
prompt_list_0 = ['t','a','o','i','n','s','h','r','d','l']
prompt_list_1 = ['th', 'he', 'in', 'er', 'an', 're', 'nd', 'on', 'en', 'at']
prompt_list_2 = ['k', 'j', 'x', 'q', 'z', 'it', 'is', 'hi', 'es', 'ng']
prompt_list_3 = ['ing', 'ent', 'ion', 'ter', 'ich', 'tion', 'ould', 'ight', 'ough', 'ment']
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Word Bomb")

bombIMG = pygame.image.load("Bomb.png") # Fix file opening
boomIMG = pygame.image.load("Boom.png") # Fix file opening
bombRect = pygame.Rect(175,235,220,220)

promptFont = pygame.font.SysFont("FreeMono, Monospace", 100)

clock = pygame.time.Clock()
typed=''
usedWords = []
failedText=False
failedTextTimer=0
failedText2=False
failedTextTimer2=0
correctGuesses=0
lastPrompt="1"
prompt=random.choice(prompt_list_0)
bombTimer = 7.50
maxBombTimer = 7.5

def ChoosePrompt(gs):
  global prompt
  global lastPrompt
  lastPrompt = prompt
  while prompt == lastPrompt:
    if gs > 50:
      prompt=random.choice(prompt_list_3)
    elif gs > 30:
      if random.randint(0,1):
        prompt=random.choice(prompt_list_2)
      else:
        prompt=random.choice(prompt_list_3)
    elif gs > 20:
      if random.randint(0,1):
        prompt=random.choice(prompt_list_1)
      else:
        prompt=random.choice(prompt_list_2)
    elif gs > 10:
      if random.randint(0,1):
        prompt=random.choice(prompt_list_0)
      else:
        prompt=random.choice(prompt_list_1)
    else:
      prompt=random.choice(prompt_list_0)
    
    
    

def CompleteWord():
  if ((typed + "\n").upper() in word_list) and (prompt in typed) and typed not in usedWords:
    global correctGuesses, bombTimer, maxBombTimer
    correctGuesses+=1
    bombTimer = maxBombTimer
    maxBombTimer = max(maxBombTimer - 0.07,1.5)
    ChoosePrompt(correctGuesses)
    usedWords.append(typed)
  else:
    if typed in usedWords:
      global failedText2
      failedText2=True
    else:
      global failedText
      failedText=True
    
    
while not False:
  clock.tick(60)
  for event in pygame.event.get():
    if bombTimer >= 0:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
          typed = typed[:-1]  
        elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
          CompleteWord()
          typed = ''
        elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT or event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL or event.key == pygame.K_LALT or event.key == pygame.K_RALT:
          pass
        else:
          if event.unicode.isalpha():
            if len(typed) <= 50:
              typed += (event.unicode).lower()
            else:
              failedText=True
          else:
            failedText=True
  if failedText:
    failedText=False
    failedTextTimer=1
  failedTextTimer -= 0.02
  if failedText2:
    failedText2=False
    failedTextTimer2=1
  failedTextTimer2 -= 0.02
  bombTimer -= 0.0166666667
  #DRAW
  screen.fill((24,12,26))
  scoreFont = pygame.font.SysFont("FreeMono, Monospace", 70)
  scoreText = scoreFont.render(str(correctGuesses), "True", (255,255,255))
  screen.blit(scoreText, (20,20))
  if bombTimer >= 0:
    screen.blit(bombIMG,pygame.Rect(175,235,220,220))
    typerFont = pygame.font.SysFont("FreeMono, Monospace", round((len(typed)**2)*.015-(1.5*len(typed))+53))
    typerText = typerFont.render(typed, "True", (255,255,255))
  
    promptText = promptFont.render(prompt, "True", (255,255-(max(failedTextTimer,0))*255,255-max((max(failedTextTimer,0))*255,(max(failedTextTimer2,0))*255)))
  
    bombTimerText = promptFont.render(str(math.floor(bombTimer * 10)/10), "True", (0,0,0))
    
    screen.blit(typerText, (int(264+(-(round((len(typed)**2)*.015-(1.5*len(typed))+53)) * len(typed)/4)),20))
    screen.blit(promptText, (int(264+(-(len(prompt)*25))),100))
    screen.blit(bombTimerText, (189, 300))
  if bombTimer<0:
    screen.blit(boomIMG,pygame.Rect(85,125,400,400))
    if bombTimer<-2:
      quit()
  pygame.display.flip()