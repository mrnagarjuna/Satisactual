from django.db import models
from utils.constants.choices import REC_STATUS_CHOICES,YES_NO_CHOICES,REPORT_FORMAT_CHOICES,AV_RECORDING_CHOICES,DISPLAY_TYPE_CHOICES,BASE_QUESTION_TYPE_CHOICES
from django.utils import timezone

class MstQuestionClass(models.Model):
    cod_question_class = models.CharField(max_length=4,)
    txt_question_class_desc = models.CharField(max_length=48,null=True,blank=True)
    num_display_sequence = models.SmallIntegerField(default=1)
    flg_default_value = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES)
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True,blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "mst_question_classes"
        verbose_name = "Question Class"
        verbose_name_plural = "Question Classes"
        unique_together=('cod_question_class', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_question_class} - {self.txt_question_class_desc}"

class MstQuestionType(models.Model):
    cod_question_type = models.CharField(max_length=4)
    enu_base_question_type = models.CharField(max_length=1,choices=BASE_QUESTION_TYPE_CHOICES,default='N')
    txt_question_type_desc = models.CharField(max_length=48,null=True,blank=True)
    enu_display_type = models.CharField(max_length=10,choices=DISPLAY_TYPE_CHOICES,null=True,blank=True)
    num_display_order = models.SmallIntegerField(null=True,blank=True)
    cod_question_class = models.ForeignKey(MstQuestionClass,on_delete=models.CASCADE,null=True,blank=True,related_name='question_types')
    num_max_chars_response = models.SmallIntegerField(default=255)
    txt_response_format = models.CharField(max_length=255,null=True,blank=True)
    flg_rating_base_zero = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    flg_rating_one_highest = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)
    txt_high_rating_label = models.CharField(max_length=48,null=True,blank=True)
    txt_low_rating_label = models.CharField(max_length=48,null=True,blank=True)
    num_rating_levels = models.SmallIntegerField(default=5)
    enu_report_format = models.CharField(max_length=10,choices=REPORT_FORMAT_CHOICES,null=True,blank=True)
    flg_av_recording_reqd = models.CharField(max_length=1,choices=AV_RECORDING_CHOICES,default='N')
    flg_simple_question = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    bin_question_icon = models.TextField(null=True,blank=True)
    flg_default_value = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True,blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "mst_question_types"
        unique_together=('cod_question_type','enu_base_question_type','cod_rec_status')
        

    def __str__(self):
        return f"{self.cod_question_type} - {self.txt_question_type_desc}"