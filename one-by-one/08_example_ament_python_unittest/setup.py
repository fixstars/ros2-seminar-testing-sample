from setuptools import setup

package_name = 'example_ament_python_unittest'

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
    description='ament_python unittest example',
    license='MIT',
    entry_points={
        'console_scripts': [
        ],
    },
)
