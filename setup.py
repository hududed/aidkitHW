from setuptools import setup

setup(
    name='challenge-hw01',
    version='0.1.0',    
    description='Python package for coding challenge',
    url='https://github.com/hududed',
    author='Hud Wahab',
    author_email='hudwahab@gmail.com',
    license='BSD 2-clause',
    packages=['challenge-hw01'],
    install_requires=['fastai',
                      'fastcore',
                      'fastinferenz'
                      'timm',
                      'tensorflow==1.15',
                      'onnx', 
                      'onnxruntime',
                      'onnx_tf @ git+https://github.com/onnx/onnx-tensorflow.git@tf-1.x#egg=onnx_tf',
                      'onnxconverter-common @ git+https://github.com/microsoft/onnxconverter-common@0d793b3f47b14e53a3d6dee31cdcef03b61d23ad#egg=onnxconverter-common',
                      ],
    )

