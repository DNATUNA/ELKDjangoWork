# Generated by Django 2.0.5 on 2018-11-08 08:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aims', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginfo',
            old_name='engineer_name',
            new_name='aims_id',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='layer_id',
            new_name='app_id',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='layer_name',
            new_name='app_name',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='rheed_id',
            new_name='host_id',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='rheed_video_filename',
            new_name='log_agent_name',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='chart1_json_json_filename',
            new_name='prediction_model_version',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='chart2_json_json_filename',
            new_name='ptn001_cnt',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='chart3_json_json_filename',
            new_name='ptn001_ratio',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='env_info',
            new_name='ptn002_cnt',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='equiv_id',
            new_name='ptn002_ratio',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='frame_num',
            new_name='ptn003_cnt',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='pred_version',
            new_name='ptn003_ratio',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='product_type',
            new_name='ptn004_cnt',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='rheed_start_date',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='loginfo',
            old_name='rheed_video_input',
            new_name='system_status',
        ),
        migrations.RemoveField(
            model_name='loginfo',
            name='real_qual',
        ),
        migrations.RemoveField(
            model_name='loginfo',
            name='recipes_id',
        ),
        migrations.RemoveField(
            model_name='loginfo',
            name='rheed_video_output',
        ),
        migrations.RemoveField(
            model_name='loginfo',
            name='run_id',
        ),
        migrations.RemoveField(
            model_name='loginfo',
            name='setting_id',
        ),
        migrations.RemoveField(
            model_name='loginfo',
            name='video_time',
        ),
        migrations.AddField(
            model_name='loginfo',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
