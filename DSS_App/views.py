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
    return render(request, 'profile_not_found.html')

def fund_transfer(request):
    customer_obj = Customer.objects.all()
    for i in range(len(customer_obj)):
        if request.user.id == customer_obj[i].user_id:
            key=customer_obj[i].c_id
            sender_balance=customer_obj[key-1].balance
            print('------------------1----------------')
            if request.method == 'POST':
                customer_acc = request.POST['customer_acc']
                transfer_amount = float(request.POST['transfer_amount'])
                print('------------------2----------------')
                for i in range(len(customer_obj)):
                    if customer_obj[i].acc_number==int(customer_acc):
                        print('------------------3----------------')
                        cust2_key=customer_obj[i].c_id
                        print(customer_obj[cust2_key-1].balance)
                        receiver_balance=customer_obj[cust2_key-1].balance
                        sender_balance-=transfer_amount
                        receiver_balance+=transfer_amount
                        customer_obj[cust2_key-1].balance=receiver_balance
                        customer_obj[key-1].balance=sender_balance
                        customer_obj[cust2_key-1].save()
                        customer_obj[key-1].save()
                        return render(request, 'fund_transfer.html', {"msg":"Successfully Transfered","customer_acc":customer_acc,"transfer_amount":transfer_amount})
            else:
                return render(request,'fund_transfer.html')
