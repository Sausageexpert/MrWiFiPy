whatIWasGoingToSay = input("No Quotations \"Whatever I Want\" Pls ")

characterCount = 0
wordCount = 1

for i in whatIWasGoingToSay:
    characterCount = characterCount + 1
    if(i == ' '):
        wordCount = wordCount + 1

print("Number Of Words You Were Going To Say 100% Accuracy")
print(wordCount)
print("Number of Characters You Were Probably Not Going To Say The E is Silent in Sure")
print(characterCount)