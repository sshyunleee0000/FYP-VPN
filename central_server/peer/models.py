from django.db import models

from django.utils import timezone

STATUS_CHOICES = [
        (0, 'Not Allowed'),
        (1, 'Allowed'),
]

class Peer(models.Model):
    p_no = models.AutoField(db_column='p_no', primary_key=True)
    p_title = models.CharField(db_column='p_title', max_length=255)
    p_key = models.CharField(db_column='p_key', max_length=255)
    p_ip = models.CharField(db_column='p_ip', max_length=255)
    member = models.ForeignKey(to='Member', on_delete=models.CASCADE, default=0)
    p_al = models.IntegerField(db_column='p_al', choices=STATUS_CHOICES, default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.p_title

    class Meta:
        verbose_name_plural = "Peer"
        db_table = 'peer'

class Member(models.Model):
    m_no = models.AutoField(db_column='m_no', primary_key=True)
    m_id = models.CharField(db_column='m_id', max_length=255)
    m_pw = models.CharField(db_column='m_pw', max_length=255)

    def __str__(self):
        return self.m_id
    class Meta:
        verbose_name_plural = "Member"
        db_table = 'member'
