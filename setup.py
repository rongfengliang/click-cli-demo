import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dalongrong_cli-demo",
    version="0.0.2",
    author="dalongrong",
    author_email="1141591465@qq.com",
    description="a simple cli project",
    long_description=long_description,
    install_requires=['click'],
    long_description_content_type="text/markdown",
    url="https://github.com/rongfengliang/click-cli-demo.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Documentation': 'https://github.com/rongfengliang/click-cli-demo.git',
        'Say Thanks!': 'https://github.com/rongfengliang/click-cli-demo.git',
        'Source': 'https://github.com/rongfengliang/click-cli-demo.git',
        'Tracker': 'https://github.com/rongfengliang/click-cli-demo.git',
    },
    entry_points={
        'console_scripts': [
            'dalongcli=cli:hello',
        ],
    }
)
