# Learning OpenCV

## Installation

Install Numpy and Scipy.
```
pip install numpy scipy
```

To enable access to certain proprietary algorithms, we need to install OpenCV with a custom compiler flag.
```
CMAKE_ARGS="-DOPENCV_ENABLE_NONFREE=ON" pip install -v --no-binary=opencv-contrib-python opencv-contrib-python
```

Save requirements.
```
pip freeze > requirements.txt
```
