# Generated by Django 3.0.8 on 2020-07-21 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='role',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='role.Role', verbose_name='角色'),
        ),
    ]
