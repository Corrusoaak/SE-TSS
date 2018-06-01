# Generated by Django 2.0.5 on 2018-05-26 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coures_select_relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_state', models.PositiveSmallIntegerField(choices=[(0, '未筛选'), (1, '选上'), (2, '未选上')])),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(default='null', max_length=10, primary_key=True, serialize=False, verbose_name='课号')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='名称')),
                ('course_type', models.PositiveSmallIntegerField(choices=[(0, '公共课'), (1, '专业选修课'), (2, '专业必修课')], verbose_name='课程类别')),
            ],
        ),
        migrations.CreateModel(
            name='course_selecting_event',
            fields=[
                ('event_label', models.CharField(default='未命名选课事件', max_length=30, primary_key=True, serialize=False)),
                ('begin_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('sec_begin', models.DateTimeField()),
                ('sec_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='所在院系')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('major', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='开设专业')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='major', to='xkxt.Department', verbose_name='所在院系')),
            ],
        ),
        migrations.CreateModel(
            name='major_cul_prog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mjr_cul_cid', to='xkxt.Course')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mjr_cul_major', to='xkxt.Major')),
            ],
        ),
        migrations.CreateModel(
            name='major_requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_course_mincredit', models.PositiveSmallIntegerField(default=0)),
                ('major_optional_mincredit', models.PositiveSmallIntegerField(default=0)),
                ('major', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mjr_req_major', to='xkxt.Major')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id_number', models.CharField(default='null', max_length=18, primary_key=True, serialize=False, verbose_name='身份证号')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='姓名')),
                ('major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='xkxt.Major', verbose_name='专业')),
            ],
        ),
        migrations.CreateModel(
            name='student_cul_prog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected', models.BooleanField(default=False)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_cul_cid', to='xkxt.Course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_cul_sid', to='xkxt.Student')),
            ],
        ),
        migrations.AddField(
            model_name='coures_select_relation',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selecting_cid', to='xkxt.Course'),
        ),
        migrations.AddField(
            model_name='coures_select_relation',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selecting_sid', to='xkxt.Student'),
        ),
    ]
