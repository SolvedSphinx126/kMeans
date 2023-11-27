This program was tested on Ubuntu (WSL) with Python 3.10

This program depends on:
    numpy
    pandas
    scipy
    scikit-learn
```
kMeans/
├── data_formatter.py
├── iris_data
│   ├── Index
│   ├── bezdekIris.data
│   ├── iris.data
│   └── iris.names
├── kMeans.py
├── libsvm-3.32
│   ├── COPYRIGHT
│   ├── FAQ.html
│   ├── Makefile
│   ├── Makefile.win
│   ├── README
│   ├── heart_scale
│   ├── java
│   │   ├── Makefile
│   │   ├── libsvm
│   │   │   ├── svm.java
│   │   │   ├── svm.m4
│   │   │   ├── svm_model.java
│   │   │   ├── svm_node.java
│   │   │   ├── svm_parameter.java
│   │   │   ├── svm_print_interface.java
│   │   │   └── svm_problem.java
│   │   ├── libsvm.jar
│   │   ├── svm_predict.java
│   │   ├── svm_scale.java
│   │   ├── svm_toy.java
│   │   └── svm_train.java
│   ├── matlab
│   │   ├── Makefile
│   │   ├── README
│   │   ├── libsvmread.c
│   │   ├── libsvmwrite.c
│   │   ├── make.m
│   │   ├── svm_model_matlab.c
│   │   ├── svm_model_matlab.h
│   │   ├── svmpredict.c
│   │   └── svmtrain.c
│   ├── python
│   │   ├── MANIFEST.in
│   │   ├── Makefile
│   │   ├── README
│   │   ├── libsvm
│   │   │   ├── __init__.py
│   │   │   ├── commonutil.py
│   │   │   ├── svm.py
│   │   │   └── svmutil.py
│   │   └── setup.py
│   ├── svm-predict
│   ├── svm-predict.c
│   ├── svm-scale
│   ├── svm-scale.c
│   ├── svm-toy
│   │   ├── qt
│   │   │   ├── Makefile
│   │   │   └── svm-toy.cpp
│   │   └── windows
│   │       └── svm-toy.cpp
│   ├── svm-train
│   ├── svm-train.c
│   ├── svm.cpp
│   ├── svm.def
│   ├── svm.h
│   ├── svm.o
│   └── tools
│       ├── README
│       ├── checkdata.py
│       ├── easy.py
│       ├── grid.py
│       └── subset.py
└── readme.md
```

libsvm must be compiled with `make` first

The command to run this program should be something like 
`<path to python executable> <path to kMeans.py>`

on Ubuntu this was:
`python3 ./kMeans.py`
