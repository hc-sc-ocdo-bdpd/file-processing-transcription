from setuptools import setup, find_packages

setup(
    name='file-processing-transcription',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'torch==2.3.1',
        'openai-whisper==20231117',
        'pytest==8.3.3',
        'numpy==1.26.4',
        'file-processing-test-data @ git+https://github.com/hc-sc-ocdo-bdpd/file-processing-test-data.git@main'
    ],
)
