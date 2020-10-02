import datetime
date = datetime.datetime.now()
#nicer output than in exercise
print("\ntoday is " + date.strftime("%x") + " and it's "+date.strftime("%X")+ " o'clock")
