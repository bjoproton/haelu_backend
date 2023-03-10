# Generated by Django 4.1.3 on 2023-02-24 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64, unique=True)),
                ('value_type', models.PositiveSmallIntegerField(choices=[(0, 'Boolean'), (1, 'Integer'), (2, 'Float')], default=0)),
                ('unit', models.CharField(default='', max_length=12)),
            ],
            options={
                'verbose_name': 'Marker',
                'verbose_name_plural': 'Markers',
            },
        ),
        migrations.CreateModel(
            name='MarkerResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(default='', max_length=64)),
                ('marker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markers.marker')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Marker Result',
                'verbose_name_plural': 'Marker Results',
            },
        ),
    ]
