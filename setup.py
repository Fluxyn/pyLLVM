from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='pyLLVM',
    version='0.1.1',
    author='lukarao',
    description='LLVM 2.6 code generation for Python.',
    long_description='A tool for compilers/interpreters written in Python that generates LLVM 2.6 code.\n' + readme,
    license='MIT',
    packages=['pyLLVM'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Compilers',
    ]
)

