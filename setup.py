from setuptools import setup, find_packages


with open('README.md') as file:
    long_description = file.read()

setup(
    name="quickdrop",
    version="0.01",
    py_modules=['quickdrop'],
    url='https://github.com/zevaverbach/quickdrop',
    install_requires=[
        'dropbox',
        'Click',
        'pyperclip',
        ],
    include_package_data=True,
    packages=find_packages(),
    description=(
        'Quickly get a shared link for any file or folder in a Dropbox-synced '
        'folder'),
    long_description_content_type='text/markdown',
    long_description=long_description,
    entry_points='''
        [console_scripts]
        url=quickdrop.quickdrop:cli
    ''',
        )
