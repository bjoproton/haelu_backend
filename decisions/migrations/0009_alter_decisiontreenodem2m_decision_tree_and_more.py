# Generated by Django 4.1.3 on 2023-02-24 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('decisions', '0008_add_sepsis_v1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decisiontreenodem2m',
            name='decision_tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nodes_m2m', to='decisions.decisiontree'),
        ),
        migrations.AlterField(
            model_name='decisiontreenodem2m',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='decisions.node'),
        ),
    ]
