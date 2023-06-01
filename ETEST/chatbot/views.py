from django.shortcuts import render
import openai
from .models import PastQ

def home(request):
    
    if request.method == "POST":
        userChoice = request.POST['model']
        userQuestion = request.POST['question']
        imageSize = request.POST['size']
    
        if userChoice == "davinci":
            openai.api_key = "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"
            openai.Model.list()
            GPT_Response = openai.Completion.create(
                model="text-davinci-003",
                prompt=userQuestion,
                temperature=0.1,
                max_tokens=100,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0)

            GPT_Response = GPT_Response["choices"][0]["text"].strip()
            
        elif userChoice == "dalle":
            openai.api_key = "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"
            openai.Model.list()

            GPT_Response = openai.Image.create(
                prompt=userQuestion,
                n=1,
                size=imageSize
            )
            GPT_Response = GPT_Response['data'][0]['url'].strip()
            
        saveQ = PastQ(question=userQuestion, answer=GPT_Response)
        saveQ.save()
        return render(request, "chatbot/home.html",{
            "userQuestion":userQuestion,
            "GPT_Response":GPT_Response,
            "botModel":userChoice
        })
    return render(request, "chatbot/home.html",{  
    })
    

