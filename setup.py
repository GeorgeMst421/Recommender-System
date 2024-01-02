from setuptools import setup, find_packages

setup(
    name='final_project',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'recommender = full_data_project.main:main',
            'preprocess = full_data_project.preprocess:preprocess',
            'recommender100 = full_data_project.main_100:main',
            'preprocess100 = full_data_project.preprocess_100:preprocess'
        ],
    },
)


