# Generated by Django 4.2.6 on 2023-12-08 04:43

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
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('_state', models.CharField(choices=[('ANDAMAN AND NICOBAR ISLANDS', 'PORT BLAIR'), ('ANDHRA PRADESH', 'AMARAVATI'), ('ARUNACHAL PRADESH', 'ITANAGAR'), ('ASSAM', 'DISPUR'), ('BIHAR', 'PATNA'), ('CHANDIGARH', 'CHANDIGARH'), ('CHHATTISGARH', 'RAIPUR'), ('DADRA AND NAGAR HAVELI AND DAMAN AND DIU', 'DAMAN'), ('DELHI', 'NEW DELHI'), ('GOA', 'PANAJI'), ('GUJARAT', 'GANDHINAGAR'), ('HARYANA', 'CHANDIGARH'), ('HIMACHAL PRADESH', 'SHIMLA'), ('JHARKHAND', 'RANCHI'), ('KARNATAKA', 'BANGALORE'), ('KERALA', 'THIRUVANANTHAPURAM'), ('LAKSHADWEEP', 'KAVARATTI'), ('MADHYA PRADESH', 'BHOPAL'), ('MAHARASHTRA', 'MUMBAI'), ('MANIPUR', 'IMPHAL'), ('MEGHALAYA', 'SHILLONG'), ('MIZORAM', 'AIZAWL'), ('NAGALAND', 'KOHIMA'), ('ODISHA', 'BHUBANESWAR'), ('PUDUCHERRY', 'PUDUCHERRY'), ('PUNJAB', 'CHANDIGARH'), ('RAJASTHAN', 'JAIPUR'), ('SIKKIM', 'GANGTOK'), ('TAMIL NADU', 'CHENNAI'), ('TELANGANA', 'HYDERABAD'), ('TRIPURA', 'AGARTALA'), ('UTTAR PRADESH', 'LUCKNOW'), ('UTTARAKHAND', 'DEHRADUN'), ('WEST BENGAL', 'KOLKATA')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('discription', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear')], max_length=2)),
                ('product_image', models.ImageField(upload_to='productimg')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]