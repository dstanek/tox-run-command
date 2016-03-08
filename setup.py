from setuptools import setup


setup(
    name='tox-run-command',
    description='tox plugin to run arbitrary commands in a virtualenv',
    long_description=open('README.rst').read(),
    version='0.4',
    py_modules=['tox_run_command'],
    entry_points={'tox': ['run_command = tox_run_command']},
    install_requires=['tox>=2.0'],
    author='David Stanek',
    author_email='dstanek@dstanek.com',
    url='https://github.com/dstanek/tox-run-command',
    license='Apache Software License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
    ]
)
