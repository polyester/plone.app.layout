from setuptools import find_packages
from setuptools import setup

version = '2.3.11.dev0'
long_description = (
    open('README.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(name='plone.app.layout',
      version=version,
      description="Layout mechanisms for Plone",
      long_description=long_description,
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
      ],
      keywords='plone layout viewlet',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.app.layout',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
          test=[
              'Products.PloneTestCase',
              'unittest2',
              'plone.app.intid',
              'plone.app.relationfield',
              'plone.app.testing',
          ],
      ),
      install_requires=[
          'setuptools',
          'plone.app.portlets',
          'plone.app.viewletmanager>=1.2',
          'plone.i18n',
          'plone.locking',
          'plone.memoize',
          'plone.portlets',
          'zope.annotation',
          'zope.component',
          'zope.deprecation',
          'zope.dottedname',
          'zope.i18n',
          'zope.interface',
          'zope.publisher',
          'zope.schema',
          'zope.viewlet',
          'Acquisition',
          'DateTime',
          'Products.CMFCore',
          'Products.CMFDefault',
          'Products.CMFDynamicViewFTI',
          'Products.CMFEditions>=1.2.2',
          'Products.CMFPlone',
          'Zope2',
      ],
      )
