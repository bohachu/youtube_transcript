
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name="youtube-transcript",
    version="1.0.4",
    packages=find_packages(),
    py_modules=['youtube_transcript'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'youtube_transcript = youtube_transcript:main',
        ],
    },
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',)
