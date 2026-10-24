from django.shortcuts import render

# Create your views here.


# function based view
# class based view

def homeView(request):
    username = "Temi"
    return render(
        request, 
        template_name="index.html",
        context={
            "username": username
        }
    )


def aboutView(request):
    
    return render(request, template_name="about.html")