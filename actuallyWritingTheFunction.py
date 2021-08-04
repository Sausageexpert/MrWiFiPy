def doHokeyPokey(name):
    print("Doing the Python Hokey Pokey (And Trying To Smile), " + name)

def talkToThePython():
    greeting = input("Type your greetings here (preferably hisssssssss) ")
    howWasYourDay = input("Ask the python how his day was (probably scaly) ")
    doYouOrganiseSquirrelFunerals = input("Do you organise squirrel funerals? (No, but I do organise breakfasts...) ")

def countThePythonFangs():
    word = input("Ask For A Bedtime Story From Mr. Py ")
    count = 0
    file = open(word, 'r')
    for line in file:
        words = line.split()
        count = count + len(words)
    print("Number Of Fangs: ")
    print(count)

countThePythonFangs()

# The previous test subjects ran away when they saw the python smiling. I think he needs to brush his
# teeth a bit more

#r for read
