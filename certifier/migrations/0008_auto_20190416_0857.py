# Generated by Django 2.1.7 on 2019-04-16 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certifier', '0007_auto_20190412_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackercertification',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certifier.Dataset'),
        ),
    ]
