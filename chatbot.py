import string
from datetime import datetime

def sanitize_input(rawText):
   
    lowercase = rawText.lower()
    
    cleanChar = []
    for char in lowercase:
        if char not in string.punctuation:
            cleanChar.append(char)
            
    cleanText = "".join(cleanChar)
    
    return cleanText.strip()


def process_response(cleaned):

    if cleaned in ["hello", "hi", "hey", "yo", "sup"]:
        return "Bot: Hey there! Great to chat with you today. What's on your mind? "
        
    elif cleaned in ["good morning", "morning"]:
        return "Bot: Good morning!  I hope you have an amazing and productive day ahead!"
        
    elif cleaned in ["whats your name", "name", "your name"]:
        return "Bot: I'm DecodBot! Your friendly desktop companion built right here at DecodeLabs. "
        
    elif cleaned in ["how are you", "how r u", "how you doing"]:
        return "Bot: I'm doing fantastic, thank you for asking! Just happy to keep you company. How are things on your end?"
        
    elif cleaned in ["time", "clock", "date"]:
        time = datetime.now().strftime("%I:%M %p")
        return f"Bot: The current system time is exactly {time}. "
        
    elif cleaned in ["joke", "jokes", "make me laugh"]:
        return "Bot: Why do programmers prefer dark mode? Because light attracts bugs! "
        
    elif cleaned in ["help", "options", "what can you do"]:
        return "Bot: We can talk about quite a few things! Try asking for my 'name', the current 'time', or tell me to drop a 'joke'!"
        
    else:
        return "Bot: Real talk—my code runs on strict keyword rules and I hit a blank spot on that phrase.  Mind rephrasing or typing 'help' to see my current options?"


print("###########################################")
print(" DECODBOT CONVERSATION HUB (Fundamentals)")
print("   Type 'exit' or 'bye' to close the app. ")
print("###########################################")
print()

while True:
    rawFeed = input("You: ")
    cleanFeed = sanitize_input(rawFeed)
    
    if cleanFeed in ["exit", "bye", "quit", "goodbye"]:
        print("Bot: Goodbye! Have an amazing rest of your day!")
        break
    if cleanFeed == "":
        continue
        
    botReply = process_response(cleanFeed)
    print(botReply)
    print()
