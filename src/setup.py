from setuptools import setup
import setup_translate

pkg = 'Extensions.Chromium'
setup(name='enigma2-plugin-extensions-chromium',
       version='3.0',
       description='E2 Chromium Plugin',
       package_dir={pkg: 'Chromium'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
