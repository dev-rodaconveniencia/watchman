'''
  Este módulo busca as nfe-s por critérios de formato da variável search. Todos
  os dados contidos no webservice a contar 90 dias anteriores a busca podem ser
  linkados aqui.
  Para usar os dados da receita basta buscar inserir os dados necessários para
  a consulta:

  import services
  sefaz = services.sefaz.nfe('path_do_pfx', 'senha', 'cnpj')
  # TODO vamos precisar guardar os pfxs dentro do banco. Para isso, recomendo o
  # uso do base64 e do gzip. Logo em seguida, deve ser feita a descompressão do
  # arquivo por uma nova classe dentro do sefaz.common.pfx(b'zzzzzzzz...').
  tracker = sefaz.tracker(search=[nsu, chave_nfe, None,...], pack=False)
  # search=None retornará todos os dados que estão transitando na receita.
  # pack == True: retornará um pacote de dados a partir do último NSU
  # pack == False: retornará apenas o NSU pedido
  models = sefaz.models(tracker)
'''

import re
from retrying import retry
from bs4 import BeautifulSoup
from pytrustnfe.certificado import Certificado
from pytrustnfe.nfe import consulta_distribuicao_nfe
# FIX: Parece que os warnings HTTPs de segurança estavam aumentando o tempo de
# execução da biblioteca.
# TODO: Rever os alertas de warning quando estivermos reescrevendo o pytrustnfe
import urllib3
urllib3.disable_warnings()

from .threshold import templates, common

class nfe(object):
  '''
  nfe(pfxpath, password, cnpj) -> nfe
  Retorna a instancia da classe nfe.

  Atributos:
  ----------
    pfxpath : str
      Local do certificado digital
    password : str
      Chave de acesso ao certificado para descriptografia
    cnpj : str
      Identificador da empresa destinatária
  '''
  def __init__(self, pfxpath, password, cnpj):
    '''
    Recebe o path do pfx, senha e cnpj.
    '''
    self.package = None
    self._pfxpath = pfxpath
    self._password = password
    self._cnpj = cnpj

    with open(self._pfxpath, 'rb') as file:
      self.locksmith = Certificado(file.read(), password)

  @retry(wait_fixed=3500)
  def _query(self, **kwargs):
    '''
    Busca parametrica na biblioteca TrustNFe.
    return : xml element tree
    '''
    response = consulta_distribuicao_nfe(
      self.locksmith,
      ambiente=1,
      estado='33',
      modelo='55',
      cnpj_cpf=self._cnpj,
      **kwargs
    )
    document = BeautifulSoup(response['received_xml'], 'xml')
    return document

  def _nsu_range(self):
    '''
    Busca o primeiro e último nsu.
    return : list(str, str)
    '''
    response = self._query(ultimo_nsu='000000000000000')
    print(response)
    return (response.find('ultNSU').text, response.find('maxNSU').text)

  def tracker(self, search=None, pack=False):
    '''
    Busca por nsu ou chave de acesso os dados da receita.
    Quando pack=True, retorna um pacote de dados a partir do nsu.
    Quando pack=False, retorna um unico dado a partir do nsu.
    Quando a busca é feita pela chave de acesso, pack sempre será False.

    return : BeautifulSoup
    '''
    documents = list()
    package = list()
    if search == None:
      # busca absolutamente todas as notas da receita em 90 dias
      # o servidor do webservice guarda apenas 670 notas por cnpj
      first_nsu, last_nsu = self._nsu_range()
      first_nsu = int(first_nsu)
      last_nsu = int(last_nsu)
      for nsu in range(first_nsu, last_nsu - 1, 50):
        nsu = str(nsu).zfill(15)
        xmls = self._query(ultimo_nsu=nsu)
        documents.extend(xmls.find_all('docZip'))
    elif len(search) == 15:
      nsu = str(int(search) - 1).zfill(15)
      xmls = self._query(ultimo_nsu=nsu)
      xmls = xmls.find_all('docZip')
      if len(xmls) == 0:
        raise AttributeError('Invalid NSU.')
      elif pack:
        documents = xmls
      else:
        documents = [xmls[0]]
    elif len(search) == 44:
      xmls = self._query(chave_nfe=search)
      documents = [xmls.find('docZip')]
    else:
      raise Exception('Search format error. Try 000000000000000 ' \
                      + 'or 00000000000000000000000000000000000000000000')
    for document in documents:
      schema = document.attrs['schema']
      xmls = common.utils.decompressor(document)
      package.append([schema, xmls])

    self.package = package
    return self._models()

  def _models(self):
    '''
    Cataloga e retorna uma lista de dicionários contendo as informações da NFe.
    return : list(dict)
    '''
    models = list()
    for pack in self.package:
        schema = pack[0]
        document = pack[1]
        nfe_model = templates.validator(schema, document, self)
        method_access = schema.replace('.xsd', '').replace('.', '')
        try:
          nfe_model = eval('nfe_model.%s()' % method_access)
          nfe_model["schema"] = schema
          models.append(nfe_model)
        except:
          pass
    return models
