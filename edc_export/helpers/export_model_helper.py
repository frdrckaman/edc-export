from django.apps import apps
from django.core import serializers

from django_crypto_fields.field_cryptor import FieldCryptor
from edc_constants.constants import CLOSED

from ..models import ExportTransaction

from .export_helper import ExportHelper


class ExportModelHelper(ExportHelper):

    def __init__(self, app_label=None, model_name=None, **kwargs):
        super().__init__(**kwargs)
        self.app_label = app_label
        self.model_name = model_name

    def reset(self):
        """Resets instance attr.
        """
        self._transactions = []
        self.export_datetime = None
        self.export_filename = None
        self.exit_status = None

    @property
    def transactions(self):
        """Prepares a list of transactions to export.
        """
        if not self._transactions:
            self.app_label = self.export_plan.app_label
            self.model_name = self.export_plan.object_name
            try:
                self.model = apps.get_model(self.app_label, self.model_name)
                if not self.model:
                    raise self.exception_cls()
            except self.exception_cls:
                raise self.exception_cls(
                    'Method get_model returned None for {0}.{1}'.format(self.app_label, self.model_name))
            # get the queued export transactions
            self.export_transactions = ExportTransaction.objects.filter(
                app_label=self.model._meta.app_label,
                object_name=self.model._meta.object_name).exclude(
                    status__in=[CLOSED, 'cancelled'], )  # if already exported but not closed, will send again
            # decrypt export transactions and add to a list
            for export_transaction in self.export_transactions:
                for obj in serializers.deserialize(
                        "json", FieldCryptor('aes', 'local').decrypt(export_transaction.tx)):
                    obj.object.export_transaction = export_transaction
                    self._transactions.append(obj.object)
        return self._transactions
