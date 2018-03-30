# SW2018

This project is part of the course the Social Web 2018. This GitHub page provides all necesarry files that were used to analyze the gender gap on International Womensday 2018.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for further development and testing purposes.

### Prerequisites

- Python 2.7
- Python packages: twitter, tweepy, json, NLTK

### File descriptions

Python file | Content
------------ | -------------
streaming.py | This file streams the data from twitter and saves it in a CSV file (JSON format)
entityanalysis.py | This file performs an entity analysis for hashtags, using Counter element
textyanalysis.py | This file performs a text analysis, it counts the most common words in the text element (tweet)
placesyanalysis.py | This file performs the place analysis, it shows in which country the most tweets were posted

### Twitter Analysis
In the streaming file you can change the #YOURPREFERENCE to any hashtag that you would like to analyse. For this project #IWD2018 was used.

```python
twitterStream = Stream(auth, listener())
x = twitterStream.filter(track=["#YOURPREFERENCE"])
```
### Project findings
The IWD2018.pdf file sumarizes all the findings for #IWD2018 using the provided files.
