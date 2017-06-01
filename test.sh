pip freeze
nosetests --with-cov --cover-package pyexcel_pygal --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source pyexcel_pygal && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
