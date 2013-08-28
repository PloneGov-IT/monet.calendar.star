from setuptools import setup, find_packages
import os

version = '1.3.0.dev0'

setup(name='monet.calendar.star',
      version=version,
      description="A complete and modular site calendar application for Plone",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        ],
      keywords='plone plonegov calendar event monet',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://plone.org/products/monet.calendar.star',
      license='GPL',
      namespace_packages=['monet', 'monet.calendar'],
      include_package_data=True,
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      zip_safe=False,
      install_requires=[
          'setuptools',
          'monet.calendar.event>=0.5.0dev',
          'monet.calendar.extensions>=0.10.0dev',
          'monet.calendar.portlet',
          'monet.calendar.criteria',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
