from setuptools import find_packages
from setuptools import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print(
        "warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()
requires = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name="{{cookiecutter.repo_name}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.repo_description}}",
    long_description=read_md('README.md'),
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}",
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    test_suite="tests",
    license="{{cookiecutter.license}}",
    zip_safe=False,
    classifiers=(
    )
)
