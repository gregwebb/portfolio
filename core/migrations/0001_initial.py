# Generated by Django 2.0.6 on 2018-07-07 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shares', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('risk', models.IntegerField(choices=[(0, 'None Selected'), (1, 'Conservative'), (2, 'Balanced'), (3, 'Growth'), (4, 'Aggresive')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=20)),
                ('ticker_description', models.TextField()),
                ('asset_class', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('ticker', 'ticker_description'),
            },
        ),
        migrations.AddField(
            model_name='holding',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Model'),
        ),
        migrations.AddField(
            model_name='holding',
            name='ticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Ticker'),
        ),
    ]