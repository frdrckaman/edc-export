from django.contrib import admin

from .actions import export_file_contents, export_as_csv_action, export_tx_to_csv_action
from .admin_site import edc_export_admin
from .models import ExportHistory, ExportPlan, ExportReceipt, ExportTransaction, UploadExportReceiptFile


@admin.register(ExportHistory, site=edc_export_admin)
class ExportHistoryAdmin (admin.ModelAdmin):

    date_hierarchy = 'sent_datetime'
    list_display = (
        'model_name', 'app_label', 'exit_status', 'closed',
        'closed_datetime', 'exported', 'exported_datetime',
        'sent', 'sent_datetime', 'received', 'received_datetime')
    list_filter = (
        'exit_status', 'app_label', 'model_name', 'closed',
        'sent', 'received', 'exported', 'closed_datetime',
        'exported_datetime', 'sent_datetime', 'received_datetime', 'user_created')
    search_fields = ('export_uuid_list', 'pk_list')
    actions = [export_file_contents, ]


@admin.register(ExportPlan, site=edc_export_admin)
class ExportPlanAdmin (admin.ModelAdmin):

    list_display = ('app_label', 'model_name',)
    list_filter = ('app_label', 'model_name', )


@admin.register(ExportReceipt, site=edc_export_admin)
class ExportReceiptAdmin (admin.ModelAdmin):

    date_hierarchy = 'received_datetime'
    list_display = ('export_uuid', 'app_label', 'model_name', 'timestamp', 'received_datetime')
    list_filter = ('app_label', 'model_name', 'received_datetime', 'created', 'modified')
    search_fields = ('export_uuid', 'tx_pk', 'id')


@admin.register(ExportTransaction, site=edc_export_admin)
class ExportTransactionAdmin (admin.ModelAdmin):

    date_hierarchy = 'created'
    list_display = (
        'export_uuid', 'timestamp', 'render', 'status',
        'app_label', 'model_name', 'export_change_type',
        'exported', 'received', 'received_datetime', 'created',)
    list_filter = (
        'status', 'exported', 'received', 'app_label',
        'model_name', 'export_change_type', 'received_datetime',
        'created')
    search_fields = ('export_uuid', 'tx_pk', 'tx')

    def get_actions(self, request):
        actions = super(ExportTransactionAdmin, self).get_actions(request)
        actions['export_as_csv_action'] = (
            export_as_csv_action(),
            'export_as_csv_action',
            "Export to CSV")
        actions['export_tx_to_csv_action'] = (
            export_tx_to_csv_action(),
            'export_tx_to_csv_action',
            "Export transaction in selected objects to CSV")
        return actions


@admin.register(UploadExportReceiptFile, site=edc_export_admin)
class UploadExportReceiptFileAdmin(admin.ModelAdmin):

    date_hierarchy = 'created'

    list_display = (
        'file_name', 'accepted', 'duplicate',
        'total', 'errors', 'created', 'user_created',
        'hostname_created')

    list_filter = ('created', 'hostname_created')