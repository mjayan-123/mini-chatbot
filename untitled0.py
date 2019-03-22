import random
alfiya_template = "Alfiya : {0}"
midhila_template = "Midhila : {0}"
name = "Alfiya Jaleel"
weather = "cloudy"
time="morning"
#def respond(message):
  
  # Concatenate the user's message to the end of a standard bot respone
   
# Alfiya_message = "Midhila You said: " + message
   
 # Return the result
    
 #return Alfiya_message


# Test function

#print(respond("Good morning Alfiya"))



# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(midhila_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(alfiya_template.format(response))

# Send a message to the bot
#send_message("hi")

responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "hi":["hlw"],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "tell me something about your project":["hi we are doing a chatbot that will communicate in sign language","we are 3 in our team"],
  "i need an icecream":["which flavour do you prefer"],
  "what's the time now?" :[ "now its evening","i think its going to be afternoon","its morning"],
  "default": ["I can't answer this question"]
}

# Use random.choice() to choose a matching response
def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["default"])
    return bot_message
