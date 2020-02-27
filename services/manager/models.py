from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class CompanyManager(models.Model):
  subname = models.CharField(
    "Subnome da empresa",
    max_length=80,
    help_text=_("E.g.: Sede, Região [1, 2, 3, 4], São Bernardo do Campo")
  )
  certificate_file = models.FileField("Certificado digital .pfx", upload_to="certificates")
  certificate_password = models.CharField("Senha do certificado", max_length=20)
  cnpj = models.CharField("CNPJ", max_length=14)
  manager_email = models.CharField("E-mail do responsável para contato", max_length=255)

  def __str__(self):
    return self.subname

  class Meta:
    verbose_name = 'Companhia e filial'
    verbose_name_plural = 'Companhias e filiais'

class UserManager(BaseUserManager):
  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    """
    Creates and saves an EmailUser with the given email and password.
    """
    now = timezone.now()
    if not email:
      raise ValueError('The given email must be set')
    email = self.normalize_email(email)
    user = self.model(email=email, is_staff=is_staff, is_active=True,
                      is_superuser=is_superuser, last_login=now,
                      date_joined=now, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password=None, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
      return self._create_user(email, password, True, True, **extra_fields)

class AbstractUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(_('email address'), max_length=255, unique=True, db_index=True)
  is_staff = models.BooleanField(
      _('staff status'), default=False,
      help_text=_('Designates whether the user can log into this admin site.')
  )
  is_active = models.BooleanField(
      _('active'), default=True,
      help_text=_('Designates whether this user should be treated as active. '
                  'Unselect this instead of deleting accounts.')
  )
  date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
  first_name = models.CharField(_('first name'), max_length=30, blank=True)
  last_name = models.CharField(_('last name'), max_length=30, blank=True)
  company = models.ForeignKey('CompanyManager', verbose_name="Companhia ou filial", on_delete=models.SET_NULL, blank=True, null=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  class Meta:
    verbose_name = _('user')
    verbose_name_plural = _('users')
    abstract = True

  def get_full_name(self):
    """
    Returns the email.
    """
    if self.first_name and self.last_name:
        return "{0} {1}".format(self.first_name, self.last_name)
    return self.email

  def get_short_name(self):
    """
    Returns the email.
    """
    return self.email

  def email_user(self, subject, message, from_email=None):
    """
    Sends an email to this User.
    """
    send_mail(subject, message, from_email, [self.email])


class User(AbstractUser):
  class Meta(AbstractUser.Meta):
      swappable = 'AUTH_USER_MODEL'
      abstract = False
