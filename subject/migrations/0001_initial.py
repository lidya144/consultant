# Generated by Django 2.1.7 on 2020-07-28 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('subjectId', models.AutoField(primary_key=True, serialize=False)),
                ('subjectName', models.CharField(max_length=255)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grade_subejct', to='grade.GradeModel')),
            ],
        ),
    ]
