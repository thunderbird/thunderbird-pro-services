# Generated by Django 5.1.3 on 2024-11-14 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_avatar_url_alter_user_display_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='_fxa_token',
            field=models.BinaryField(db_column='fxa_token', null=True),
        ),
    ]
