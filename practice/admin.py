from django.utils import timezone
from datetime import timedelta
from django.contrib import admin
from django.db.models import Sum
from .models import Matter, Client, CourtDate
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
@admin.register(Matter)
class MatterAdmin(admin.ModelAdmin):

    list_display = ('matter_number', 'client', 'status', 'assigned_to', 'fees_agreed', 'amount_paid')

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)

        try:
            queryset = response.context_data['cl'].queryset

            total_fees = queryset.aggregate(Sum('fees_agreed'))['fees_agreed__sum'] or 0
            total_paid = queryset.aggregate(Sum('amount_paid'))['amount_paid__sum'] or 0

            today = timezone.now().date()
            next_week = today + timedelta(days=7)

            upcoming_courts = CourtDate.objects.filter(
                hearing_date__range=[today, next_week]
            ).order_by('hearing_date')

            response.context_data['summary'] = {
                'total_fees': total_fees,
                'total_paid': total_paid,
                'total_outstanding': total_fees - total_paid,
                'total_matters': queryset.count(),
                'upcoming_courts': upcoming_courts,
            }

        except Exception:
            pass

        return response    
@admin.register(CourtDate)
class CourtDateAdmin(admin.ModelAdmin):
    list_display = ('matter', 'court_name', 'hearing_date')
    list_filter = ('hearing_date',)
    search_fields = ('court_name',)
admin.site.site_header = "Lutaaya & Co. Advocates"
admin.site.site_title = "Lutaaya & Co. Admin"
admin.site.index_title = "Practice Management System"