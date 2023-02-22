# Generated by Django 4.1.7 on 2023-02-20 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KATEGORI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.CharField(max_length=140)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Kategori',
            },
        ),
        migrations.CreateModel(
            name='IHA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=140)),
                ('model', models.CharField(max_length=140)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ağırlık')),
                ('flight_time', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Uçuş Süresi')),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.kategori')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'İHA',
            },
        ),
    ]