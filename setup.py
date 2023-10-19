import setuptools

with open('README.md','r', encoding='utf-8') as f:
    description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'union_budget_sentiment'
AUTHOR_USER_NAME = 'saumil89'
SRC_REPO = 'sentiment'
AUTHOR_EMAIL = 'doshisaumilm@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version= __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Sentiment Analysis of Union Budget',
    long_description=description,
    long_description_content='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)