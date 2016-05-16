from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
import django_revision.revision_field
import edc_base.model.fields.hostname_modification_field
import edc_base.model.fields.userfield
import edc_base.model.fields.uuid_auto_field
import uuid
from unipath import Path


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExportHistory',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='One-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_base.model.fields.uuid_auto_field.UUIDAutoField(editable=False, help_text='System field. UUID primary key.', primary_key=True, serialize=False)),
                ('history_uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='system field for export tracking.', unique=True)),
                ('app_label', models.CharField(max_length=50)),
                ('object_name', models.CharField(max_length=50)),
                ('export_uuid_list', models.TextField(help_text="list of export_uuid's of model app_label.object_name", null=True)),
                ('pk_list', models.TextField(help_text="list of pk's of model app_label.object_name", null=True)),
                ('exit_message', models.CharField(help_text='exit message from the export_transactions command', max_length=250)),
                ('exit_status', models.IntegerField(help_text='0=success, 1=failed from the export_transactions command', null=True)),
                ('export_filename', models.CharField(help_text='original filename on export', max_length=250)),
                ('export_file_contents', models.TextField(help_text='save contents of file as a list of rows', null=True)),
                ('exported', models.BooleanField(default=False, help_text='exported to a file')),
                ('exported_datetime', models.DateTimeField(null=True)),
                ('notification_plan_name', models.CharField(max_length=50, null=True)),
                ('sent', models.BooleanField(default=False, help_text='export file sent to recipient')),
                ('sent_datetime', models.DateTimeField(null=True)),
                ('received', models.BooleanField(default=False, help_text='have received an ACK from the recipient')),
                ('received_datetime', models.DateTimeField(null=True)),
                ('closed', models.BooleanField(default=False, help_text='exported, sent, received')),
                ('closed_datetime', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ('-sent_datetime',),
            },
        ),
        migrations.CreateModel(
            name='ExportPlan',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
<<<<<<< HEAD
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
=======
                ('hostname_created', models.CharField(default='One-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
>>>>>>> 6237c4048c8a1e339b18ec46aa614e9f6567de9e
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_base.model.fields.uuid_auto_field.UUIDAutoField(editable=False, help_text='System field. UUID primary key.', primary_key=True, serialize=False)),
                ('app_label', models.CharField(max_length=50)),
                ('object_name', models.CharField(max_length=50)),
                ('fields', models.TextField(max_length=500)),
                ('extra_fields', models.TextField(max_length=500)),
                ('exclude', models.TextField(max_length=500)),
                ('header', models.BooleanField(default=True)),
                ('track_history', models.BooleanField(default=True)),
                ('show_all_fields', models.BooleanField(default=True)),
                ('delimiter', models.CharField(default=',', max_length=1)),
                ('encrypt', models.BooleanField(default=False)),
                ('strip', models.BooleanField(default=True)),
                ('target_path', models.CharField(default='~/export', max_length=250)),
                ('notification_plan_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExportReceipt',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
<<<<<<< HEAD
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
=======
                ('hostname_created', models.CharField(default='One-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
>>>>>>> 6237c4048c8a1e339b18ec46aa614e9f6567de9e
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_base.model.fields.uuid_auto_field.UUIDAutoField(editable=False, help_text='System field. UUID primary key.', primary_key=True, serialize=False)),
                ('export_uuid', models.UUIDField(editable=False, help_text='system field for export tracking.')),
                ('app_label', models.CharField(max_length=64)),
                ('object_name', models.CharField(max_length=64)),
                ('tx_pk', models.CharField(max_length=36)),
                ('timestamp', models.CharField(max_length=50, null=True)),
                ('received_datetime', models.DateTimeField(help_text='date ACK received', null=True)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='ExportTransaction',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
<<<<<<< HEAD
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
=======
                ('hostname_created', models.CharField(default='One-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
>>>>>>> 6237c4048c8a1e339b18ec46aa614e9f6567de9e
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_base.model.fields.uuid_auto_field.UUIDAutoField(editable=False, help_text='System field. UUID primary key.', primary_key=True, serialize=False)),
                ('exported', models.BooleanField(default=False, editable=False, help_text="system field for export tracking. considered 'exported' if both sent and received.")),
                ('exported_datetime', models.DateTimeField(editable=False, help_text='system field for export tracking.', null=True)),
                ('export_change_type', models.CharField(choices=[('I', 'Insert'), ('U', 'Update'), ('D', 'Delete')], default='I', editable=False, help_text='system field for export tracking.', max_length=1)),
                ('export_uuid', django_extensions.db.fields.UUIDField(blank=True, editable=False, help_text='system field for export tracking.')),
                ('tx', models.TextField()),
                ('app_label', models.CharField(max_length=64)),
                ('object_name', models.CharField(max_length=64)),
                ('tx_pk', models.CharField(max_length=36)),
                ('timestamp', models.CharField(db_index=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('exported', 'Exported'), ('closed', 'Closed'), ('cancelled', 'Cancelled')], default='new', help_text='exported by export_transactions, closed by import_receipts', max_length=15)),
                ('received', models.BooleanField(default=False, help_text='True if ACK received')),
                ('received_datetime', models.DateTimeField(help_text='date ACK received', null=True)),
                ('is_ignored', models.BooleanField(default=False, help_text='Ignore if update')),
                ('is_error', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='UploadExportReceiptFile',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='One-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_base.model.fields.uuid_auto_field.UUIDAutoField(editable=False, help_text='System field. UUID primary key.', primary_key=True, serialize=False)),
                ('export_receipt_file', models.FileField(upload_to=Path('/home/django/uploads'))),
                ('file_name', models.CharField(editable=False, max_length=50, null=True, unique=True)),
                ('app_label', models.CharField(max_length=50)),
                ('object_name', models.CharField(max_length=50)),
                ('accepted', models.IntegerField(default=0, editable=False)),
                ('duplicate', models.IntegerField(default=0, editable=False)),
                ('total', models.IntegerField(default=0, editable=False)),
                ('errors', models.TextField(editable=False, null=True)),
                ('receipt_datetime', models.DateTimeField(editable=False, null=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='exportplan',
            unique_together=set([('app_label', 'object_name')]),
        ),
    ]
