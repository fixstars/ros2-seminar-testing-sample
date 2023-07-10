from setuptools import setup

package_name = 'example_launch_pytest'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Shuhei Aoki',
    maintainer_email='shuhei.aoki@fixstars.com',
    description='launch_pytest example',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'twice=example_launch_pytest.twice:main'
        ],
    },
)
