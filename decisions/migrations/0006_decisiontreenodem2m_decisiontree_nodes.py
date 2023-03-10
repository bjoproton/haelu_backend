# Generated by Django 4.1.3 on 2023-02-24 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('decisions', '0005_decisiontree'),
    ]

    operations = [
        migrations.CreateModel(
            name='DecisionTreeNodeM2M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decision_tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decisions.decisiontree')),
                ('neg_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='decisions.node')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decisions.node')),
                ('pos_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='decisions.node')),
            ],
        ),
        migrations.AddField(
            model_name='decisiontree',
            name='nodes',
            field=models.ManyToManyField(through='decisions.DecisionTreeNodeM2M', to='decisions.node'),
        ),
    ]
