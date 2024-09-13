from setuptools import setup, find_packages

setup(
    name='file-processing-transcription',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'torch',
        'openai-whisper',
    ],
)
