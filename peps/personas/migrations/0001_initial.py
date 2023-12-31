# Generated by Django 4.2.3 on 2023-11-23 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonaPEP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=20, unique=True)),
                ('es_pep', models.CharField(default='Si', max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('tipo_pep', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_vinculacion', models.DateField()),
                ('fecha_desvinculacion', models.DateField(blank=True, null=True)),
                ('cuentas_extranjeras', models.CharField(max_length=50)),
                ('fecha_registro_pep', models.DateField()),
                ('fecha_actualizacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=20)),
                ('parentesco', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('persona_pep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiares', to='personas.personapep')),
            ],
        ),
    ]
