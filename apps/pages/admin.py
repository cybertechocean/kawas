from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import FAQ, PrivacyPolicy, TermsOfService


@admin.register(FAQ)
class FAQAdmin(ModelAdmin):
    list_display = ['question', 'is_active', 'ordering']
    list_editable = ['is_active', 'ordering']
    search_fields = ['question', 'answer']
    ordering = ['ordering']


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(ModelAdmin):
    def has_add_permission(self, request):
        return not PrivacyPolicy.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TermsOfService)
class TermsOfServiceAdmin(ModelAdmin):
    def has_add_permission(self, request):
        return not TermsOfService.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
