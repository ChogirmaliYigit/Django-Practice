# Generated by Django 4.1.7 on 2023-02-23 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accounts',
            options={'verbose_name_plural': 'Accounts'},
        ),
        migrations.AlterModelOptions(
            name='customers',
            options={'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='rooms',
            options={'verbose_name_plural': 'Rooms'},
        ),
        migrations.AlterField(
            model_name='customers',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='other', max_length=10, verbose_name='Customer gender'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='payment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment_transaction', to='reservation.payment', verbose_name='Payment'),
        ),
    ]