# import csv in order to be able to read/import csv files into directory
import csv

#Load data using the reader function in python, therefrom create a list including all the information present in the userreviews csv file
file = csv.reader(open("/Users/dionboonstra/Downloads/userReviews all three parts.csv", encoding= 'utf8'), delimiter = ';')
reviews = list(file)
#print(reviews)

#Create a new list which includes all reviews on the movie American-Sniper
reviewers = []
for x in reviews:
    if x[0] == 'american-sniper':
        #all reviewers with reviews on the american-sniper movie are added to the list
        reviewers.append(x)
#print(reviewers)

#Create a new list in which all reviews are included from the reviewers present in the reviewers list.
#In addition, the list is constructed so it only contains reviews from reviewers whom scored american-sniper with a 7 or higher,
#where the other reviews are higher than the one provided for american-sniper, and the reviews can be on the movie american sniper itself
recommendations = list()
for y in reviewers:
   for z in reviews:
        if y[2] == z[2] and int(y[1]) > 7 and int(z[1]) >= int(y[1]) and z[0] != 'american-sniper':
            #absolute and relative increase of the reviewscore in comparison to the american-sniper movie are created
            absinc = int(z[1]) - int(y[1])
            relinc = (int(z[1]) - int(y[1])) / int(y[1])
            #the absolute and relative increases of reviewscore are added to the existing list of rows of the original csv file
            totalrec = (z[0], z[1], z[2], z[3], z[4], z[5], z[6], z[7], z[8], z[9], absinc, relinc)
            #all rows are added to the recommendations list
            recommendations.append(totalrec)
#print(recommendations)

#The recommendations list is sorted descending on the absolute increase of the review score (tup[11])
sortedrec = sorted(recommendations, key=lambda tup: (tup[11]), reverse=True)
#print(sortedrec)

#Headers are added in order to create a clear overview for the new recommendations file
header = ["movieName", "Metascore_w", "Author", "AuthorHref", "Date", "Summary", "InteractionsYesCount", "InteractionsTotalCount", "InteractionsThumbUp", "InteractionsThumbDown", "AbsoluteIncrease", "RelativeIncrease"]

#Create a new csv including the header and sortedrec list, completing the movie recommendations list with american-sniper as favorite movie
with open("MovieRecommendations.csv", "w", newline= '') as ResitRecSys:
    writer = csv.writer(ResitRecSys, delimiter=';')
    writer.writerow(header)

    for row in sortedrec:
        writer.writerow(row)
