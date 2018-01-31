# PLEASE READ - You must use Python3
# Only use what is provided in the standard libraries.

''' This function reads in a file and returns a 
	set of all the tokens. It ignores the subject line

	If the email had the following content:

	Subject: Get rid of your student loans
	Hi there,
	If you work for us, we will give you money
	to repay your student loans. You will be
	debt free!
	FakePerson_22393

	This function would return to you
	set(['', 'work', 'give', 'money', 'rid', 'your', 'there,',
		'for', 'Get', 'to', 'Hi', 'you', 'be', 'we', 'student',
		'debt', 'loans', 'loans.', 'of', 'us,', 'will', 'repay',
		'FakePerson_22393', 'free!', 'You', 'If'])
'''
import os, sys
import math
def token_set(filename):
	#open the file handle
	with open(filename, 'r') as f:
		text = f.read()[9:] # Ignoring 'Subject:'
		text = text.replace('\r', '')
		text = text.replace('\n', ' ')
		tokens = text.split(' ')
		return set(tokens)

def main():
	# TODO: Implement the Naive Bayes Classifier
	pathTest = '/data/test/'
	pathTrainHam = '/data/train/ham/'
	pathTrainSpam = '/data/train/spam/'
	itemsHam = os.listdir('.' + pathTrainHam)
	itemsSpam = os.listdir('.' + pathTrainSpam)
	itemsTest = os.listdir('.' + pathTest)
	hamTable = dict()
	spamTable = dict()
	proHam = math.log10(len(itemsHam) / (len(itemsHam) + len(itemsSpam)))
	proSpam = math.log10(1 - (len(itemsHam) / (len(itemsHam) + len(itemsSpam))))
	for item in itemsHam:
		set = token_set('.' + pathTrainHam + item)
		for word in set:
			if word in hamTable:
				hamTable[word] += 1
			else:
				hamTable[word] = 1
	for item in itemsSpam:
		set = token_set('.' + pathTrainSpam + item)
		for word in set:
			if word in spamTable:
				spamTable[word] += 1
			else:
				spamTable[word] = 1
	for testFile in itemsTest:
		sumSpam = 0
		sumHam = 0
		set = token_set('.' + pathTest + testFile)
		for word in set:
			if word in spamTable:
				magSpam = spamTable[word]
			else:
				magSpam = 0
			if word in hamTable:
				magHam = hamTable[word]
			else:
				magHam = 0
			sumSpam += math.log10(((magSpam + 1) / (len(itemsSpam) + 2)))
			sumHam += math.log10(((magHam + 1) / (len(itemsHam) + 2)))
		if proSpam + sumSpam > proHam + sumHam:
			print(testFile + " Spam")
		else:
			print(testFile + " Ham")
	pass

if __name__ == '__main__':
    main()


