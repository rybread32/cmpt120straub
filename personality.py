#personality.py
#Creates an AI personality
#Created by Ryan Straub
#4/15/19

def intro():
    #Greetings
    print("Different interactions: reward, punish, threaten, joke")
    print("------------------------------------------------------")
    print("Hello there! My name is Alyssa Issah (AI)! How would you like to interact?: ")

def primaryLoop():
    #default and possible emotions 
    currEmotion = ["anger", "disgust", "fear", "happiness", "sadness", "suprise"]
    curr=currEmotion[3]
    currNum=3;
    while True:
        action = getInteraction() #end program
        if action == 4:
            print("Goodbye!")
            break
        else:
            #lookupEmotion(currNum, action)
            currNum =lookupEmotion(currNum, action)
            curr=currEmotion[currNum]
            showEmotion(currNum)
      
def getInteraction():
    action = int(input("Specify An Action(0 - Reward, 1 - Punish, 2 - Threaten, 3 - Joke, 4 - Quit): " ))#HOW TO GET INPUT TO GO TO MATRIX AND NOT PRIMARY LOOP
    return action # return a corresponding integer
    pass # TODO prompt user to choose an action

def lookupEmotion(currNum, action):
    currEmotion = ["anger", "disgust", "fear", "happiness", "sadness", "suprise"]
    #Matrix of how AI will respond
    emotionMatrix = [[3,3,5,5,3,3],
                     [1,2,4,2,4,5],
                     [2,0,2,2,2,2],
                     [0,1,5,3,3,3]]
    emote=emotionMatrix [action][currNum]
    return emote
    pass # TODO do the matrix lookup
    

def showEmotion(currEmotion):
    text = ["Hey! What was that for?! >:-(", "Ugh! Whatever.", "Ahhh!! I'm sorry! :-(", "Thanks! I am happy! :-)", "Oh, i'm sorry :-(", "Woah! What?!"]
    print(text[currEmotion])
    #returns current emotion of AI to primary loop 
    return currEmotion

def main():
    currEmotion = ["anger", "disgust", "fear", "happiness", "sadness", "suprise"]
    intro()
    primaryLoop()

main()
    
