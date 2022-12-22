#importing packages
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import os

stemmer = SnowballStemmer("english")

STOPWORDS = set(stopwords.words("english"))

#get counts (dictionary) open file, for every word in the dictionary, write word and number of occurences
#while writing integers convert them into string first
#python gives errors if you try to print a string and integer together

def write_counts(counts, filepath):
    with open(filepath, "w") as outfile:
        for word in counts.keys():
            to_write = word + " : " + str(counts[word]) + "\n"
            outfile.write(to_write)


def get_counts(infilename):
    # Read the file
    with open(infilename, "r") as infile:
        text = infile.read()

    # get the tokens(words)
    tokens = word_tokenize(text)
    # Extract only the words and convert to lowercase
    #important as some words might me capitallised the first letter
    words = [word.lower() for word in tokens if word.isalpha()]
    #removing stopwords (like articles)
    words = [stemmer.stem(word) for word in words if word not in STOPWORDS]
    # for word in words:
    #     if word not in STOPWORDS:
    #         words = [stemmer.stem(word)]

    counts = {}
    # {"words":occurrences}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    # if word in counts:
    #     counts[word] = counts[word] + 1
    # else:
    #     counts[word] = 1

    #sorting occurences of the words
    sorted_tuples = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    sorted_counts = {k: v for k, v in sorted_tuples}
    return sorted_counts


filenames = os.listdir("./input")
for filename in filenames:
    counts = get_counts("./input/" + filename)
    write_counts(counts, "./output/" + filename)