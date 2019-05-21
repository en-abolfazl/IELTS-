# This program calculates your IELTS Listening and Reading (General & Academic) band score
# A description of raw scores and band scores for IELTS Listening
bandscore0forlistening = [0, 1, 2, 3]
bandscore2_5forlistening = [4, 5]
bandscore3forlistening = [6, 7]
bandscore3_5forlistening = [8, 9, 10]
bandscore4forlistening = [10, 11, 12]
bandscore4_5forlistening = [13, 14, 15]
bandscore5forlistening = [16, 17]
bandscore5_5forlistening = [18, 19, 20, 21, 22]
bandscore6forlistening = [23, 24, 25]
bandscore6_5forlistening = [26,27, 28, 29]
bandscore7forlistening = [30, 31]
bandscore7_5forlistening = [32, 33, 34]
bandscore8forlistening = [35, 36]
bandscore8_5forlistening = [37, 38]
bandscore9forlistening = [39, 40]

# A description of raw scores and band scores for IELTS Reading 
bandscore0foracademicreading = [0, 1, 2, 3]
bandscore2_5foracademicreading = [4, 5]
bandscore3foracademicreading = [6, 7]
bandscore3_5foracademicreading = [8, 9]
bandscore4foracademicreading = [10, 11, 12]
bandscore4_5foracademicreading = [13, 14]
bandscore5foracademicreading = [15, 16, 17, 18]
bandscore5_5foracademicreading = [19, 20, 21, 22]
bandscore6foracademicreading = [23, 24, 25, 26]
bandscore6_5foracademicreading = [27, 28, 29]
bandscore7foracademicreading = [30, 31, 32]
bandscore7_5foracademicreading = [33, 34]
bandscore8foracademicreading = [35, 36]
bandscore8_5foracademicreading = [37, 38]
bandscore9foracademicreading = [39, 40]


# A description of raw scores and band scores for IELTS General Reading 
bandscore0forgeneralreading = [0, 1, 2, 3, 4, 5]
bandscore2_5forgeneralreading = [6, 7, 8]
bandscore3forgeneralreading = [9, 10, 11]
bandscore3_5forgeneralreading = [12, 13, 14]
bandscore4forgeneralreading = [15, 16, 17, 18]
bandscore4_5forgeneralreading = [19, 20, 21, 22]
bandscore5forgeneralreading = [23, 24, 25, 26]
bandscore5_5forgeneralreading = [27, 28, 29]
bandscore6forgeneralreading = [30, 31]
bandscore6_5forgeneralreading = [32, 33]
bandscore7forgeneralreading = [34, 35]
bandscore7_5forgeneralreading = [36]
bandscore8forgeneralreading = [37, 38]
bandscore8_5forgeneralreading = [39]
bandscore9forgeneralreading = [40]


print ("Welcome to the Python IELTS Listening and Reading (Academic/General) band score calculator.") 
print ("This program calculates your IELTS Listening and Reading (Academic & General) band score.")
print ("For Listening enter 1, for Academic Reading enter 2 and for General Reading enter 3")

choice = input ("Please choose 1, 2 or 3")
choice = int (choice)



#raw score for IELTS Listening
if choice == 1:
    print ("You can calculate your IELTS Listening band score here:")
    
raw_score = input ("Please enter your IELTS listening raw score")
raw_score = int (raw_score)

if raw_score in bandscore0forlistening:
    print ("Your Listening band score is 0")
elif raw_score in bandscore2_5forlistening:
    print ("Your Listening band score is 2.5")
elif raw_score in bandscore3forlistening:
    print ("Your Listening band score is 3")
elif raw_score in bandscore3_5forlistening:
    print ("Your Listening band score is 3.5")
elif raw_score in bandscore4forlistening:
    print ("Your Listening band score is 4")
elif raw_score in bandscore4_5forlistening:
    print ("Your Listening band score is 4.5")
elif raw_score in bandscore5forlistening:
    print ("Your Listening band score is 5")
elif raw_score in bandscore5_5forlistening:
    print ("Your Listening band score is 5.5")
elif raw_score in bandscore6forlistening:
    print ("Your Listening band score is 6")
elif raw_score in bandscore6_5forlistening:
    print ("Your Listening band score is 6.5")
