# Generated by Django 4.2.8 on 2023-12-14 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("providers", "0057_alter_servicelevel_weight_unit_belgianpostsettings"),
    ]

    operations = [
        migrations.CreateModel(
            name="AlliedExpressSettings",
            fields=[
                (
                    "carrier_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="providers.carrier",
                    ),
                ),
                ("username", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
                ("account", models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                "verbose_name": "Allied Express Settings",
                "verbose_name_plural": "Allied Express Settings",
                "db_table": "allied-express-settings",
            },
            bases=("providers.carrier",),
        ),
    ]