# Generated by Django 4.2 on 2023-04-22 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0005_rename_texto_mensaje_mensaje'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='mensaje',
            new_name='texto',
        ),
    ]
