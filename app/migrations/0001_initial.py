# Generated by Django 3.0.1 on 2019-12-18 13:52

from django.db import migrations, models
import django.db.models.deletion


def create_object(apps, schema_editor):
    Key = apps.get_model('app', 'Key')
    Value = apps.get_model('app', 'Value')

    k = Key.objects.create(name='a')

    Value.objects.create(key=k, value='b')


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Key')),
            ],
        ),
        migrations.RunPython(create_object, migrations.RunPython.noop),
    ]
