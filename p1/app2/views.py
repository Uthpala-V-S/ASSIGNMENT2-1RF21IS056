
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CustomerRegistrationForm, SavingsAccountForm, MFAccountForm, LoanAccountForm
from .models import Customer, SavingsAccount, MFAccount, LoanAccount

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('products_page', customer_id=customer.CustomerId)
    else:
        form = CustomerRegistrationForm()
    return render(request, 'register.html', {'form': form})

def products_page(request, customer_id):
    return render(request, 'products.html', {'customer_id': customer_id})

def open_savings_account(request, customer_id):
    customer = get_object_or_404(Customer, CustomerId=customer_id)
    if request.method == 'POST':
        form = SavingsAccountForm(request.POST)
        if form.is_valid():
            savings_account = form.save(commit=False)
            savings_account.customer = customer
            savings_account.save()
            return HttpResponse(f"Savings Account created successfully! Account Number: {savings_account.account_number}")
    else:
        form = SavingsAccountForm()
    return render(request, 'open_savings_account.html', {'form': form, 'customer_id': customer_id})

def open_mf_account(request, customer_id):
    customer = get_object_or_404(Customer, CustomerId=customer_id)
    if request.method == 'POST':
        form = MFAccountForm(request.POST)
        if form.is_valid():
            mf_account = form.save(commit=False)
            mf_account.customer = customer
            mf_account.save()
            return HttpResponse(f"MF Account created successfully! Account Number: {mf_account.account_number}")
    else:
        form = MFAccountForm()
    return render(request, 'open_mf_account.html', {'form': form, 'customer_id': customer_id})

def open_loan_account(request, customer_id):
    customer = get_object_or_404(Customer, CustomerId=customer_id)
    if request.method == 'POST':
        form = LoanAccountForm(request.POST)
        if form.is_valid():
            loan_account = form.save(commit=False)
            loan_account.customer = customer
            loan_account.save()
            return HttpResponse(f"Loan Account created successfully! Account Number: {loan_account.account_number}")
    else:
        form = LoanAccountForm()
    return render(request, 'open_loan_account.html', {'form': form, 'customer_id': customer_id})