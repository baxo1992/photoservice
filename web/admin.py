from django.contrib import admin
from .models import Session, Reservation, News
# Register your models here.


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter = ('price', 'name')
    search_fields = ('title',)




@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_type', 'reservation_date')
    list_filter = ('session_type', 'reservation_date')
    search_fields = ('session_type',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'publication_date')
    list_filter = ('title', 'publication_date')
    search_fields = ('title', 'body',)
