from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerForm, AccountForm, CrewForm, ReservationForm, TransactionForm, PaymentForm, RoomTypeForm, RoomForm
from .models import Customers, Accounts, Crew, Reservation, Transaction, Payment, Rooms, RoomType

def index(request):
    return render(request=request, template_name='reservation/index.html')

def add_account(request):
    form = AccountForm()
    if request.method == 'POST':
        Accounts.objects.create(type=request.POST.get('type'), username=request.POST.get('username'),
        password=str(len(request.POST.get('password')) * '*'))
        return redirect('accounts')
    return render(request=request, template_name='reservation/add_account.html', context={"form": form})

def accounts(request):
    accounts = Accounts.objects.all()
    return render(request=request, template_name='reservation/accounts.html', context={"accounts": accounts})

def update_account(request, account_id):
    account = get_object_or_404(Accounts, id=account_id)
    form = AccountForm(instance=account)
    if request.method == "POST":
        form = AccountForm(data={
            'type': request.POST.get('type'),
            'username': request.POST.get('username'),
            'password': str(len(request.POST.get('password')) * '*')
        },
        instance=account)
        if form.is_valid():
            form.save()
            return redirect('accounts')
        else:
            print(form.errors)
    return render(request=request, template_name='reservation/edit_account.html', context={"form": form})

def delete_account(request, account_id):
    account = get_object_or_404(Accounts, id=account_id)
    account.delete()
    return redirect('accounts')


def add_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        Customers.objects.update_or_create(account_id=int(request.POST.get('account')), name=request.POST.get('name'), age=request.POST.get('age'),
        gender=request.POST.get('gender'), contact_number=request.POST.get('contact_number'), address=request.POST.get('address'))
        return redirect('customers')
    return render(request=request, template_name='reservation/add_customer.html', context={'form': form})

def customers(request):
    customers = Customers.objects.all()
    return render(request=request, template_name='reservation/customers.html', context={"customers": customers})

def update_customer(request, customer_id):
    customer = get_object_or_404(Customers, id=customer_id)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(data=request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
        else:
            print(form.errors)
    return render(request=request, template_name='reservation/edit_customer.html', context={"form": form})

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customers, id=customer_id)
    customer.delete()
    return redirect('customers')

def add_crew(request):
    form = CrewForm()
    if request.method == 'POST':
        Crew.objects.create(account_id=request.POST.get('account'), name=request.POST.get('name'), job_title=request.POST.get('job_title'),
        assignment=request.POST.get('assignment'), details=request.POST.get('details'))
        return redirect('crews')
    return render(request=request, template_name='reservation/add_crew.html', context={"form": form})

def crews(request):
    crews = Crew.objects.all()
    return render(request=request, template_name='reservation/crews.html', context={"crews": crews})

def update_crew(request, crew_id):
    crew = get_object_or_404(Crew, id=crew_id)
    form = CrewForm(instance=crew)
    if request.method == 'POST':
        form = CrewForm(data=request.POST, instance=crew)
        if form.is_valid():
            form.save()
            return redirect('crews')
        else:
            print(form.errors)
    return render(request=request, template_name='reservation/edit_crew.html', context={'form': form})

def delete_crew(request, crew_id):
    crew = get_object_or_404(Crew, id=crew_id)
    crew.delete()
    return redirect('crews')

def add_roomtype(request):
    form = RoomTypeForm()
    if request.method == 'POST':
        RoomType.objects.create(name=request.POST.get('name'), description=request.POST.get('description'))
        return redirect('roomtypes')
    return render(request=request, template_name='reservation/add_roomtype.html', context={'form': form})

def roomtypes(request):
    roomtypes = RoomType.objects.all()
    return render(request=request, template_name='reservation/roomtypes.html', context={'roomtypes': roomtypes})

