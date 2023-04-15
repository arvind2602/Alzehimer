from django.shortcuts import render
# import openai,os
# from dotenv import load_dotenv


# api_key=os.getenv('OPENAI_KEY',None)
def home(request):
    return render(request,'index.html')
def detect(request):
    return render(request,'detect/dragdrop.html')


# openai.api_key = "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"

# def chatbot_response(user_input):
#     response = openai.Completion.create(
#       engine="text-davinci-002",
#       prompt=user_input,
#       temperature=0.5,
#       max_tokens=1024,
#       top_p=1,
#       frequency_penalty=0,
#       presence_penalty=0
# )



# def chatbot(request):
#     chatbot_response=None
    
#     if api_key is not None and request.method =='POST':
#         openai.api_key='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'  
#         user_input=request.POST.get["user_input"]
#         response=chatbot_response(user_input)
        
#         response=openai.Completion.create(
#             engine="text-davinci-002",
#             prompt=user_input,
#             max_tokens=256,
#             temperature=0.5,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0,
#         )
#         print(response)
#         response=response['choices'][0]["text"]
#     return render(request,'chat.html',{'response':response,})