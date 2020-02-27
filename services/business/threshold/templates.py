from pprint import pprint as print

import json
import xmltodict
import ast
from flatten_dict import flatten
from .common import types

'''
Este módulo contém os templates das devidas alterações de tipos do documento xml.
Para alterar ou inserir algum tipo adicione um dicionário com o nome do campo,
e dentro um dicionário com o tipo e sua referência na classe types do módulo
common.py.
'''

NFe_res = {
  "chNFe" : { "type" : types.int },
  "CNPJ" : { "type" : types.int },
  "xNome" : { "type" : types.str },
  "IE" : { "type" : types.int },
  "dhEmi" : { "type" : types.datetime },
  "tpNF" : { "type" : types.int },
  "vNF" : { "type" : types.float },
  "digVal" : { "type" : types.str },
  "dhRecbto" : { "type" : types.datetime },
  "nProt" : { "type" : types.datetime },
  "cSitNFe" : { "type" : types.int }
}

NFe = {
  "ide" : {
    "cUF" : { "type" : types.int },
    "cUF" : { "type" : types.int },
    "cNF" : { "type" : types.int },
    "cNF" : { "type" : types.int },
    "natOp" : { "type" : types.str },
    "natOp" : { "type" : types.str },
    "mod" : { "type" : types.int },
    "mod" : { "type" : types.int },
    "serie" : { "type" : types.int },
    "serie" : { "type" : types.int },
    "nNF" : { "type" : types.int },
    "nNF" : { "type" : types.int },
    "dhEmi" : { "type" : types.datetime },
    "dhEmi" : { "type" : types.datetime },
    "dhSaiEnt" : { "type" : types.datetime },
    "dhSaiEnt" : { "type" : types.datetime },
    "tpNF" : { "type" : types.int },
    "tpNF" : { "type" : types.int },
    "idDest" : { "type" : types.int },
    "idDest" : { "type" : types.int },
    "cMunFG" : { "type" : types.int },
    "cMunFG" : { "type" : types.int },
    "tpImp" : { "type" : types.int },
    "tpImp" : { "type" : types.int },
    "tpEmis" : { "type" : types.int },
    "tpEmis" : { "type" : types.int },
    "cDV" : { "type" : types.int },
    "cDV" : { "type" : types.int },
    "tpAmb" : { "type" : types.int },
    "finNFe" : { "type" : types.int },
    "finNFe" : { "type" : types.int },
    "indFinal" : { "type" : types.int },
    "indFinal" : { "type" : types.int },
    "indPres" : { "type" : types.int },
    "indPres" : { "type" : types.int },
    "procEmi" : { "type" : types.int },
    "procEmi" : { "type" : types.int },
    "verProc" : { "type" : types.str },
    "verProc" : { "type" : types.str }
  },

  "emit" : {
    "CNPJ" : { "type" : types.int },
    "CNPJ" : { "type" : types.int },
    "xNome" : { "type" : types.str },
    "xFant" : { "type" : types.str },
    "xLgr" : { "type" : types.str },
    "nro" : { "type" : types.int },
    "xCpl" : { "type" : types.str },
    "xBairro" : { "type" : types.str },
    "cMun" : { "type" : types.int },
    "xMun" : { "type" : types.str },
    "UF" : { "type" : types.str },
    "CEP" : { "type" : types.int },
    "cPais" : { "type" : types.int },
    "xPais" : { "type" : types.str },
    "fone" : { "type" : types.int },
    "enderEmit" : { "type" : types.str },
    "IE" : { "type" : types.str },
    "CRT" : { "type" : types.int }
  },

  "transporta" : {
    "CNPJ" : { "type" : types.int },
    "xNome" : { "type" : types.str },
    "IE" : { "type" : types.int },
    "xEnder" : { "type" : types.str },
    "xMun" : { "type" : types.str },
    "UF" : { "type" : types.str },
    "placa" : { "type" : types.str },
    "UF" : { "type" : types.str },
    "qVol" : { "type" : types.int },
    "marca" : { "type" : types.str },
    "nVol" : { "type" : types.int },
    "pesoL" : { "type" : types.float },
    "pesoB" : { "type" : types.float },
  },

  "cobr" : {
    "nFat" : { "type" : types.int },
    "vOrig" : { "type" : types.float },
    "vDesc" : { "type" : types.float },
    "vLiq" : { "type" : types.float },
    "fat" : { "type" : types.int },
    "nDup" : { "type" : types.int },
    "dVenc" : { "type" : types.datetime },
    "vDup" : { "type" : types.float },
  },

  "infProt" : {
    "tpAmb" : { "type" : types.int },
    "verAplic" : { "type" : types.str },
    "chNFe" : { "type" : types.int },
    "dhRecbto" : { "type" : types.datetime },
    "nProt" : { "type" : types.int },
    "digVal" : { "type" : types.str },
    "cStat" : { "type" : types.int },
    "xMotivo" : { "type" : types.str },
  }
}

