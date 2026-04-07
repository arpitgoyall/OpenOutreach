from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0002_add_linkedin_sync_fields"),
    ]

    operations = [
        migrations.RemoveField(model_name="chatmessage", name="answer_to"),
        migrations.RemoveField(model_name="chatmessage", name="topic"),
        migrations.RemoveField(model_name="chatmessage", name="recipients"),
        migrations.RemoveField(model_name="chatmessage", name="to"),
        migrations.AddField(
            model_name="chatmessage",
            name="sender_name",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Display name of the message sender, stored at sync time",
                max_length=200,
                verbose_name="Sender name",
            ),
        ),
    ]
