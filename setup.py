from setuptools import setup, find_packages
from medacy_dataset_template import __version__, __authors__

packages = find_packages()

def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='medacy_dataset_template', #the name of the python package, prefix with medacy_dataset
    version=__version__,
    license='GNU GENERAL PUBLIC LICENSE',
    description='A template for medaCy compatible datasets', #describe the package
    long_description=readme(),
    packages=packages,
    url='https://github.com/NLPatVCU/medaCy_dataset_template',
    author=__authors__,
    author_email='contact@andriymulyar.com',
    keywords='dataset, medacy-dataset, medacy, nlp, medical-nlp',
    classifiers=[
        '( Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Topic :: Text Processing :: Linguistic',
        'Intended Audience :: Science/Research'
    ],
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=False

)
