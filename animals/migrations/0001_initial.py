# Generated by Django 4.0.5 on 2022-06-14 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('characteristics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.FloatField()),
                ('weight', models.FloatField()),
                ('sex', models.CharField(max_length=15)),
                ('characteriscs', models.ManyToManyField(related_name='characteristcs', to='characteristics.characteristic')),
                ('groups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='groups.group')),
            ],
        ),
    ]
