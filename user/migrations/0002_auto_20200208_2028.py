# Generated by Django 3.0.3 on 2020-02-08 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Position',
            new_name='position',
        ),
    ]