from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def board(request):
    return render(request, 'pages/board.html')

def customer(request):
    return render(request, 'pages/customer.html')
