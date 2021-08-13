# Generated by Django 3.2.6 on 2021-08-13 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mentoringapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('user_id', models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='아이디')),
                ('user_pw', models.CharField(max_length=1000, verbose_name='비밀번호')),
                ('user_name', models.CharField(max_length=256, verbose_name='성명')),
                ('user_email', models.EmailField(max_length=256, unique=True, verbose_name='이메일')),
                ('user_register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')),
                ('user_phone_number', models.IntegerField(unique=True, verbose_name='전화번호')),
                ('user_RRN1', models.IntegerField(unique=True, verbose_name='주민번호 앞자리')),
                ('user_RRN2', models.IntegerField(unique=True, verbose_name='주민번호 뒷자리')),
                ('user_certification', models.ImageField(blank=True, upload_to='', verbose_name='본인증명서')),
                ('user_certification_check', models.BooleanField(default=False, verbose_name='인증여부')),
                ('user_cash', models.IntegerField(default=0, verbose_name='잔액')),
                ('user_school', models.CharField(default='경기대학교', max_length=256, verbose_name='학력')),
                ('user_role', models.CharField(blank=True, choices=[('멘토', '멘토'), ('멘티', '멘티')], max_length=16, verbose_name='멘토/멘티')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저',
                'db_table': 'user_table',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_at', models.DateTimeField(auto_now_add=True, verbose_name='결제 날짜/시간')),
                ('sum', models.ForeignKey(db_column='sum', on_delete=django.db.models.deletion.PROTECT, to='mentoringapp.lecture', verbose_name='합계')),
                ('user_id', models.ForeignKey(db_column='user_id', db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.user_info', verbose_name='유저 ID')),
            ],
            options={
                'verbose_name': '결제',
                'verbose_name_plural': '결제',
                'db_table': 'payment_table',
            },
        ),
        migrations.CreateModel(
            name='Menti_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField(blank=True, null=True, verbose_name='멘티 이력')),
                ('user_info_id', models.ForeignKey(db_column='user_info_id', db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_menti', to='myapp.user_info', verbose_name='멘티 ID')),
            ],
            options={
                'verbose_name': '멘티',
                'verbose_name_plural': '멘티',
                'db_table': 'menti_table',
            },
        ),
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer', models.CharField(max_length=256, verbose_name='입금자명')),
                ('cash_charge', models.IntegerField(default=0, verbose_name='충전 금액')),
                ('cash_at', models.DateTimeField(auto_now_add=True, verbose_name='충전 날짜/시간')),
                ('success_true_false', models.BooleanField(default=False, verbose_name='충전 성공 여부')),
                ('user_id', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.PROTECT, to='myapp.user_info', verbose_name='유저 ID')),
            ],
            options={
                'verbose_name': '캐시',
                'verbose_name_plural': '캐시',
                'db_table': 'cash_table',
            },
        ),
    ]
