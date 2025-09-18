from setuptools import setup, find_packages

setup(
    name="document_validator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'google-generativeai>=0.3.0',
        'google-cloud-firestore>=2.0.0',
    ],
    python_requires='>=3.8',
)