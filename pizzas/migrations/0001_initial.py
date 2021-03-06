# Generated by Django 3.0.6 on 2020-05-27 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('EUR', 'EUR'), ('USD', 'USD')], max_length=5, verbose_name='Currency')),
                ('rate', models.DecimalField(decimal_places=4, help_text='to EUR', max_digits=12, verbose_name='Rate')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1024, verbose_name='Address')),
                ('contact_details', models.TextField(blank=True, null=True, verbose_name='Contacts details')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Total price')),
                ('delivery_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Delivery price')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.Currency', verbose_name='Currency')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, help_text='in EUR', max_digits=9, verbose_name='Price')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pizzas/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Pizza',
                'verbose_name_plural': 'Pizzas',
            },
        ),
        migrations.CreateModel(
            name='OrderPizzasCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzas_count', models.PositiveIntegerField(default=1, verbose_name='Pizzas count')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas_set', to='pizzas.Order')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_set', to='pizzas.Pizza')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='pizzas',
            field=models.ManyToManyField(through='pizzas.OrderPizzasCount', to='pizzas.Pizza', verbose_name='Pizzas'),
        ),
    ]
