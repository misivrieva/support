#!/mims/bin/env python3
#coding: latin-1

import os
import datetime
import pprint

inputFilePath = "/home/mims/Desktop/python/review.log.YYYY.MM.DD_NN.txt"

open_file = open (inputFilePath, "r")
print (open_file.read()) 

head, tail = os.path.split(inputFilePath)
print (head)
print (tail)

old_file_name = tail
print old_file_name, len(old_file_name)

YYYY = old_file_name[11:15]
print YYYY

MM = old_file_name[16:18]
print MM

DD = old_file_name[19:21]
print DD

NN = old_file_name[22:24]
print NN

create_new_file = open ("FS2PRODB_REVIEWS_" + YYYY+ MM + DD + '.txt', "w+")

print ("FS2PRODB_REVIEWS_" + YYYY+ MM + DD + '.txt')

print ("New file created")

outputFilePath = "/home/mims/Desktop/python/FS2PRODB_REVIEWS_YYYYMMDD.txt"

"""^ realised it can't work because the information in the name is NOT from the same time zone -> the date can be different on the two reports"""


with open (inputFilePath) as f:
    with open (outputFilePath, 'a') as f1:
        for line in f:
            f1.write(line)
f1.close()
f.close()   

print ('File copied')  

#give me the 1st line

pp = pprint.PrettyPrinter(indent=1)

with open (inputFilePath, 'r') as f:
    for i, x in enumerate(f):
        if (i == 0):
            categories = x.split('■')
            
            categoriesString = '■'.join(categories)
            pp.pprint(categoriesString)
        if (i > 0):
            alertReviewList = []
            print('Line: ' + str(i))

            alertReviewList = x.split('■')

            print(alertReviewList)
            
            for index, ed in enumerate(alertReviewList):
                alertReviewList[index] = ed.strip()

            pp.pprint(alertReviewList)

            review_date = alertReviewList[0]
            reviewer = alertReviewList[1]

            event_type = alertReviewList[3]
            if 'registration' in event_type:
                alertReviewList(0, True)
                alertReviewList(1, False)
                alertReviewList(2, False)
                alertReviewList(3, False)
                alertReviewList (4, False)

            elif 'login' in event_type:
                alertReviewList (0, False)
                alertReviewList (1, True)
                alertReviewList (2, False)
                alertReviewList (3, False)
                alertReviewList (4, False)
                
            elif 'transfer' in event_type: 
                alertReviewList (0, False)
                alertReviewList (1, False)
                alertReviewList (2, True)
                alertReviewList (3, False)
                alertReviewList (4, False)

            elif 'deposit' in event_type: 
                alertReviewList (0, False)
                alertReviewList (1, False)
                alertReviewList (2, False)
                alertReviewList (3, True)
                alertReviewList (4, False)   

            elif 'detailsUpdate' in event_type:
                alertReviewList (0, False)
                alertReviewList (1, False)
                alertReviewList (2, False)
                alertReviewList (3, False)
                alertReviewList (4, True)   
            else:
                print ('Error in Event Type')


                
            

            reviewerArray = reviewer.split(',')
            reviewerArrayFormatted = reversed(reviewerArray)
            reviewerString = ",".join(reviewerArrayFormatted)

            alertReviewList.insert(0, review_date)
            alertReviewList.insert(1, reviewerString)

            eventDetailsString = '■'.join(alertReviewList)






