import setuptools

with open('README.adoc', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='Covid Certificate Decoder',
    version='0.0.1',
    description='Decoder for EU COVID Certificate QR-Codes',
    long_description=long_description,
    long_description_content_type='text/asciidoc',
    author='David Wolf',
    author_email='david@wolf.gdn',
    packages=setuptools.find_packages(exclude=('tests',)),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
    install_requires=['base45', 'cbor2']
)
