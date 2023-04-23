# Generated by Django 4.1.7 on 2023-03-27 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0003_alter_worker_position"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="worker",
            options={"verbose_name": "worker", "verbose_name_plural": "workers"},
        ),
        migrations.AlterField(
            model_name="task",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="worker",
            name="position",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="workers",
                to="tasks.position",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="worker",
            name="years_of_experience",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]