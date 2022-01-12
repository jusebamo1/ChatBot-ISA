# Generated by Django 2.1.5 on 2021-10-07 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isa', '0006_normatividad'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoFrec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intent', models.TextField(max_length=255)),
                ('nombre', models.TextField(max_length=255, null=True)),
                ('info', models.TextField(max_length=255, null=True)),
                ('complemento', models.TextField(blank=True, max_length=255, null=True)),
                ('ultimaModificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
