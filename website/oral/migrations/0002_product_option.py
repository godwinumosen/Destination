# Generated by Django 4.1.4 on 2023-03-05 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oral', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='option',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], default='draft', max_length=100),
        ),
    ]