class validator:
  '''
  validator(schema, document, parent) -> validator
  Retorna a instancia da classe validator.

  Atributos:
  ----------
    schema : str
      Tipo do esquema xml vindo da receita.
    document : BeautifulSoup
      Documento xml como tree element pelo BeautifulSoup
    parent : nfe
      Instânca da classe pai services.sefaz.nfe
  '''
  def _underscore_reducer(self, k1, k2):
    '''Redutor de nested dicionario'''
    if k1 is None:
      return k2
    else:
      return k1 + "_" + k2

  def resNFe_v101(self):
    '''Esquema resNFe_v101. Retorna o esquema xml de nota resumida em dicionario.'''
    res = dict()
    for node, parser in NFe_res.items():
      elNode = self.document.find(node)
      if elNode != None:
        if len(elNode.findChildren()) == 0:
          res[node] = parser['type'](str(elNode.text))
        else:
          res[node] = None
      else:
        res[node] = None
    return res

  def procNFe_v400(self):
    '''Esquema procNFe_v400. Retorna o esquema xml de nota completa em dicionario.'''
    nfe = dict()
    products = list()
    product = dict()
    emit = dict(
      CNPJ=None,
      CPF=None,
      xNome=None,
      xFant=None,
      xLgr=None,
      nro=None,
      xCpl=None,
      xBairro=None,
      cMun=None,
      xMun=None,
      UF=None,
      CEP=None,
      cPais=None,
      xPais=None,
      fone=None,
      IE=None,
      IEST=None,
      IM=None,
      CNAE=None,
      CRT=None
    )
    for root, field in NFe.items():
      for node, parser in field.items():
        elRoot = self.document.find(root)
        if elRoot != None:
          elNode = elRoot.find(node)
          if elNode != None:
            if len(elNode.findChildren()) == 0:
              nfe[node] = parser['type'](str(elNode.text))
    for key, value in emit.items():
      if key in nfe.keys():
        emit[key] = nfe[key]
        del nfe[key]
    for element in self.document.find_all('det'):
      _product = xmltodict.parse(str(element), process_namespaces=False)
      product.update(dict(_product['det']['prod']))
      product.update(
        flatten(dict(_product['det']['imposto']), self._underscore_reducer)
      )
      for key, value in product.items():
        try:
          value = value.lstrip('0')
          if value == '0':
            value = 0
          elif value == '':
            value = 'None'
          product[key] = ast.literal_eval(value)
        except:
          pass
      products.append(product)
    return dict(nfe=nfe, emit=emit, products=products)

  def __init__(self, schema, document=None, parent=None):
      # schema : str
      # Quando for 'xsd', vai rodar todos os métodos referentes ao xmls parser
      #   -> document : BeautifulSoup
      #   -> parent : services.sefaz.nfe
      # Quandor for 'json', vai rodar todos os métodos referentes ao json

    if 'xsd' in schema:
      self.schema = schema
      self.document = document
      self.parent = parent
      method_access = self.schema.replace('.xsd', '').replace('.', '')
      try:
        exec('self.%s()' % method_access)
      except:
        pass
    elif 'json' in schema:
      pass
