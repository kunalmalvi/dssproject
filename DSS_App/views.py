from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


@login_required
def home(request):
    title = "Online Fund Transfer"
    return render(request, 'index.html')

def customer_profile(request):
    customer_obj = Customer.objects.all()
    for i in range(len(customer_obj)):
        if request.user.id == customer_obj[i].user_id:
            key=customer_obj[i].c_id
            vs = get_object_or_404(Customer, pk=key)
            return render(request, 'customer_profile.html', {'object': vs})
    # return render(request, 'profile_not_found.html')
