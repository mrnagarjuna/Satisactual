from django.db import models
from utils.constants.choices import REC_STATUS_CHOICES, YES_NO_CHOICES,AUDIT_PERIODICITY_CHOICES,FOREX_CATEGORY,OFFICE_TYPE,AUDIT_FREQ_CHOICES,BASE_COLL_TYPE_CHOICES,DEPR_METHOD_CHOICES,REVIEW_FREQ_CHOICES,BASE_CHANNEL_CHOICES,MAIL_PROTOCOL_CHOICES
from django.utils import timezone

class MstContactChannel(models.Model):
    cod_channel = models.CharField(max_length=4)
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_channel_desc = models.CharField(max_length=48, null=True, blank=True)

    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    enu_base_channel = models.CharField(max_length=4, choices=BASE_CHANNEL_CHOICES, null=True)

    flg_email_supported = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True)
    flg_SMS_supported = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True)
    flg_auto_dialer_supported = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True)

    cod_auto_dialer = models.CharField(max_length=4, null=True, blank=True)

    enu_mail_protocol = models.CharField(max_length=1, choices=MAIL_PROTOCOL_CHOICES, default='S')
    txt_email_id_for_send = models.CharField(max_length=48, null=True, blank=True)
    txt_email_signature = models.TextField(null=True, blank=True)
    txt_email_signature_2fa = models.TextField(null=True, blank=True)
    txt_smtp_client = models.CharField(max_length=255, null=True, blank=True)

    flg_enable_ssl = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True)
    num_smtp_port = models.SmallIntegerField(default=25)

    txt_pop3_username = models.CharField(max_length=48, null=True, blank=True)
    txt_pop3_client = models.CharField(max_length=255, null=True, blank=True)
    num_pop3_port = models.SmallIntegerField(default=995)
    txt_pop3_encryption = models.CharField(max_length=4, null=True, blank=True)

    txt_imap_username = models.CharField(max_length=48, null=True, blank=True)
    txt_imap_client = models.CharField(max_length=255, null=True, blank=True)
    num_imap_port = models.SmallIntegerField(default=993)
    txt_imap_encryption = models.CharField(max_length=4, null=True, blank=True)

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "mst_contact_channel"
        unique_together = ('cod_channel', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_channel} - {self.txt_channel_desc}"
    
class MstContactOutcome(models.Model):
    cod_contact_outcome = models.CharField(max_length=4)
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_contact_outcome_desc = models.CharField(max_length=96, null=True, blank=True)
    cod_parent_outcome = models.CharField(max_length=4, null=True, blank=True)

    enu_base_channel_type = models.CharField(max_length=4, choices=BASE_CHANNEL_CHOICES, null=True)

    flg_valid_outcome = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_retry = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_use_for_followup = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_outbound = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "mst_contact_outcome"
        unique_together = ('cod_contact_outcome', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_contact_outcome} - {self.txt_contact_outcome_desc}"
    
# class MstContractEvents(models.Model):
#     cod_event = models.CharField(max_length=4)
#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

#     txt_event_desc = models.CharField(max_length=48)

#     flg_owners_alerts = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
#     flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

#     txt_last_maker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.pk:  
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = "mst_contract_events"
#         unique_together = ('cod_event', 'cod_rec_status')

#     def __str__(self):
#         return f"{self.cod_event} - {self.txt_event_desc}"
    
# class MstContractTypes(models.Model):
#     cod_contract_type = models.CharField(max_length=4)
#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

#     txt_contract_type_desc = models.CharField(max_length=48, null=True, blank=True)
#     flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

#     txt_last_maker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.pk:  
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = "mst_contract_types"
#         unique_together = ('cod_contract_type', 'cod_rec_status')

#     def __str__(self):
#         return f"{self.cod_contract_type} - {self.txt_contract_type_desc}"
