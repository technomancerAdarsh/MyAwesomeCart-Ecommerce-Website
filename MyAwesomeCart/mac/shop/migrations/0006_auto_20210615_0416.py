# Generated by Django 3.1.6 on 2021-06-14 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orderupdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='subject',
            new_name='phone',
        ),
    ]