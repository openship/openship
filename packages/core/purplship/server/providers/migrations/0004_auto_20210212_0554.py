# Generated by Django 3.1.6 on 2021-02-12 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20210125_2125'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('providers', '0003_auto_20201230_0820'),
    ]

    operations = [
        migrations.CreateModel(
            name='AramexSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('account_pin', models.CharField(max_length=200)),
                ('account_entity', models.CharField(max_length=200)),
                ('account_number', models.CharField(max_length=200)),
                ('account_country_code', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Aramex Settings',
                'verbose_name_plural': 'Aramex Settings',
                'db_table': 'aramex-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='CanparSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Canpar Settings',
                'verbose_name_plural': 'Canpar Settings',
                'db_table': 'canpar-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='DHLUniversalSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('consumer_key', models.CharField(max_length=200)),
                ('consumer_secret', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'DHL Universal Tracking Settings',
                'verbose_name_plural': 'DHL Universal Tracking Settings',
                'db_table': 'dhl_universal-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='DicomSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('billing_account', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Dicom Settings',
                'verbose_name_plural': 'Dicom Settings',
                'db_table': 'dicom-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='RoyalMailSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('client_id', models.CharField(max_length=200)),
                ('client_secret', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Royal Mail Settings',
                'verbose_name_plural': 'Royal Mail Settings',
                'db_table': 'royalmail-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='SendleSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('sendle_id', models.CharField(max_length=200)),
                ('api_key', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Sendle Settings',
                'verbose_name_plural': 'Sendle Settings',
                'db_table': 'sendle-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='SFExpressSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('partner_id', models.CharField(max_length=200)),
                ('check_word', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'SF-Express Settings',
                'verbose_name_plural': 'SF-Express Settings',
                'db_table': 'sf_express-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='USPSSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'USPS Settings',
                'verbose_name_plural': 'USPS Settings',
                'db_table': 'usps-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='YanwenSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('customer_number', models.CharField(max_length=200)),
                ('license_key', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Yanwen Settings',
                'verbose_name_plural': 'Yanwen Settings',
                'db_table': 'yanwen-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='YunExpressSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('customer_number', models.CharField(max_length=200)),
                ('api_secret', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Yunexpress Settings',
                'verbose_name_plural': 'Yunexpress Settings',
                'db_table': 'yunexpress-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.RenameModel(
            old_name='DHLSettings',
            new_name='DHLExpressSettings',
        ),
        migrations.RenameModel(
            old_name='FedexSettings',
            new_name='FedexExpressSettings',
        ),
        migrations.RenameModel(
            old_name='PurolatorSettings',
            new_name='PurolatorCourierSettings',
        ),
        migrations.RenameModel(
            old_name='UPSSettings',
            new_name='UPSPackageSettings',
        ),
    ]
