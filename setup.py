import setuptools

setuptools.setup(
    name="metasub-scripts",
    version="0.9.0",
    url="https://github.com/MetaSUB/metasub-scripts",

    author="David C. Danko",
    author_email="dcdanko@gmail.com",

    description="Scripts for various metasub related things",

    packages=['airtable-sync'],
    package_dir={'airtable-sync': 'airtable-sync'},

    install_requires=[
        'click==6.7'
    ],

    entry_points={
        'console_scripts': [
            'airtable-sync=airtable-sync.airtable-uploader:main'
        ]
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
