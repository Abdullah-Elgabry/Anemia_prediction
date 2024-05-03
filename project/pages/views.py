from django.shortcuts import render
from django.core.mail import send_mail




def index(request):

    return render(request,"pages/index.html")
  

def Help(request):

    return render(request,"pages/help.html")





def contact(request):
    if request.method == "POST":
        nameGET = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(

            subject,
            message,
            email,
            ['bedo.4114@gmail.com'],



        )


        return render(request,"pages/contact.html",{'username':nameGET})
    else :
        return render(request,"pages/contact.html")




def about (request):

    return render(request,"pages/about.html")
 