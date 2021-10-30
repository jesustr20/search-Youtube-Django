from django.db import models



class Community_info(models.Model):
    title = models.CharField(verbose_name='Título', max_length=300, blank=True, null=True)
    description = models.TextField(verbose_name='Descripción', blank=True, null=True)
    r_social1 =models.CharField(verbose_name='Facebook',max_length=200, blank=True, null=True)
    r_social2 =models.CharField(verbose_name='Instagram',max_length=200, blank=True, null=True)
    r_social3 =models.CharField(verbose_name='Linkedin',max_length=200, blank=True, null=True)
    r_social4 =models.CharField(verbose_name='Telegram',max_length=200, blank=True, null=True)
    r_social5 =models.CharField(verbose_name='Twitter',max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Community_info'
        verbose_name_plural = 'Community_infos'
        ordering = ['id']

class Link_Enlace(models.Model):
    whatsapp = models.CharField(verbose_name='Whatsapp', max_length=200, blank=True, null=True)
    telegram = models.CharField(verbose_name='Telegram', max_length=200, blank=True, null=True)
    discord = models.CharField(verbose_name='Discord', max_length=200, blank=True, null=True)

    def __str__(self):
        return f'Grupo: {self.whatsapp}'

    class Meta:
        verbose_name='Link_Enlace'
        verbose_name_plural = 'Links_Enlaces'
        ordering = ['id']

class EnlacesAPI(models.Model):
    name = models.CharField(max_length=300)
    FIELDNAME = models.URLField()


