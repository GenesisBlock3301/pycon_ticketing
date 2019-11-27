from django.http import HttpRequest
from django.shortcuts import render
import re
from .forms import TicketForm
from .data import Ticket

EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\+]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')

def index(request:HttpRequest):
    # print(request.POST.get('name'))
    errors = {}
    is_valid = False
    ticket = None
    form = TicketForm(data=request.POST)
    if request.method == "POST":
        is_valid = form.is_valid()
        if is_valid:
            ticket = Ticket(
                request.POST.get('name'),
                request.POST.get('email'),
                request.POST.get('phone'),
            )
            ticket.save()
    return render(request,'index.html',context={
        'errors':errors,
        'ticket':ticket,
        'form':form,
    })

        # phone = request.POST.get('phone')
        # if  not (len(phone) == 11):
        #     errors['phone'] = "Phone number is wrong"
        # name = request.POST.get('name')
        # if not len(name) > 2:
        #     errors['name'] = "More than 2 digit"
        # email = request.POST.get('email')
        # if not EMAIL_REGEX.fullmatch(email):
        #     errors['email'] = 'Email incorrect'
    # success = request.method == "POST" and not errors

# {
#     'csrfmiddlewaretoken': ['Eiyn2YRzSOBxDlGErKGfVWOQq4po5ziOLvZQB5aSZJVcAtL6qTe8r5OKUzRnFi23'],
#     # 'name': ['Sifat'],
#     'email': ['ntrlove31@gmail.com'],
#     'phone': ['01949168736'],
#     'agreed': ['on']
# }
