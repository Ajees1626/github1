import google.generativeai as genai

def aiCalling(text):
    genai.configure(api_key="AIzaSyBBbcF7Ph1-K6mHZa1VO5lOYAfV9vHc-VA")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(text)
    return response.text

while True :
    print("""
        Please select your options below :
            1) Chat with AI 
            2) Exit
    """)
    choice = int(input("Enter your Choices : "))
    if(choice == 1) :
        #while True:
        userText = input("Enter your Query : ")
        if(userText == "Bye") :
            break
        response = aiCalling(userText)
        print(f"AI : {response}")
    elif (choice == 2) :
        print("Program Successfully Executed")
        break
    else :
        print("Invalid Choices")