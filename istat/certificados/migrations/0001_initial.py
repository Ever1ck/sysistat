# Generated by Django 4.2 on 2023-10-28 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAuxiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEducacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CertificadoModular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_inst', models.CharField(blank=True, max_length=15)),
                ('fecha', models.DateField()),
                ('firma', models.ImageField(blank=True, upload_to='')),
                ('detalle_matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.detallematricula')),
            ],
        ),
        migrations.CreateModel(
            name='CertificadoEducacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_inst', models.CharField(blank=True, max_length=15)),
                ('registro_minedu', models.CharField(blank=True, max_length=15)),
                ('fecha', models.DateField()),
                ('firma', models.ImageField(blank=True, upload_to='')),
                ('detalle_matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.detallematricula')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificados.tipoeducacion')),
            ],
        ),
        migrations.CreateModel(
            name='CertificadoAuxiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_inst', models.CharField(blank=True, max_length=15)),
                ('fecha', models.DateField()),
                ('firma', models.ImageField(blank=True, upload_to='')),
                ('detalle_matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.detallematricula')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificados.tipoauxiliar')),
            ],
        ),
    ]