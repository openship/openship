# Generated by Django 4.1.4 on 2022-12-17 11:46

from django.db import migrations, models
import karrio.server.core.utils as utils
import karrio.lib as lib


def forwards_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    APILog = apps.get_model("core", "APILog")
    APILogIndex = apps.get_model("core", "APILogIndex")
    logs = APILog.objects.using(db_alias).filter(
        models.Q(response__contains="test_mode")
    )

    for log in logs:
        response = utils.failsafe(lambda: lib.to_dict(lib.to_dict(log.response)))
        entity_id = utils.failsafe(lambda: response["id"])
        test_mode = utils.failsafe(lambda: response["test_mode"])

        if test_mode is None and '"test_mode": true' in log.response:
            test_mode = True
        if test_mode is None and '"test_mode": false' in log.response:
            test_mode = False

        if test_mode is not None and hasattr(log, "apilogindex"):
            log.apilogindex.test_mode = test_mode
            log.apilogindex.save()

        if hasattr(log, "apilogindex") is False:
            _index = APILogIndex(
                apirequestlog_ptr=log,
                entity_id=entity_id,
                test_mode=test_mode,
            )
            _index.save_base(raw=True)

        log.response = utils.DP.jsonify(response)
        log.save()


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_apilogindex"),
    ]

    operations = [
        migrations.AddField(
            model_name="apilogindex",
            name="test_mode",
            field=models.BooleanField(
                default=True, help_text="execution context", null=True
            ),
        ),
        migrations.RunPython(forwards_func, reverse_func),
    ]
