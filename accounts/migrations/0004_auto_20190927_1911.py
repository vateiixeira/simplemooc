# Generated by Django 2.2.5 on 2019-09-27 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190927_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passwordreset',
            old_name='user',
            new_name='username',
        ),
    ]