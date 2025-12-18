from google import genai

client = genai.Client(api_key = "AIzaSyBMuyM144kGFP4yJ9flotNtfEZYWN7NhAg")

messages = []
while True:
    user_input = input("You: ")
    messages.append("user: "+ user_input)
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = messages,                               
    )
    messages.append("AI: "+ response.text)
    print("AI: "+ response.text)






# messages = []
# while True:
#     user_input = input("You: ")
#     messages.append("user: "+ user_input)
#     response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents = messages,                               
#     )
#     print("AI: "+ response.text)









# while True:
#     user_input = input("You: ")
#     response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents = user_input
#     )
#     print("AI: "+ response.text)












# user_input = input("Enter your prompt:- ")
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents = user_input
# )

# print(response.text)