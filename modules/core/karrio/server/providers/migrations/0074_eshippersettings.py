# Generated by Django 4.2.14 on 2024-07-27 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("providers", "0073_delete_eshipperxmlsettings"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="EShipperXMLSettings",
            new_name="EShipperSettings",
        ),
        migrations.AlterModelTable(
            name="eshippersettings",
            table="eshipper-settings",
        ),
    ]