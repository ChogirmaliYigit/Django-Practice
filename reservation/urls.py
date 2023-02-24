from django.urls import path
from .views import index, add_account, accounts, update_account, delete_account, add_customer, customers, update_customer\
, delete_customer, add_crew, crews, update_crew, delete_crew, add_roomtype, roomtypes, update_roomtype, delete_roomtype\
, add_room, rooms, update_room, delete_room, add_reservation, reservations, update_reservation, delete_reservation\
, payments, add_payment, update_payment, delete_payment, transactions, add_transaction, update_transaction, delete_transaction

urlpatterns = [
    path('', index, name='index'),
    path('add_account/', add_account, name='add_account'),
    path('accounts/', accounts, name='accounts'),
    path('update_account/<int:account_id>/', update_account, name='update_account'),
    path('delete_account/<int:account_id>/', delete_account, name='delete_account'),
    path('add_customer/', add_customer, name='add_customer'),
    path('customers/', customers, name='customers'),
    path('update_customer/<int:customer_id>/', update_customer, name='update_customer'),
    path('delete_customer/<int:customer_id>/', delete_customer, name='delete_customer'),
    path('add_crew/', add_crew, name='add_crew'),
    path('crews/', crews, name='crews'),
    path('edit_crew/<int:crew_id>/', update_crew, name='update_crew'),
    path('delete_crew/<int:crew_id>/', delete_crew, name='delete_crew'),
    path('add_roomtype/', add_roomtype, name='add_roomtype'),
    path('roomtypes/', roomtypes, name='roomtypes'),
    path('edit_roomtype/<int:roomtype_id>/', update_roomtype, name='update_roomtype'),
    path('delete_roomtype/<int:roomtype_id>/', delete_roomtype, name='delete_roomtype'),
    path('add_room/', add_room, name='add_room'),
    path('rooms/', rooms, name='rooms'),
    path('edit_room/<int:room_id>/', update_room, name='update_room'),
    path('delete_room/<int:room_id>/', delete_room, name='delete_room'),
    path('add_reservation/', add_reservation, name='add_reservation'),
    path('reservations/', reservations, name='reservations'),
    path('edit_reservation/<int:reservation_id>/', update_reservation, name='update_reservation'),
    path('delete_reservation/<int:reservation_id>/', delete_reservation, name='delete_reservation'),
    path('add_payment/', add_payment, name='add_payment'),
    path('payments/', payments, name='payments'),
    path('edit_payment/<int:payment_id>/', update_payment, name='update_payment'),
    path('delete_payment/<int:payment_id>/', delete_payment, name='delete_payment'),
    path('add_transaction/', add_transaction, name='add_transaction'),
    path('transactions/', transactions, name='transactions'),
    path('edit_transaction/<int:transaction_id>/', update_transaction, name='update_transaction'),
    path('delete_transaction/<int:transaction_id>/', delete_transaction, name='delete_transaction')
]

