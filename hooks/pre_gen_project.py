import os

os.system("gh re --new %s %s" %
          ("{{cookiecutter.repo_name}}", "{{cookiecutter.repo_description}}"))
print os.getcwd()
os.system('ls')
