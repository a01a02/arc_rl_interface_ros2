from setuptools import setup

package_name = 'arc_rl_interface'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            [f'resource/{package_name}']),
        (f'share/{package_name}', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aaron',
    maintainer_email='aaron@todo.todo',
    description='ROS 2 RL interface for ARC car',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'interface_node = arc_rl_interface.interface_node:main',
        ],
    },
)
