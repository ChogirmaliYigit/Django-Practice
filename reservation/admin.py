from django.contrib import admin
from .models import Customers, Accounts, Crew, Transaction, Reservation, Rooms, RoomType, Payment


admin.site.register(Customers)
admin.site.register(Accounts)
admin.site.register(Crew)
admin.site.register(Transaction)
admin.site.register(Reservation)
admin.site.register(Rooms)
admin.site.register(RoomType)
admin.site.register(Payment)