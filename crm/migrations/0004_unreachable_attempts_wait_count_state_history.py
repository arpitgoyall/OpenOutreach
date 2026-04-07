from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0003_public_identifier_unique"),
    ]

    operations = [
        migrations.RenameField(
            model_name="deal",
            old_name="connect_attempts",
            new_name="unreachable_attempts",
        ),
        migrations.AddField(
            model_name="deal",
            name="wait_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="deal",
            name="state_history",
            field=models.JSONField(default=list),
        ),
    ]
