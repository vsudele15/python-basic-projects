#getting the raw story from the story.txt file which is in the same directory
with open("story.txt" , "r") as f:
    story = f.read()

#creating a set to store the <words>
words= set()
start_of_word = -1

target_start= "<"
target_end= ">"
#iterating through the story string to find <words>
for i,char in enumerate(story):
    if char== target_start:
        start_of_word= i
    
    if char== target_end and start_of_word!=-1:
        word= story[start_of_word: i+1]
        words.add(word)
        start_of_word=-1

#creating a dictionary to store the user input for that particular word
answers= {}
for word in words:
    answer= input("Enter a word for "+ word + ": ")
    answers[word]= answer

for word in words:
    story = story.replace(word, answers[word])

#printing out the replaced words story to the console
print(story)