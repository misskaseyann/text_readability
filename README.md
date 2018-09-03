Text Difficulty Assessment
====
Using the Flesch-Kincaid reading ease formula:

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/bd4916e193d2f96fa3b74ee258aaa6fe242e110e "formula")

I created a program to determine the readability of literature over time.
### Readability Over Time
Comparing the oldest novel that I ran through the algorithm (Leviathan with a score of 63.8) with the newest novel (Gone Girl with a score of 82.7), there was an 18.9 point increase between 1651 and 2012. Some of the reasons why this could be are first: how our culture has changed, second: economics and cost of printing, and third: accessability.

<img src="http://i64.tinypic.com/288m7o7.png" alt="readability over time" width="500"/>

### Readability in Modern Sources
Twitter has the easiest readability by far. Taking the average value of all tweets read by the algorith, it had a score of 98.4. An example tweet is as follows:
>“yall tired of boiling water every time you make pasta? boil a few gallons at the beginning of the week and freeze it for later.” 
>@datassque 7:47 PM - 29 Jul 2017

Tweets typically make up a total of two sentences on average with a character limit of 140. The formula being used depends strongly on the number of words divided by the total sentences which means tweets will on average have a larger value.

<div>
<img src="http://i63.tinypic.com/wb81oi.png" alt="various lit sources" width="400"/> <img src="http://i67.tinypic.com/ankbd0.jpg"score alt="various blog sources" width="400"/></div>

With tweets being the highest readability, suprisingly enough, blogs had the lowest readability with an average score of 65. Going further indepth, I evaluated multiple blog genres and found they ranked as such (starting at least readable):

1. Tech
2. Science
3. Gaming
4. Longform
5. Lifestyle
6. Entertainment

### Improving the Accessibility of Text Automatically
This algorithm can quickly read through thousands of pages of text which makes it efficient for determining how difficult a piece of reading material could be for the average consumer. Using that information can quickly turn a complicated text book into a much more readable piece of material depending on what user it is aimed for.

### Interesting Finds
The most interesting find that I discovered while working on this project was the fact that the length of a novel does not determine its complexity. For example, War and Peace has over 562,000 words in it with the reading level of a 7th grader. The literature piece, A Modest Proposal has less than 4,000 words in it and it has the reading level of a College student. However, the difficulty is measured based on words, sentences, and syllables. Assumptions that older classical books are more difficult to read could still be valid since the language used in the 1800s is different from modern 21st century language thus making it harder for the typical modern day reader to understand the conveyed meaning.
