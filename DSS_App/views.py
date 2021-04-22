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
    transactions_obj = Transactions.objects.all()
    for i in range(len(customer_obj)):
        if request.user.id == customer_obj[i].user_id:
            key=customer_obj[i].c_id
            logined_user_acc = customer_obj[i].acc_number
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
                        receiver_balance=customer_obj[cust2_key-1].balance
                        sender_balance-=transfer_amount
                        receiver_balance+=transfer_amount
                        customer_obj[cust2_key-1].balance=receiver_balance
                        customer_obj[key-1].balance=sender_balance
                        customer_obj[cust2_key-1].save()
                        customer_obj[key-1].save()
                        Transactions.objects.create(sender_acc=logined_user_acc, receiver_acc=customer_acc, transactions_amount=transfer_amount)

                        return render(request, 'fund_transfer.html', {"msg":"Successfully Transfered","customer_acc":customer_acc,"transfer_amount":transfer_amount})
            else:
                return render(request,'fund_transfer.html')

def view_transactions(request):
    customer_obj = Customer.objects.all()
    transactions_obj = Transactions.objects.all()
    transactions_list=[]
    for i in range(len(customer_obj)):
        if request.user.id == customer_obj[i].user_id:
            for j in range(len(transactions_obj)):
                if customer_obj[i].acc_number == transactions_obj[j].sender_acc or transactions_obj[j].receiver_acc:
                    debit_credit = "Debit" if customer_obj[i].acc_number == transactions_obj[j].sender_acc else "Credit"
                    transactions_list.append({1:transactions_obj[j].sender_acc,2:transactions_obj[j].receiver_acc,3:transactions_obj[j].transactions_amount,4:transactions_obj[j].transaction_time,5:debit_credit})
    print(transactions_list)
    return render(request, 'view_fund_transfer.html', {"status":debit_credit,"transactions_list":transactions_list})
