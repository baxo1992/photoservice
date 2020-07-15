from django.contrib import admin
from .models import Session, Reservation, News, Photos


# Register your models here.


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter = ('price', 'name')
    search_fields = ('title',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'publication_date')
    list_filter = ('title', 'publication_date')
    search_fields = ('title', 'body',)


class PhotosAdmin(admin.TabularInline):
        model = Photos


class ReservationAdmin(admin.ModelAdmin):
    inlines = [PhotosAdmin]
    class Meta:
        model = Reservation


admin.site.register(Reservation, ReservationAdmin)
