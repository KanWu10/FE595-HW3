import os
import re
import nltk
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# Define paths
malepath = os.path.join("Users","dongyuewu","Desktop","Male")
femalepath = os.path.join("Users","dongyuewu","Desktop","Female")
# Extract all the text names in a list
Malenameslist = os.listdir(malepath)
Femalenameslist = os.listdir(femalepath)
# Remove an unrelated file name produced by MacOS.
Malenameslist.remove(".DS_Store")
Femalenameslist.remove(".DS_Store")
# Combine all the text files in one txt file.
with open("Maleresult.txt", "w") as outfile:
    for f in Malenameslist:
        with open(malepath+'/'+f) as infile:
            outfile.write(infile.read())
with open("Femaleresult.txt", "w") as outfile:
    for f in Femalenameslist:
        with open(femalepath+'/'+f) as infile:
            outfile.write(infile.read())
# Clean and organize text into a list.
def genderlist(gender):
    if gender == "Male":
        maletxt = open(str(gender + "result.txt")).read()
        puremaletxt = re.sub(r'\d+','',maletxt)
        puremaletxt = re.sub(r"[^\w\d'\s]+",'',puremaletxt)
        malelist1 = puremaletxt.split("He")
        malelist1.remove('')
        finalmalelist = []
        for sentence in malelist1:
            he = str("He" + sentence.replace("\n", ""))
            finalmalelist.append(he)
        print(finalmalelist)
    elif gender == "Female":
        femaletxt = open(str(gender + "result.txt")).read()
        purefemaletxt = re.sub(r'\d+','',femaletxt)
        purefemaletxt = re.sub(r"[^\w\d'\s]+",'',purefemaletxt)
        femalelist1 = purefemaletxt.split("She")
        femalelist1.remove('')
        finalfemalelist = []
        for sentence in femalelist1:
            she = str("She" + sentence.replace("\n", ""))
            finalfemalelist.append(she)
        print(finalfemalelist)

# Sentiment analysis

sia = SentimentIntensityAnalyzer()
def get_sentiment(text):
    return sia.polarity_scores(text)
# Create a dictionary containing the characters and corresponding scores.

Malescore = {}
Femalescore = {}
def Score(gender):
    if gender == "Male":
        for male in finalmalelist:
            Malescore[male] = get_sentiment(male)['compound']
        Malescoreordered = sorted(Malescore.items(),key=lambda x: x[1])
        Toptenmale = Malescoreordered[-11:-1]
        Bottomtenmale = Malescoreordered[0:10]
        Toptenmalelist = []
        Bottomtenmalelist = []
        for l in Toptenmale:
            Toptenmalelist.append(l[0])
        for b in Bottomtenmale:
            Bottomtenmalelist.append(b[0])
        with open('Top10Male.txt', mode='wt', encoding='utf-8') as file1:
            file1.write('\n'.join(Toptenmalelist))
        with open('Bottom10Male.txt', mode='wt', encoding='utf-8') as file2:
            file2.write('\n'.join(Bottomtenmalelist))
    elif gender == "Female":
        for female in finalfemalelist:
            Femalescore[female] = get_sentiment(female)['compound']
        Femalescoreordered = sorted(Femalescore.items(),key=lambda x: x[1])
        Toptenfemale = Femalescoreordered[-11:-1]
        Bottomtenfemale = Femalescoreordered[0:10]
        Toptenfemalelist = []
        Bottomtenfemalelist = []
        for l in Toptenfemale:
            Toptenfemalelist.append(l[0])
        for b in Bottomtenfemale:
            Bottomtenfemalelist.append(b[0])
        with open('Top10Female.txt', mode='wt', encoding='utf-8') as file3:
            file3.write('\n'.join(Toptenfemalelist))
        with open('Bottom10Female.txt', mode='wt', encoding='utf-8') as file4:
            file4.write('\n'.join(Bottomtenfemalelist))

def CommonDescriptor(gender):
    dellist = ['A','SHE','HE','S','THE','AN','WITH','HIS','ON','FOR','OF','FROM','WHO','IN','TO','BY','AND','HER']
    if gender == "Male":
        maletxt = open(str(gender + "result.txt")).read()
        puremaletxt = re.sub(r'\d+','',maletxt)
        puremaletxt = re.sub(r"[^\w\d'\s]+",'',puremaletxt)
        Malewords = re.findall(r'\w+',puremaletxt)
        Malecap_words = [word.upper() for word in Malewords]
        Maleword_count = Counter(Malecap_words)
        for n in dellist:
            del Maleword_count[n]
        Maleword_count = sorted(Maleword_count.items(),key=lambda x: x[1])
        Mtencommon = []
        for i in range(-11,-1):
            Mtencommon.append(str(Maleword_count[i][0])+':'+ str(Maleword_count[i][1]))
        with open('10commonMale.txt', mode='wt', encoding='utf-8') as file5:
            file5.write('\n'.join(Mtencommon))
    elif gender == "Female":
        femaletxt = open(str(gender + "result.txt")).read()
        purefemaletxt = re.sub(r'\d+','',femaletxt)
        purefemaletxt = re.sub(r"[^\w\d'\s]+",'',purefemaletxt)
        Femalewords = re.findall(r'\w+',purefemaletxt)
        Femalecap_words = [word.upper() for word in Femalewords]
        Femaleword_count = Counter(Femalecap_words)
        for n in dellist:
            del Femaleword_count[n]
        Femaleword_count = sorted(Femaleword_count.items(),key=lambda x: x[1])
        Ftencommon = []
        for i in range(-11,-1):
            Ftencommon.append(str(Femaleword_count[i][0])+':'+str(Femaleword_count[i][1]))
        with open('/Users/dongyuewu/Desktop/10commonFemale.txt', mode='wt', encoding='utf-8') as file6:
            file6.write('\n'.join(Ftencommon))










 
