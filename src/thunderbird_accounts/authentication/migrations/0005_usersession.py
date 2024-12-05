# Generated by Django 5.1.3 on 2024-12-05 18:49

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_user_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('session_key', models.CharField(help_text='Session Key', max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'indexes': [models.Index(fields=['uuid'], name='authenticat_uuid_f1b526_idx'), models.Index(fields=['created_at'], name='authenticat_created_406c61_idx'), models.Index(fields=['updated_at'], name='authenticat_updated_222183_idx')],
            },
        ),
    ]
