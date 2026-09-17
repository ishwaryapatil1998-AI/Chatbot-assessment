import pandas as pd
import numpy as np

#Step 1:Creating a dataset
data = {
    "Article": [
        "cricket team won match",
        "football player scored goal",
        "cricket player hit century",

        "new smartphone launched",
        "artificial intelligence improves software",
        "new laptop has powerful processor",

        "government announced new policy",
        "election campaign started",
        "minister announced new scheme"
    ],

    "Category": [
        "Sports",
        "Sports",
        "Sports",

        "Technology",
        "Technology",
        "Technology",

        "Politics",
        "Politics",
        "Politics"
    ]
}
print('Article sepereated into categories')
print('='*40)
df = pd.DataFrame(data)

print(df,'\n')

#Step 2:Finding the number of unique elements
tokens = df['Article'].str.split().explode().unique()
print('The available unique words in dataset are')
print('='*40)
print(tokens,'\n')
print('Count of unique words :' ,len(tokens),'\n')

#Step 3:Category wise count and calculating their probablity
sports_count = np.sum(df['Category'] == 'Sports')
technology_count = np.sum(df['Category'] == 'Technology')
politics_count = np.sum(df['Category'] == 'Politics')
total_count = len(df)
prob_sports = sports_count/total_count
prob_tech = technology_count/total_count
prob_pol = politics_count/total_count

print('Probablity of all the categories in the dataset')
print('='*50)
print('Probablity of sports category is :',prob_sports)
print('Probablity of technology category is :',prob_tech)
print('Probablity of politics category is :',prob_pol,'\n')

#Step 4:Creating a word probablity function
def word_probablity(word,category_name):
    articles = df[df['Category'] == category_name]['Article']
    count = 0
    for article in articles:
        words = article.lower().split()
        if word in words:
            count+=1
        category_count = len(articles)
        probablity = (count+1)/(category_count+len(tokens))
    return probablity
print('Calculated probablity using functions')
print('='*40)
print('The probablity of cricket in sports is :',word_probablity('cricket','Sports'))
print('The probablity of cricket in technology is :',word_probablity('cricket','Technology'),'\n')

#Step 5:Combining function probablities
while True:
    word = input('Enter a word : ')
    if word == 'B':
        print('\nPrediction completed exiting the program...','\n')
        break
    sports_prob = prob_sports*word_probablity(word,'Sports')
    tech_prob = prob_tech*word_probablity(word,'Technology')
    pol_prob = prob_pol*word_probablity(word,'Politics')

    print('\nCombined probablities')
    print('='*20)
    print('Probablity of given word in sports is :',sports_prob)
    print('Probablity of given word in  technology is :',tech_prob)
    print('Probablity of given word in politics is :',pol_prob,'\n')

#Step 6:Final Prediction

    if sports_prob > tech_prob and pol_prob:
        prediction = 'Sports'
    elif tech_prob > sports_prob and pol_prob:
        prediction = 'Technology'
    else:
        prediction = 'Politics'
    print('The prediction of given word is :',prediction,'\n')
