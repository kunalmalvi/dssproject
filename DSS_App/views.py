from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


@login_required
def home(request):
    title = "Online Fund Transfer"
    return render(request, 'index.html')

def customer_profile(request, pk):
    vs = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer_profile.html', {'object': vs})
