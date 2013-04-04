# The purpose of this program is to take two times and then add them together.
# This is based directly on the example code in chapters 12-14 of 'How to Think Like a Computer Scientist Learning with Python' by Allen Downey, Jeffrey Elkner, and Chris Meyers, (Wellesley, Massachusetts: Green Tea Press, 2002)

# One obvious problem is that this requires tha the times get passed in the very specific '00:00:00' format.

# An important points is that it only adds hours, minutes, and seconds--it doesn't figure out how much further along in time you'll be if you add a certain amount of time to a clock time (or the "time of day"). For times less than 24 total hours, and passed to the program in 24-hour format, adding two times and learning the new clock time when you add two times will be the same. When you're adding enough time that you move to the next day, the calculated values won't tell you the time it will be during that next day--you'll instead have a total of all the hours, minutes, and seconds. The two kinds of time adding are useful in different situations, but this program simply adds pure times, not clock times.

class Time:
  pass

def breakTime(t):
	time = Time()
	time.seconds = int(t[-2:])
	time.minutes = int(t[-5:-3])
	time.hours = int(t[-8:-6])
	return time
	
def convertToSeconds(t):
	minutes = t.hours * 60 + t.minutes
	seconds = minutes * 60 + t.seconds
	return seconds

def makeTime(seconds):
	time = Time()
	time.hours = seconds // 3600
	time.minutes = (seconds%3600) // 60
	time.seconds = seconds%60
	return time

def addTime(t1, t2):
	t1broken=breakTime(t1)
	t2broken=breakTime(t2)
	t1seconds=convertToSeconds(t1broken)
	t2seconds=convertToSeconds(t2broken)
	secondsTotal=t1seconds+t2seconds
	totalTime=makeTime(secondsTotal)

	# The next part deals with the fact that the attributes of a Time class are integers between 0 and 60. The problem is that when the hours, minutes, or seconeds of the totalTime are less than 10, the program returns the integers and drops them into the three parts of a time or clock string. That is, you're expecting something like "10:04:05", but you could get "10:4:5". This checks to see if the time elments are less than 10 and adds a "0" the the beginning of the strong that represents that time attirbute.

	newHours = 0
	newMinutes = 0
	newSeconds = 0

	if totalTime.hours < 10:
		newHours = '0' + str(totalTime.hours)
	else:
			newHours = str(totalTime.hours)

	if totalTime.minutes < 10:
		newMinutes = '0' + str(totalTime.minutes)
	else:
			newMinutes = str(totalTime.minutes)

	if totalTime.seconds < 10:
		newSeconds = '0' + str(totalTime.seconds)
	else:
			newMinutes = str(totalTime.seconds)

	return newHours + ":" + newMinutes + ":" + newSeconds

# Format MUST be '##:##:##', or hours:minutes:seconds
print addTime('21:05:00', '03:27:01')
