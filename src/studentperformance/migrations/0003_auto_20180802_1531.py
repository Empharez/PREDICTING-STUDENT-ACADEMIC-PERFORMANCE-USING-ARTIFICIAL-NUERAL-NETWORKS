# Generated by Django 2.1 on 2018-08-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentperformance', '0002_auto_20180802_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='higher_edu',
            field=models.BooleanField(verbose_name='Do you intend to pursue an higher education?'),
        ),
    ]