def update_roomtype(request, roomtype_id):
    roomtype = get_object_or_404(RoomType, id=roomtype_id)
    form = RoomTypeForm(instance=roomtype)
    if request.method == 'POST':
        form = RoomTypeForm(data=request.POST, instance=roomtype)
        if form.is_valid():
            form.save()
            return redirect('roomtypes')
        else:
            print(form.errors)
    return render(request=request, template_name='reservation/edit_roomtype.html', context={'form':form})

def delete_roomtype(request, roomtype_id):
    roomtype = get_object_or_404(RoomType, id=roomtype_id)
    roomtype.delete()
    return redirect('roomtypes')

def add_room(request):
    form = RoomForm()
    if request.method == 'POST':
        Rooms.objects.create(type_id=request.POST.get('type'), name=request.POST.get('name'), description=request.POST.get('description'),
        price=request.POST.get('price'), status=request.POST.get('status'))
        return redirect('rooms')
    return render(request=request, template_name='reservation/add_room.html', context={'form': form})

def rooms(request):
    rooms = Rooms.objects.all()
    return render(request=request, template_name='reservation/rooms.html', context={'rooms': rooms})

def update_room(request, room_id):
    room = get_object_or_404(Rooms, id=room_id)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(data=request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('rooms')
        else:
            print(form.errors)
    return render(request=request, template_name='reservation/edit_room.html', context={'form': form})

def delete_room(request, room_id):
    room = get_object_or_404(Rooms, id=room_id)
    room.delete()
    return redirect('rooms')

def reservations(request):
    reservations = Reservation.objects.all()
    return render(request=request, template_name='reservation/reservations.html', context={'reservations': reservations})

def add_reservation(request):
    form = ReservationForm()
    if request.method == 'POST':
        Reservation.objects.create(crew_id=request.POST.get('crew'), customer_id=request.POST.get('customer'), room_id=request.POST.get('room'),
        total_payment=request.POST.get('total_payment'), date=request.POST.get('date'), date_in=request.POST.get('date_in'), date_out=request.POST.get('date_out'))
        return redirect('reservations')
    return render(request=request, template_name='reservation/add_reservation.html', context={'form': form})

def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    form = ReservationForm(instance=reservation)
    if request.method == 'POST':
        form = ReservationForm(data=request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations')
        else:
            print(form.errors)
    return render(request=request, template_name='reservation/edit_reservation.html', context={'form': form})

def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()
    return redirect('reservations')

def payments(request):
    payments = Payment.objects.all()
    return render(request=request, template_name='reservation/payments.html', context={'payments': payments})

def add_payment(request):
    form = PaymentForm()
    if request.method == 'POST':
        Payment.objects.create(customer_id=request.POST.get('customer'), method=request.POST.get('method'),
        amount=request.POST.get('amount'), date=request.POST.get('date'))
        return redirect('payments')
    return render(request=request, template_name='reservation/add_payment.html', context={'form': form})

def update_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    form = PaymentForm(instance=payment)
    if request.method == 'POST':
        form = PaymentForm(data=request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payments')
        else:
            print(form.errors)
    return render(request=request, template_name='reservation/edit_payment.html', context={'form': form})

def delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    payment.delete()
    return redirect('payments')

def transactions(request):
    transactions = Transaction.objects.all()
    return render(request=request, template_name='reservation/transactions.html', context={'transactions': transactions})

def add_transaction(request):
    form = TransactionForm()
    if request.method == 'POST':
        Transaction.objects.create(customer_id=request.POST.get('customer'), crew_id=request.POST.get('crew'), payment_id=request.POST.get('payment'),
        reservation_id=request.POST.get('reservation'), trans_date=request.POST.get('trans_date'))
        return redirect('transactions')
    return render(request=request, template_name='reservation/add_transaction.html', context={'form': form})

def update_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    form = TransactionForm(instance=transaction)
    if request.method == 'POST':
        form = TransactionForm(data=request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transactions')
        else:
            print(form.errors)
    return render(request=request, template_name='reservation/edit_transaction.html', context={'form': form})

def delete_transaction(request, transaction_id):
    transactiondel = get_object_or_404(Transaction, id=transaction_id)
    transactiondel.delete()
    return redirect('transactions')

