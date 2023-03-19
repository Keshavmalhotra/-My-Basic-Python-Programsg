import time
t= time.strftime("%H: %M", time.localtime())
t2= int(t[:2])
if t2>= 4 and t2< 12:
  print("good morning! the time is,", t, "AM", "have a nice day.")
elif t2>= 12 and t2< 16:
  print("good afternoon! the time is,", t, "PM", "enjoy.")
elif t2>= 16 or t2== 16 and t2< 00:
  print("good evening! the time is,", t, "PM", "enjoy")
elif t2>= 00 and t2< 4:
  print("good night, sweet dreams! the time is,", t, "AM", "enjoy.")