from django.db import models

class Customer(models.Model):
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    Aadhaar = models.CharField(max_length=12, unique=True)
    Pincode = models.CharField(max_length=6)
    CustomerId = models.CharField(max_length=10, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            last_customer = Customer.objects.all().order_by('id').last()
            if last_customer:
                self.id = last_customer.id + 1
            else:
                self.id = 5001
        self.CustomerId = f"CID_{self.id}"
        super(Customer, self).save(*args, **kwargs)

class SavingsAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    initial_amount = models.DecimalField(max_digits=10, decimal_places=2)
    account_number = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            last_account = SavingsAccount.objects.all().order_by('id').last()
            if last_account:
                new_id = last_account.id + 1
            else:
                new_id = 1
            self.account_number = f"SAV{new_id:06d}"
        super(SavingsAccount, self).save(*args, **kwargs)

class MFAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    initial_investment = models.DecimalField(max_digits=10, decimal_places=2)
    account_number = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            last_account = MFAccount.objects.all().order_by('id').last()
            if last_account:
                new_id = last_account.id + 1
            else:
                new_id = 1
            self.account_number = f"MF{new_id:06d}"
        super(MFAccount, self).save(*args, **kwargs)

class LoanAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    account_number = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            last_account = LoanAccount.objects.all().order_by('id').last()
            if last_account:
                new_id = last_account.id + 1
            else:
                new_id = 1
            self.account_number = f"LOAN{new_id:06d}"
        super(LoanAccount, self).save(*args, **kwargs)