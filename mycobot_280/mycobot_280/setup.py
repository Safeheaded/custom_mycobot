from setuptools import setup

import os
from glob import glob

package_name = 'mycobot_280'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # launch 文件路径
        (os.path.join('share', package_name, "launch"), glob('launch/*.launch.py')),
        # python 文件
        # (os.path.join('lib',package_name),glob(package_name+'/*.py')),
        # 配置文件
        (os.path.join('share', package_name, "config"), glob('config/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='u2',
    maintainer_email='u2@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'follow_display = mycobot_280.follow_display:main',
            'listen_real = mycobot_280.listen_real:main',
            'simple_gui = mycobot_280.simple_gui:main',
            'slider_control = mycobot_280.slider_control:main',
            'teleop_keyboard = mycobot_280.teleop_keyboard:main',
        ],
    },
)