import random
import sys

def unique(list1):
 
    unique_list = []
 
    for i in list1:
        if i not in unique_list:
            unique_list.append(i)
            
    return(unique_list)

file_path1 = "recent_hashtags.txt"

file_path2 = "all_hashtags.txt"

acceptable = False
while not acceptable:
    num_hashtags = input("How many hashtags would you like to select? ")
    try:
        num_hashtags = int(num_hashtags)
        acceptable = True
    except ValueError as e:
        print(f"Your input needs to be an integer...")

#create list of recently used hastags
recent_hashtags = []
with open(file_path1, 'r') as f:
	for i in f:
		recent_hashtags.append(i.replace('\n', ''))
		
	recent_hashtag = []
	for i in recent_hashtags:
		i = i.split(' ')
		recent_hashtag.append(i)

#create list of all potential hashtags to select		
all_hashtags = []
with open(file_path2, 'r') as f:
	for i in f:
		all_hashtags.append(i.replace('\n', ''))
		
	all_hashtag = []
	for i in all_hashtags:
		i = i.split(' ')
		all_hashtag.append(i)

#filter recently used hashtags from list of potential hashtags
candidates = []
if all_hashtag[0] == 0:
	print('The file all_hastags.txt is empty. Please add hashtags to this file.')
else:		
	for i in all_hashtag[0]:
		if len(recent_hashtag) != 0:
			if i in recent_hashtag[0]:
				continue
			else:
				candidates.append(i)
		else:
			candidates.append(i)
		
		
selected = []
#get unique candidate hashtags to avoid sampling bias from repeats
candidates = unique(candidates)

#until the request number of hashtags are selected, select a random hashtag from the list of potential hashtags
if num_hashtags <= len(candidates):
	while len(selected) != num_hashtags:
		x = candidates[random.randrange(len(candidates))]
		if x in selected:
			continue
		else:
			selected.append(x)
	for i in selected:
		print(i, end = ' ')
else:
	print('Not enough hashtags to choose from!')
	print('Add more hashtags to the all_hashtags.txt file to print ' + str(num_hashtags) + ' hashtags...')

#update record of recently used hashtags
file1_empty = open(file_path1, 'r+')
file1_empty.truncate(0)
for i in selected:
	file1_amend = open(file_path1, "a")
	file1_amend.write(i+' ')






