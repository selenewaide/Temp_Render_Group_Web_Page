from setuptools import setup

setup(name="bike-website",
      version="0.1",
      description="bike website in COMP30670 2017",
      url="",
      author="Louise Klodt",
      author_email="louiseklodt@ucdconnect.ie",
      licence="GPL3",
      packages=['bike-website'],
      entry_points={
        'console_scripts':['bike-website=bike-website.__main__:main']
        }
      )