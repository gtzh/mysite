# Generated by Django 2.2.3 on 2019-07-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spares', '0003_auto_20190720_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spare',
            name='详细细节',
            field=models.CharField(max_length=30, null=True),
        ),
    ]