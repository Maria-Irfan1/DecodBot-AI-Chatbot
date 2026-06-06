import string
from datetime import datetime

def sanitize_input(raw_text):
   
    lowercase_text = raw_text.lower()
    
    clean_chars = []
    for char in lowercase_text:
        if char not in string.punctuation:
            clean_chars.append(char)
            
    clean_text = "".join(clean_chars)
    
    return clean_text.strip()


def process_response(cleaned_text):

    if cleaned_text in ["hello", "hi", "hey", "yo", "sup"]:
        return "Bot: Hey there! Great to chat with you today. What's on your mind? "
        
    elif cleaned_text in ["good morning", "morning"]:
        return "Bot: Good morning!  I hope you have an amazing and productive day ahead!"
        
    elif cleaned_text in ["whats your name", "name", "your name"]:
        return "Bot: I'm DecodBot! Your friendly desktop companion built right here at DecodeLabs. "
        
    elif cleaned_text in ["how are you", "how r u", "how you doing"]:
        return "Bot: I'm doing fantastic, thank you for asking! Just happy to keep you company. How are things on your end?"
        
    elif cleaned_text in ["time", "clock", "date"]:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"Bot: The current system time is exactly {current_time}. "
        
    elif cleaned_text in ["joke", "jokes", "make me laugh"]:
        return "Bot: Why do programmers prefer dark mode? Because light attracts bugs! "
        
    elif cleaned_text in ["help", "options", "what can you do"]:
        return "Bot: We can talk about quite a few things! Try asking for my 'name', the current 'time', or tell me to drop a 'joke'!"
        
    else:
        return "Bot: Real talk—my code runs on strict keyword rules and I hit a blank spot on that phrase.  Mind rephrasing or typing 'help' to see my current options?"


print("###########################################")
print(" DECODBOT CONVERSATION HUB (Fundamentals)")
print("   Type 'exit' or 'bye' to close the app. ")
print("###########################################")
print()

while True:
    user_raw_feed = input("You: ")
    user_clean_feed = sanitize_input(user_raw_feed)
    
    if user_clean_feed in ["exit", "bye", "quit", "goodbye"]:
        print("Bot: Goodbye! Have an amazing rest of your day!")
        break
    if user_clean_feed == "":
        continue
        
    bot_reply = process_response(user_clean_feed)
    print(bot_reply)
    print()