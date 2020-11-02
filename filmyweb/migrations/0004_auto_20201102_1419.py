# Generated by Django 3.1.2 on 2020-11-02 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0003_auto_20201020_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='DodatkoweInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czas_trwania', models.PositiveSmallIntegerField(default=0)),
                ('gatunek', models.PositiveSmallIntegerField(choices=[(2, 'Komedia'), (0, 'Inne'), (3, 'Sci-fi'), (1, 'Horror'), (4, 'Drama')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='dodatkowe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filmyweb.dodatkoweinfo'),
        ),
    ]