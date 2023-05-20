from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.owned_flats.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'town_district', 'address',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year',
                    'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by', 'owners')
    inlines = [OwnerInline, ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('complained_about_flat', 'who_complained',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owned_flats',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
