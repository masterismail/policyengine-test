from setuptools import setup, find_packages

setup(
    name='policyengine',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'policyengine_us',
        'policyengine_uk',
        #'policyengine_canada'
    ],
)

#sphinx-build /home/tahseer/Desktop/policyengine-test/docs /home/tahseer/Desktop/policyengine-test/docs/_build/html -b html