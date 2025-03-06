# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bike_sharing', 'bike_sharing.tools']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18.1,<2.0.0',
 'python-minifier>=2.5.0,<3.0.0',
 'scikit-learn>=0.22.2,<0.23.0']

setup_kwargs = {
    'name': 'bike_sharing-software',
    'version': '0.1.0',
    'description': 'A package for performing forecast on Bike Sharing dataset',
    'long_description': '#  Bike Sharing Forecast Software\n\nA package to forecast the cnt \n\n## Installation\n\nFor installation please first install [Poetry](https://python-poetry.org/docs/). Then make a virtual evironment using poetry. \n\n```sh\npoetry install\n```\n\n## Random Forest to the rescue\n\nTree-based models, such as Decision Trees, Random Forests, and Boosted Trees, typically don\'t perform well with one-hot encodings with lots of levels. This is because they pick the feature to split on based on how well that splitting the data on that feature will "purify" it.\n',
    'author': 'Yasaman Samiee',
    'author_email': 'Yasaman.msamiee@gamil.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.6,<3.10.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
