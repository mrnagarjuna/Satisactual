from django.db import models
from utils.constants.choices import REC_STATUS_CHOICES, YES_NO_CHOICES,AUDIT_PERIODICITY_CHOICES,FOREX_CATEGORY,OFFICE_TYPE,CAMPAIGN_STATUS_CHOICES
from django.utils import timezone
from utils.management.file_rename import upload_to_logo_image


class MstCampaignTypes(models.Model):
    cod_campaign_type = models.CharField(max_length=4)
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')
    txt_campaign_type_desc = models.CharField(max_length=96, null=True, blank=True)
    flg_sales_campaign = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_employee_survey = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    num_min_size_for_reporting = models.SmallIntegerField(default=25)
    flg_dnc_scrub_reqd = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    flg_structured = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_response_reqd = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_targetlist_mandatory = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)

    flg_cawi = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_cati = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_capi = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True, related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True, related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mst_campaign_types'
        unique_together = ('cod_campaign_type', 'cod_rec_status')  # composite primary key

class MstCampaignTeamRole(models.Model):
    cod_team_role = models.CharField(max_length=4)
    txt_role_name = models.CharField(max_length=48, null=True, blank=True)
    flg_certification_required = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)
    flg_rating_allowed = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)
    flg_default_value = models.CharField( max_length=1, choices=YES_NO_CHOICES, default='N')
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A' )
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "mst_campaign_team_role"
        unique_together = ('cod_team_role', 'cod_rec_status')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cod_team_role} - {self.txt_role_name}"

class MstThirdPartyTypes(models.Model):
    cod_third_party_type = models.CharField(max_length=4)
    txt_third_party_type_desc = models.CharField(max_length=48, null=True, blank=True)

    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_credit_bureau = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_vendor_agency = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_builder_developer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_regulator = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_employer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_client_entity = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_authentication_agency = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_distributor_agency = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_auditor = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_lawyer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_clearing_house = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_insurer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_accredited_university = models.CharField(
        max_length=1, choices=YES_NO_CHOICES, null=True, blank=True
    )

    cod_rec_status = models.CharField(
        max_length=1, choices=REC_STATUS_CHOICES, default='A'
    )

    txt_last_maker_id = models.ForeignKey(
        'user.SecUserMaster',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_maker'
    )
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey(
        'user.SecUserMaster',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_checker'
    )
    dat_last_checker = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        elif self.txt_last_checker_id:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mst_third_party_types'
        unique_together = ('cod_third_party_type', 'cod_rec_status')
        verbose_name = 'Third Party Type'
        verbose_name_plural = 'Third Party Types'

    def __str__(self):
        return f"{self.cod_third_party_type} - {self.txt_third_party_type_desc}"
    
