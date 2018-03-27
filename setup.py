import setuptools

setuptools.setup(
    name="metasub-scripts",
    version="0.9.0",
    url="https://github.com/MetaSUB/metasub-scripts",

    author="David C. Danko",
    author_email="dcdanko@gmail.com",

    description="Scripts for various metasub related things",

    packages=['airtablesync'],
    package_dir={'airtablesync': 'airtablesync'},

    install_requires=[
        'click==6.7'
    ],

    entry_points={
        'console_scripts': [
            'airtable-sync=airtablesync.airtable_uploader:main',
            'cbind-tables=airtablesync.cbind_tables:main',
            'parse-plate-files=inbound_outbound_parsing.cli:main',
            'parse-qiagen-files=inbound_outbound_parsing.parse_qiagen:main',
            'airtable-upload-plate-files=inbound_outbound_parsing.airtable_upload:main'
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
