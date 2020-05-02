from configparser import ConfigParser


class DoConfig:
  def __init__(self, filepath, encoding='utf-8'):
    self.cf = ConfigParser()
    self.cf.read(filepath, encoding)

  # 获取所有的section
  def get_sections(self):
    return self.cf.sections()

  # 获取某一section下的所有option
  def get_option(self, section):
    return self.cf.options(section)

  # 获取section、option下的某一项值-str值
  def get_strValue(self, section, option):
    return self.cf.get(section, option)

  # 获取section、option下的某一项值-int值
  def get_intValue(self, section, option):
    return self.cf.getint(section, option)

  # 获取section、option下的某一项值-float值
  def get_floatValue(self, section, option):
    return self.cf.getfloat(section, option)

  # 获取section、option下的某一项值-bool值
  def get_boolValue(self, section, option):
    return self.cf.getboolean(section, option)

  def setdata(self, section, option, value):
    return self.cf.set(section, option, value)


if __name__ == '__main__':
  cf = DoConfig('demo.conf')
  res = cf.get_sections()
  print(res)
  res = cf.get_option('db')
  print(res)
  res = cf.get_strValue('db', 'db_name')
  print(res)
  res = cf.get_intValue('db', 'db_port')
  print(res)
  res = cf.get_floatValue('user_info', 'salary')
  print(res)
  res = cf.get_boolValue('db', 'is')
  print(res)

  cf.setdata('db', 'db_port', '3306')
  res = cf.get_strValue('db', 'db_port')
  print(res)
