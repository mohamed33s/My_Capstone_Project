from ast import Or
from django.contrib import admin
from .models import ClientProfile, Orders , Review


class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('user_model', 'birth', 'phone')
    list_filter = ('user_model',)
    search_fields = ('user_model',)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('sender_order', 'recipient_order', 'order_title', 'order_type', 'date_time', 'order_status')
    list_filter = ('order_title',)
    date_hierarchy = 'date_time'
    search_fields = ('order_title',)




class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('service_provider', 'username', 'review_date')
    list_filter = ('username',)
    date_hierarchy = 'review_date'
    search_fields = ('username',)



admin.site.register(ClientProfile, ClientProfileAdmin)
admin.site.register(Orders,OrdersAdmin)
admin.site.register(Review, ReviewsAdmin)
