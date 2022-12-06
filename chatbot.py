import re
import longresponses as long

def messageProbability(userMessage, recognizedWords, singleResponse = False, requiredWords = []):
    messageCertainty = 0
    hasRequiredWords = True

    for word in userMessage:
        if word in recognizedWords:
            messageCertainty += 1

    percentage = float(messageCertainty) / float(len(recognizedWords))

    for word in requiredWords:
        if word not in userMessage:
            hasRequiredWords = False
            break
    if hasRequiredWords or singleResponse:
        return int(percentage * 100)
    else:
        return 0

def checkAllMessages(message):
    highestProbabilityList = {}   

    def response(botResponse,listOfWords,singleResponse = False, requiredWords = []):
        nonlocal highestProbabilityList
        highestProbabilityList[botResponse] = messageProbability(message, listOfWords, singleResponse, requiredWords)
    
    #Responses --------------------------------------------------------------------------------------------
    response('Hello!',['hello', 'hi', 'hallo', 'hey', 'szia', 'hiiii', "what's up"], singleResponse = True)
    response('Goodbye!',['bye', 'goodbye', 'ciao',], singleResponse = True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], requiredWords =['how'])
    response('Thank you!', ['you', 'are', 'amazing', 'nice',], requiredWords =['you', 'amazing', 'nice'])
    response(long.rEating, ['what', 'you', 'eat',], requiredWords =['you', 'eat'])
    response(long.rRobot, ['are', 'you', 'a', 'bot', 'robot'], requiredWords =['robot', 'you', 'bot'])
    response(long.rSomething, ['tell', 'me', 'something',], requiredWords =['tell', 'me', 'something'])
    response(long.rJoke, ['funny', 'joke', 'are', 'tell'], requiredWords =['funny', 'joke','are','tell'])

    bestMatch = max(highestProbabilityList, key = highestProbabilityList.get)
    # print(highestProbabilityList)

    return long.unknown() if  highestProbabilityList[bestMatch] < 1 else bestMatch

def getResponse(userInput):
    splitMessage = re.split(r"\s+|[,;?!.-]\s*", userInput.lower())
    response = checkAllMessages(splitMessage)
    return response


#Testing the response system
while True:
    print('Bot: ' + getResponse(input('You: '))) 
