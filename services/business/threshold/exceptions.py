# TODO Tem que documentar este módulo assim que acabado o pacote prototypes


class ValidationException(Exception):
  SERVER_ERROR = "The value returned a invalid value. Type of field not expected."

  def __init__(self, message):
    self.message = message

  def __str__(self):
    return str(self.message)


class ProtectedAccessException(Exception):
  PROTECTED_ACCESS = "Unexpected variable access"

  def __init__(self, message):
    self.message = "%s. %s" % (PROTECTED_ACCESS, message)
  def __str__(self):
    return str(self.message)
