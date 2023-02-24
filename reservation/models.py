from django.db import models


class Accounts(models.Model):
    type = models.CharField(max_length=255, verbose_name="Account type")
    username = models.CharField(max_length=255, verbose_name="Username")
    password = models.CharField(max_length=50, verbose_name="Password")

    def __str__(self):
        return f'{self.username} - {self.type}'
    
    class Meta:
        verbose_name_plural = "Accounts"

class Customers(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    )

    account = models.OneToOneField(Accounts, on_delete=models.CASCADE, verbose_name="Account", related_name="account")
    name = models.CharField(max_length=255, verbose_name="Customer name")
    age = models.PositiveIntegerField(verbose_name="Customer age")
    gender = models.CharField(max_length=10, verbose_name="Customer gender", choices=GENDER, default=OTHER)
    contact_number = models.CharField(max_length=100, verbose_name="Customer phone number")
    address = models.TextField(verbose_name="Customer address")

    def __str__(self):
        return f'{self.account.username} - {self.name}'

    class Meta:
        verbose_name_plural = "Customers"

class Crew(models.Model):
    account = models.OneToOneField(Accounts, on_delete=models.CASCADE, related_name='crew_account', verbose_name="Account")
    name = models.CharField(max_length=150, verbose_name="Crew name")
    job_title = models.CharField(max_length=100, verbose_name='	Job Title')
    assignment = models.CharField(max_length=255, verbose_name='Work Assignment')
    details = models.TextField(verbose_name='Assignment Details')

    def __str__(self):
        return f'{self.account.username} - {self.name}'


class RoomType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Room type name")
    description = models.TextField(verbose_name="Room type description")

    def __str__(self):
        return self.name


class Rooms(models.Model):
    type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='room_type', verbose_name="Room type")
    name = models.CharField(max_length=255, verbose_name="Room name")
    description = models.TextField(verbose_name="Room description")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Room price")
    status = models.CharField(max_length=100, verbose_name="Room status")

    def __str__(self):
        return f'{self.type.name} - {self.name}'

    class Meta:
        verbose_name_plural = "Rooms"


class Reservation(models.Model):
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, related_name="crew_reservation", verbose_name="Crew")
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="customer_reservation", verbose_name="Customer")
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name="room_reservation", verbose_name="Room")
    date = models.DateTimeField(verbose_name="Date of Reservation")
    date_in = models.DateTimeField(verbose_name="Date of Coming In")
    date_out = models.DateTimeField(verbose_name="Date of Coming Out")
    total_payment = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Total Payment")

    def __str__(self):
        return f'{self.customer.name} - {self.room.name} - {self.date}'


class Payment(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="customer_payment", verbose_name="Customer")
    method = models.CharField(max_length=150, verbose_name="Payment method")
    amount = models.PositiveIntegerField(verbose_name="Payment amount")
    date = models.DateTimeField(verbose_name="Date of Payment")

    def __str__(self):
        return f'{self.customer.name} - {self.method} ({self.amount})'


class Transaction(models.Model):
    trans_date = models.DateTimeField(verbose_name="Transaction date")
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="customer_transaction", verbose_name="Customer")
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, related_name="crew_transaction", verbose_name="Crew")
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, related_name="payment_transaction", verbose_name="Payment")
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="reservation_transaction", verbose_name="Reservation")


    def __str__(self):
        return f'{self.customer.name} - {self.crew.name} ({self.trans_date})'