class MstThirdParties(models.Model):
    id_third_party = models.BigAutoField(primary_key=True)

    cod_third_party_type = models.ForeignKey(MstThirdPartyTypes,on_delete=models.SET_NULL,null=True,blank=True,related_name='third_parties')

    txt_third_party_name = models.CharField(max_length=255, null=True, blank=True)
    txt_third_party_short_name = models.CharField(max_length=48, null=True, blank=True)

    flg_credit_bureau = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_vendor_agency = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_builder_developer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_regulator = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_employer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_client_entity = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_authentication_agency = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_distributor_agency = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_auditor = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_lawyer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_clearing_house = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_insurer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_accredited_university = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    txt_our_id = models.CharField(max_length=48, null=True, blank=True)

    flg_msg_xchg_available = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    txt_msg_xchg_ip_address = models.CharField(max_length=96, null=True, blank=True)
    txt_msg_xchg_port_num = models.SmallIntegerField(null=True, blank=True)
    txt_msg_xchg_protocol = models.CharField(max_length=48, null=True, blank=True)
    txt_msg_xchg_user_id = models.CharField(max_length=48, null=True, blank=True)
    txt_msg_xchg_signature = models.CharField(max_length=48, null=True, blank=True)

    txt_msg_send_format = models.CharField(max_length=48, null=True, blank=True)
    txt_msg_recv_format = models.CharField(max_length=48, null=True, blank=True)
    txt_file_send_format = models.CharField(max_length=48, null=True, blank=True)
    txt_file_recv_format = models.CharField(max_length=48, null=True, blank=True)
    txt_file_send_folder = models.CharField(max_length=255, null=True, blank=True)
    txt_file_recv_folder = models.CharField(max_length=255, null=True, blank=True)

    num_min_score_possible = models.SmallIntegerField(null=True, blank=True)
    num_max_score_possible = models.SmallIntegerField(null=True, blank=True)

    txt_principal_contact_name = models.CharField(max_length=96, null=True, blank=True)

    txt_addr_line1 = models.CharField(max_length=96, null=True, blank=True)
    txt_addr_line2 = models.CharField(max_length=96, null=True, blank=True)
    txt_addr_line3 = models.CharField(max_length=96, null=True, blank=True)
    txt_addr_city = models.CharField(max_length=96, null=True, blank=True)
    txt_addr_pin = models.CharField(max_length=8, null=True, blank=True)
    cod_address_state = models.ForeignKey('masters.MstStateCodes',on_delete=models.SET_NULL,null=True,blank=True,related_name='third_party_state')
    cod_addr_country = models.ForeignKey('masters.MstCountryCodes',on_delete=models.SET_NULL,null=True,blank=True,related_name='third_party_state')
    dat_addr_effective = models.DateField(null=True, blank=True)

    txt_phone_num = models.CharField(max_length=48, null=True, blank=True)
    txt_email_id = models.CharField(max_length=96, null=True, blank=True)
    txt_org_url = models.CharField(max_length=96, null=True, blank=True)

    txt_escalation_1_name = models.CharField(max_length=96, null=True, blank=True)
    txt_escalation_1_phone = models.CharField(max_length=48, null=True, blank=True)
    txt_escalation_1_email = models.CharField(max_length=96, null=True, blank=True)
    txt_escalation_1_title = models.CharField(max_length=96, null=True, blank=True)

    txt_escalation_2_name = models.CharField(max_length=96, null=True, blank=True)
    txt_escalation_2_phone = models.CharField(max_length=48, null=True, blank=True)
    txt_escalation_2_email = models.CharField(max_length=96, null=True, blank=True)
    txt_escalation_2_title = models.CharField(max_length=96, null=True, blank=True)

    txt_registration_num = models.CharField(max_length=48, null=True, blank=True)
    dat_registration = models.DateField(null=True, blank=True)

    num_gl_acct = models.IntegerField(null=True, blank=True)

    bin_third_party_logo = models.CharField(max_length=255)
    flg_poa_received = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    bin_poa_doc = models.CharField(max_length=255, null=True, blank=True)

    cod_id_proof_doctyp = models.CharField(max_length=4, null=True, blank=True)
    txt_id_proof_docnum = models.CharField(max_length=48, null=True, blank=True)
    id_issuer = models.BigIntegerField(null=True, blank=True)
    txt_id_proof_issuer = models.CharField(max_length=96, null=True, blank=True)

    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_last_maker_id = models.ForeignKey(
        'user.SecUserMaster',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey(
        'user.SecUserMaster',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mst_third_parties'
        unique_together = ('id_third_party', 'cod_rec_status')

class CmpCampaigns(models.Model):
    id = models.BigAutoField(primary_key=True)

    txt_campaign_name = models.CharField(max_length=96, null=True, blank=True)
    txt_campaign_short_code = models.CharField(max_length=48, null=True, blank=True)
    txt_campaign_title = models.CharField(max_length=96, null=True, blank=True)
    txt_campaign_subtitle = models.CharField(max_length=96, null=True, blank=True)
    txt_campaign_desc = models.TextField(null=True, blank=True)

    cod_campaign_type = models.ForeignKey(MstCampaignTypes,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='campaign')

    enu_campaign_status = models.CharField(max_length=1,choices=CAMPAIGN_STATUS_CHOICES,default='D')

    flg_model_campaign = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_targeted_list = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)

    dat_start = models.DateField(null=True, blank=True)
    dat_end = models.DateField(null=True, blank=True)

    txt_camp_mgr_id = models.CharField(max_length=48, null=True, blank=True)
    id_commissioned_by_thirdparty = models.BigIntegerField(null=True, blank=True)

    bin_logo_to_display = models.ImageField(upload_to=upload_to_logo_image, null=True, blank=True)

    cod_department = models.ForeignKey('masters.MstDepartments',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='campaign')
    txt_invoice_sent_to_id = models.CharField(max_length=48, null=True, blank=True)

    cod_language = models.ForeignKey('masters.MstLanguages',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='campaign')
    cod_promo = models.ForeignKey('product.MstPromoCodes',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='campaign')
    cod_product = models.ForeignKey('product.MstProdCodes',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='campaign')

    flg_voice_recording_consent = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_video_recording_consent = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_nonconsent_terminate = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_anonymize_names = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_anonymous_response_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_allow_clarif_contact_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_allow_secure_print = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_proof_before_submit = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_invite_bids = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    num_tot_response_reqd = models.IntegerField(null=True, blank=True)
    num_attempts_per_item = models.SmallIntegerField(default=6)
    num_hours_between_attempts = models.SmallIntegerField(default=24)
    num_archival_months = models.SmallIntegerField(default=24)

    num_est_target_population = models.IntegerField(null=True, blank=True)
    num_confidence_level = models.FloatField(default=97)
    num_margin_of_error = models.FloatField(default=5)
    num_z_score_calc = models.FloatField(null=True, blank=True)
    num_sample_size = models.IntegerField(null=True, blank=True)
    num_est_contact_pct = models.SmallIntegerField(null=True, blank=True)
    num_est_response_pct = models.FloatField(null=True, blank=True)
    num_est_apply_pct = models.FloatField(null=True, blank=True)
    num_est_purchase_pct = models.SmallIntegerField(null=True, blank=True)
    amt_est_rev_per_purchase = models.FloatField(null=True, blank=True)

    txt_created_by_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,
        related_name='%(class)s_created')
    
    dat_created = models.DateField(null=True, blank=True)

    txt_qa_review_proc_name = models.CharField(max_length=96, null=True, blank=True)

    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

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
        db_table = "cmp_campaigns"
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"

    def __str__(self):
        return f"{self.id} - {self.txt_campaign_name}"

