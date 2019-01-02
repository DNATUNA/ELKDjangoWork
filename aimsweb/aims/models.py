from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class LogInfo(models.Model):
    aims_id = models.CharField(max_length=100)
    host_id = models.CharField(max_length=100)
    app_id = models.CharField(max_length=100)
    app_name = models.CharField(max_length=100)
    system_status = models.CharField(max_length=100)
    log_agent_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    use_yn = models.TextField(blank=True, default="Y", max_length=1)
    prediction_qual = models.CharField(blank=True, null=True, max_length=100)
    prediction_model = models.CharField(blank=True, null=True, max_length=100)
    prediction_model_version = models.CharField(blank=True, null=True, max_length=100)
    ptn001_cnt = models.CharField(blank=True, null=True, max_length=100)
    ptn001_ratio = models.CharField(blank=True, null=True, max_length=100)
    ptn002_cnt = models.CharField(blank=True, null=True, max_length=100)
    ptn002_ratio = models.CharField(blank=True, null=True, max_length=100)
    ptn003_cnt = models.CharField(blank=True, null=True, max_length=100)
    ptn003_ratio = models.CharField(blank=True, null=True, max_length=100)
    ptn004_cnt = models.CharField(blank=True, null=True, max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.aims_id

    def get_absolute_url(self):
        return reverse("loginfo:detail", kwargs={"aims_id": self.aims_id})



class HostInfo(models.Model):
    host_id = models.CharField(max_length=100)
    host_name = models.CharField(max_length=100)
    host_ip = models.CharField(max_length=100)
    host_desc = models.CharField(max_length=100)
    use_yn = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

class AppInfo(models.Model):
    app_id = models.CharField(max_length=100)
    app_name = models.CharField(max_length=100)
    app_desc = models.CharField(max_length=100)
    use_yn = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)


class MonthlyTranInfo(models.Model):
    log_mid = models.CharField(max_length=100)
    tran_w1_cnt = models.CharField(blank=True, null=True, max_length=100)
    tran_w1_errcnt = models.CharField(blank=True, null=True, max_length=100)
    tran_w1_ratio = models.CharField(blank=True, null=True, max_length=100)
    tran_w1_errratio = models.CharField(blank=True, null=True, max_length=100)
    tran_w2_cnt = models.CharField(blank=True, null=True, max_length=100)
    tran_w2_errcnt = models.CharField(blank=True, null=True, max_length=100)
    tran_w2_ratio = models.CharField(blank=True, null=True, max_length=100)
    tran_w2_errratio = models.CharField(blank=True, null=True, max_length=100)
    tran_w3_cnt = models.CharField(blank=True, null=True, max_length=100)
    tran_w3_errcnt = models.CharField(blank=True, null=True, max_length=100)
    tran_w3_ratio = models.CharField(blank=True, null=True, max_length=100)
    tran_w3_errratio = models.CharField(blank=True, null=True, max_length=100)
    tran_w4_cnt = models.CharField(blank=True, null=True, max_length=100)
    tran_w4_errcnt = models.CharField(blank=True, null=True, max_length=100)
    tran_w4_ratio = models.CharField(blank=True, null=True, max_length=100)
    tran_w4_errratio = models.CharField(blank=True, null=True, max_length=100)
    tran_w5_cnt = models.CharField(blank=True, null=True, max_length=100)
    tran_w5_errcnt = models.CharField(blank=True, null=True, max_length=100)
    tran_w5_ratio = models.CharField(blank=True, null=True, max_length=100)
    tran_w5_errratio = models.CharField(blank=True, null=True, max_length=100)
    use_yn = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)


class WeeklyTranInfo(models.Model):
    log_mid = models.CharField(max_length=100)
    tran_d1_cnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d1_errcnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d1_ratio = models.CharField(blank=True, null=True, max_length=100)
    tran_d1_errratio = models.CharField(blank=True, null=True, max_length=100)
    tran_d2_cnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d2_errcnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d2_ratio = models.CharField(blank=True, null=True, max_length=100)
    tran_d2_errratio = models.CharField(blank=True, null=True, max_length=100)
    tran_d3_cnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d3_errcnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d3_ratio = models.CharField(blank=True, null=True, max_length=100)
    tran_d3_errratio = models.CharField(blank=True, null=True, max_length=100)
    tran_d4_cnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d4_errcnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d4_ratio = models.CharField(blank=True, null=True, max_length=100)
    tran_d4_errratio = models.CharField(blank=True, null=True, max_length=100)
    tran_d5_cnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d5_errcnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d5_ratio = models.CharField(blank=True, null=True, max_length=100)
    tran_d5_errratio = models.CharField(blank=True, null=True, max_length=100)
    tran_d6_cnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d6_errcnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d6_ratio = models.CharField(blank=True, null=True, max_length=100)
    tran_d6_errratio = models.CharField(blank=True, null=True, max_length=100)
    tran_d7_cnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d7_errcnt = models.CharField(blank=True, null=True, max_length=100)
    tran_d7_ratio = models.CharField(blank=True, null=True, max_length=100)
    tran_d7_errratio = models.CharField(blank=True, null=True, max_length=100)
    use_yn = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

