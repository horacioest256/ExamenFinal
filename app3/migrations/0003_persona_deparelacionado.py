# Generated by Django 4.2.7 on 2024-08-14 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0002_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='depaRelacionado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app3.departamento'),
        ),
    ]