class CmpCampaignUserGeoCoverage(models.Model):
    txt_login_id = models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='campaign_geo_coverage')
    id_campaign = models.ForeignKey(CmpCampaigns,null=True,blank=True,on_delete=models.DO_NOTHING,related_name='campaign_geo_coverage')
    cod_country = models.ForeignKey('masters.MstCountryCodes',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='campaign_geo_coverage')
    cod_state = models.ForeignKey('masters.MstStateCodes',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='campaign_geo_coverage')
    cod_district = models.ForeignKey('masters.MstDistrictCodes',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='campaign_geo_coverage')
    txt_city_name = models.CharField(max_length=96, default='')
    cod_pin_code = models.ForeignKey('masters.MstPinCodes',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='campaign_geo_coverage')

    num_priority_sequence = models.SmallIntegerField(default=1)
    num_allocated = models.SmallIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "cmp_campaign_user_geo_coverage"
        verbose_name = "Campaign User Geo Coverage"
        verbose_name_plural = "Campaign User Geo Coverage"
        unique_together = (
            "txt_login_id",
            "cod_country",
            "cod_state",
            "cod_district",
            "txt_city_name",
            "cod_pin_code",
            "id_campaign",
        )

    def __str__(self):
        return f"{self.txt_login_id} | Campaign {self.id_campaign}"
    
# class CmpWaves(models.Model):
#     id_campaign = models.BigIntegerField()
#     id_campaign_wave = models.BigIntegerField()
#     txt_campaign_wave_name = models.CharField(
#         max_length=96, null=True, blank=True
#     )
#     id_contact_list = models.BigIntegerField(null=True, blank=True)
#     dat_wave_start = models.DateField(null=True, blank=True)
#     dat_wave_end = models.DateField(null=True, blank=True)

#     txt_wave_delivery_head_id = models.CharField(
#         max_length=48, null=True, blank=True
#     )
#     txt_wave_requisitioner_id = models.CharField(
#         max_length=48, null=True, blank=True
#     )

#     id_questionnaire = models.BigIntegerField(null=True, blank=True)

#     flg_one_question_format = models.CharField(
#         max_length=1,
#         choices=[('Y', 'Yes'), ('N', 'No')],
#         default='N'
#     )

#     num_tot_response_reqd = models.IntegerField(null=True, blank=True)

#     num_escalation_levels = models.SmallIntegerField(default=0)
#     num_hours_to_escalation = models.SmallIntegerField(default=48)

#     num_low_rating_below = models.SmallIntegerField(default=6)
#     num_high_rating_above = models.SmallIntegerField(default=9)

#     cod_css_theme = models.CharField(max_length=4, null=True, blank=True)

#     flg_test_wave = models.CharField(
#         max_length=1,
#         choices=[('Y', 'Yes'), ('N', 'No')],
#         null=True, blank=True
#     )

#     cod_rec_status = models.CharField(
#         max_length=1,
#         choices=[
#             ('A', 'Active'),
#             ('N', 'New'),
#             ('M', 'Modified'),
#             ('R', 'Rejected'),
#             ('C', 'Closed'),
#             ('X', 'Deleted'),
#         ],
#         default='A'
#     )

#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)

#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     class Meta:
#         db_table = "cmp_waves"
#         verbose_name = "Campaign Wave"
#         verbose_name_plural = "Campaign Waves"

#         unique_together = (
#             "id_campaign",
#             "id_campaign_wave",
#         )

#         indexes = [
#             models.Index(fields=["id_campaign"]),
#             models.Index(fields=["cod_rec_status"]),
#         ]

#     def __str__(self):
#         return f"Campaign {self.id_campaign} | Wave {self.id_campaign_wave}"
