# Generated by Django 3.0.4 on 2020-04-06 17:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OfficeCode', models.IntegerField()),
                ('OfficeName', models.CharField(max_length=20)),
                ('Attribution', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OfficeCode', models.IntegerField()),
                ('SubId', models.IntegerField()),
                ('StartDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('EndDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrganizationName', models.CharField(max_length=20)),
                ('OrginizationCode', models.IntegerField()),
                ('Description', models.TextField(blank=True, null=True)),
                ('Date_Joined', models.DateTimeField(auto_now_add=True)),
                ('Address1', models.CharField(max_length=20)),
                ('Address2', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('ZipCode', models.IntegerField()),
                ('PhoneNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrginizationCode', models.IntegerField()),
                ('SubId', models.IntegerField()),
                ('StartDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('EndDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('CountryOrigin', models.CharField(max_length=20)),
                ('CitizenShip', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceCode', models.IntegerField()),
                ('ServiceName', models.CharField(max_length=20)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Premium', models.CharField(max_length=20)),
                ('Allocation', models.DecimalField(decimal_places=2, max_digits=65)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sId', models.IntegerField()),
                ('User_Name', models.CharField(max_length=20)),
                ('SubscriptTypeCode', models.IntegerField()),
                ('ServiceCode', models.IntegerField()),
                ('RequestDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('StartDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('EndDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('SubCancellation', models.CharField(max_length=20)),
                ('BeneficiaryId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubscriptTypeCode', models.IntegerField()),
                ('SubscriptTypeName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TransferdSubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransferId', models.IntegerField()),
                ('TransferFrom', models.CharField(max_length=20)),
                ('TransferTo', models.CharField(max_length=20)),
                ('Request_Date', models.DateTimeField(auto_now_add=True)),
                ('Transfer_Date', models.DateTimeField(auto_now_add=True)),
                ('SubId', models.IntegerField()),
            ],
        ),
    ]
