# Generated by Django 2.1 on 2018-09-18 17:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180918_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
