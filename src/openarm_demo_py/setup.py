from setuptools import find_packages, setup

package_name = 'openarm_demo_py'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='myvh',
    maintainer_email='myvh@example.com',
    description='ROS 2 Python demo package covering Nodes, Topics, Services, Parameters, and Actions',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'arm_publisher = openarm_demo_py.topic_publisher:main',
            'arm_subscriber = openarm_demo_py.topic_subscriber:main',
            'arm_service_server = openarm_demo_py.service_server:main',
            'arm_service_client = openarm_demo_py.service_client:main',
            'arm_param_demo = openarm_demo_py.param_demo:main',
            'arm_action_server = openarm_demo_py.action_server:main',
            'arm_action_client = openarm_demo_py.action_client:main',
        ],
    },
)
