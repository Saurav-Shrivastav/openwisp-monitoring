# Generated by Django 2.0.2 on 2018-03-01 13:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_index=True, max_length=64)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('description', models.TextField(blank=True, help_text='Notes')),
                ('object_id', models.CharField(blank=True, db_index=True, max_length=36)),
                ('check', models.CharField(choices=[('openwisp_monitoring.check.classes.Ping', 'Ping')], db_index=True, help_text='Select check type', max_length=128, verbose_name='check type')),
                ('params', jsonfield.fields.JSONField(blank=True, default=dict, help_text='parameters needed to perform the check', verbose_name='parameters')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
