import os

os.system(
    'lice {{cookiecutter.license}} -y 2015 -o "{{cookiecutter.author}}" >>LICENSE')
repo_url = "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}"
os.system('git remote add origin %s' % repo_url)
