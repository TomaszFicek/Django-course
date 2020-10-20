# Generated by Django 3.1.2 on 2020-10-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0002_auto_20201020_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='imbd_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='opis',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='film',
            name='plakat',
            field=models.ImageField(blank=True, null=True, upload_to='plakaty'),
        ),
        migrations.AddField(
            model_name='film',
            name='premiera',
            field=models.DateField(blank=True, null=True),
        ),
    ]