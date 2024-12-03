import os

from glob import glob

from setuptools import find_packages, setup


package_name = 'dummy_pub_sub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='migueldm',
    maintainer_email='midemig@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dummy_pub_node = dummy_pub_sub.dummy_pub_node:main',
            'dummy_sub_node = dummy_pub_sub.dummy_sub_node:main',
        ],
    },
)
