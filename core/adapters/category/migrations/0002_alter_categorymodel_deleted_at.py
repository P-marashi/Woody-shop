# Generated by Django 4.2.3 on 2024-07-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]