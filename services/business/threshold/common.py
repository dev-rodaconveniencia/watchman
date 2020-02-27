import re
import gzip
import base64
from bs4 import BeautifulSoup

import dateutil.parser

from .exceptions import ValidationException

class utils:
  @classmethod
  def decompressor(self, document):
    xml = document.text
    xml = base64.b64decode(xml)
    xml = gzip.decompress(xml)
    xml = BeautifulSoup(xml, 'xml')
    return xml


class types:
  @classmethod
  def str(self, value):
    return value
  @classmethod
  def float(self, value):
    return float(value)
  @classmethod
  def list(self, value):
    return value

  @classmethod
  def int(self, value):
    if value == None or not value.isdigit():
      return None
    elif isinstance(value, str):
      value = ''.join(re.findall('\d+', value))
      value = int(value)
    else:
      raise ValidationException('The parameter could not be compiled by regex.')
    return value

  @classmethod
  def datetime(self, value):
    try:
      return dateutil.parser.parse(value)
    except Exception as ex:
      return None
