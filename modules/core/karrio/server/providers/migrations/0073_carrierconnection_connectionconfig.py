# Generated by Django 4.2.11 on 2024-06-08 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import functools
import karrio.server.core.fields
import karrio.server.core.models
import karrio.server.core.models.base


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("providers", "0072_rename_eshippersettings_eshipperxmlsettings_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarrierConnection",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.CharField(
                        default=functools.partial(
                            karrio.server.core.models.base.uuid,
                            *(),
                            **{"prefix": "conn_"}
                        ),
                        editable=False,
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "carrier_id",
                    models.CharField(
                        db_index=True,
                        help_text="eg. canadapost, dhl_express, fedex, purolator_courrier, ups...",
                        max_length=150,
                    ),
                ),
                (
                    "test_mode",
                    models.BooleanField(
                        db_column="test_mode",
                        default=True,
                        help_text="Toggle carrier connection mode",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        db_index=True,
                        default=True,
                        help_text="Disable/Hide carrier from clients",
                    ),
                ),
                (
                    "is_system",
                    models.BooleanField(
                        db_index=True,
                        default=False,
                        help_text="Determine that the carrier connection is available system wide.",
                    ),
                ),
                (
                    "capabilities",
                    karrio.server.core.fields.MultiChoiceField(
                        choices=[
                            ("pickup", "pickup"),
                            ("rating", "rating"),
                            ("shipping", "shipping"),
                            ("tracking", "tracking"),
                            ("paperless", "paperless"),
                            ("manifest", "manifest"),
                        ],
                        default=functools.partial(
                            karrio.server.core.models._identity, *(), **{"value": []}
                        ),
                        help_text="Select the capabilities of the carrier that you want to enable",
                    ),
                ),
                (
                    "metadata",
                    models.JSONField(
                        blank=True,
                        default=functools.partial(
                            karrio.server.core.models._identity, *(), **{"value": {}}
                        ),
                        help_text="User defined metadata",
                        null=True,
                    ),
                ),
                (
                    "credentials",
                    models.JSONField(
                        default=functools.partial(
                            karrio.server.core.models._identity, *(), **{"value": {}}
                        ),
                        help_text="Carrier connection",
                    ),
                ),
                (
                    "active_users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="connection_users",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["test_mode", "-created_at"],
            },
            bases=(karrio.server.core.models.base.ControlledAccessModel, models.Model),
        ),
        migrations.CreateModel(
            name="ConnectionConfig",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.CharField(
                        default=functools.partial(
                            karrio.server.core.models.base.uuid,
                            *(),
                            **{"prefix": "cfg_"}
                        ),
                        editable=False,
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "config",
                    models.JSONField(
                        default=functools.partial(
                            karrio.server.core.models._identity, *(), **{"value": {}}
                        )
                    ),
                ),
                (
                    "connection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="configs",
                        to="providers.carrierconnection",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Connection Config",
                "verbose_name_plural": "Connection Configs",
                "db_table": "connection-config",
                "ordering": ["-created_at"],
            },
            bases=(karrio.server.core.models.base.ControlledAccessModel, models.Model),
        ),
    ]