elif raw_score in bandscore7forlistening:
    print ("Your Listening band score is 7")
elif raw_score in bandscore7_5forlistening:
    print ("Your Listening band score is 7.5")
elif raw_score in bandscore8forlistening:
    print ("Your Listening band score is 8")
elif raw_score in bandscore8_5forlistening:
    print ("Your Listening band score is 8.5")
elif raw_score in bandscore9forlistening:
    print ("Your Listening band score is 9")

    


#raw score for IELTS Academic Reading
if choice == 2:
    print ("You can also calculate your IELTS Academic Reading band score here:")
    
raw_score = input ("Please enter your IELTS Academic Reading raw score")
raw_score = int (raw_score)

if raw_score in bandscore0foracademicreading:
    print ("Your Academic Reading band score is 0")
elif raw_score in bandscore2_5foracademicreading:
    print ("Your Academic Reading band score is 2.5")
elif raw_score in bandscore3foracademicreading:
    print ("Your Academic Reading band score is 3")
elif raw_score in bandscore3_5foracademicreading:
    print ("Your Academic Reading band score is 3.5")
elif raw_score in bandscore4foracademicreading:
    print ("Your Academic Reading band score is 4")
elif raw_score in bandscore4_5foracademicreading:
    print ("Your Academic Reading band score is 4.5")
elif raw_score in bandscore5foracademicreading:
    print ("Your Academic Reading band score is 5")
elif raw_score in bandscore5_5foracademicreading:
    print ("Your Academic Reading band score is 5.5")
elif raw_score in bandscore6foracademicreading:
    print ("Your Academic Reading band score is 6")
elif raw_score in bandscore6_5foracademicreading:
    print ("Your Academic Reading band score is 6.5")
elif raw_score in bandscore7foracademicreading:
    print ("Your Academic Reading band score is 7")
elif raw_score in bandscore7_5foracademicreading:
    print ("Your Academic Reading band score is 7.5")
elif raw_score in bandscore8foracademicreading:
    print ("Your Academic Reading band score is 8")
elif raw_score in bandscore8_5foracademicreading:
    print ("Your Academic Reading band score is 8.5")
elif raw_score in bandscore9foracademicreading:
    print 



#raw score for IELTS General Reading
if choice == 3: 
    print ("You can also calculate your IELTS General Reading band score here:")
    
raw_score = input ("Please enter your IELTS General Reading raw score")
raw_score = int (raw_score)

if raw_score in bandscore0forgeneralreading:
    print ("Your General Reading band score is 0")
elif raw_score in bandscore2_5forgeneralreading:
    print ("Your General Reading band score is 2.5")
elif raw_score in bandscore3forgeneralreading:
    print ("Your General Reading band score is 3")
elif raw_score in bandscore3_5forgeneralreading:
    print ("Your General Reading band score is 3.5")
elif raw_score in bandscore4forgeneralreading:
    print ("Your General Reading band score is 4")
elif raw_score in bandscore4_5forgeneralreading:
    print ("Your General Reading band score is 4.5")
elif raw_score in bandscore5forgeneralreading:
    print ("Your General Reading band score is 5")
elif raw_score in bandscore5_5forgeneralreading:
    print ("Your General Reading band score is 5.5")
elif raw_score in bandscore6forgeneralreading:
    print ("Your General Reading band score is 6")
elif raw_score in bandscore6_5forgeneralreading:
    print ("Your General Reading band score is 6.5")
elif raw_score in bandscore7forgeneralreading:
    print ("Your General Reading band score is 7")
elif raw_score in bandscore7_5forgeneralreading:
    print ("Your General Reading band score is 7.5")
elif raw_score in bandscore8forgeneralreading:
    print ("Your General Reading band score is 8")
elif raw_score in bandscore8_5forgeneralreading:
    print ("Your General Reading band score is 8.5")
elif raw_score in bandscore9forgeneralreading:
    print ("Your General Reading band score is 9")


print ("Wish you luck :) and happy IELTSing")







asjhfvlsjdahvljhvsdljhvsadjlhblsdjhvksjdvksdjhvcskdjvcskdjcvsjcvsjcvsdljhcvsldjhcvasldjhcvasdjlhcvsdljhcvsdljhcvsdjlcvsdljhc

