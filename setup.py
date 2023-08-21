from setuptools import setup, find_packages

setup(
    name='scrapy-sentry',
    version_format='{tag}.dev{commitcount}+{gitsha}',
    description='Sentry component for Scrapy',
    long_description=open('README.md').read(),
    author='Jordi Llonch',
    author_email='llonchj@gmail.com',
    url='https://github.com/llonchj/scrapy-sentry',
    packages=find_packages(),
    license='BSD',
    install_requires=['Scrapy>=2.6.0', 'raven>=6.3.0', 'six>=1.11.0'],
    setup_requires=['setuptools-git-version'],
    tests_require=[
        'pytest-flakes',
        'pytest-pep8',
        'pytest',
        'tox',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
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
