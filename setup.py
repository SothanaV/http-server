# setup.py

from setuptools import setup, find_packages

setup(
    name="http_server",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'server=http_server.server:main',
        ],
    },
    install_requires=[
        # Add any dependencies your package needs
    ],
    author="SothanaV",
    author_email="sothana.vcr@gmail.com",
    description="Simple HttpServer",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="hhttps://github.com/SothanaV/http-server.git",  # Replace with your GitHub repo or project URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)