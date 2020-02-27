from django.db import models

class Overman(models.Model):
  CHOICES_LEVEL = (
    ('WC', 'Alerta de conexão'),
    ('VP', 'Produto vencido'),
    ('PP', 'Erro no pagamento'),
  )

  reference = models.CharField("Referência do chamado", max_length=8)
  instalation = models.ForeignKey('micromarket.Instalation', verbose_name="Serviço de Autopagamento", on_delete=models.SET_NULL, null=True)
  summary = models.TextField('Descrição')
  debug = models.TextField('Ações tomadas no micromarket', blank=True)
  level = models.CharField('Nível', max_length=2, choices=CHOICES_LEVEL)
  isChecked = models.BooleanField('Visualizado', default=False)

  # Meta Fields
  ddmmyyy_created = models.DateField("Criado em", auto_now_add=True)
  created = models.DateTimeField('Criado em', auto_now_add=True)
  updated = models.DateTimeField('Atualizado em', auto_now=True)

  def __str__(self):
    return "#%s" % self.reference

  class Meta:
    verbose_name = 'Inspetor'
    verbose_name_plural = 'Inspetores'
