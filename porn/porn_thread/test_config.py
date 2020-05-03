import porn
import configparser
# config = configparser.ConfigParser()
# config.read('../porn_config.ini')
# sections=config.sections()
# jh_ = config['porn.jh']
# print(sections)
# print(jh_['wawq'])


config = porn.DoConfig('../porn_config.ini')
sections = config.get_sections()
porn_jh = config.get_section('porn.jh')
print(porn_jh['wawq'])
# print(sections)