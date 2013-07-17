from setuptools import setup, find_packages

setup(name='scrapy-sentry',
      version='0.6.1',
      description='Sentry component for Scrapy',
      long_description=open('README.md').read(),
      author='Jordi Llonch',
      author_email='llonchj@gmail.com',
      url='https://github.com/llonchj/scrapy-sentry',
      packages=find_packages(),
      license='BSD',
      install_requires=['Scrapy>0.16', 'raven'],
      classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Environment :: Console',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Internet :: WWW/HTTP',
        ]
    )
