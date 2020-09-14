call venv\scripts\activate
python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel
python -m pip install --user --upgrade twine
echo "username is aaronfulton password is JaBhdgVBT7ig"
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
rmdir /s /q dist
rmdir /s /q radariq.egg-info
pause