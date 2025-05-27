# corn-leaf-disease-classifier

This project attempts to classify images of corn leaves to identify presence or absence of disease.

The models trained include a:
- Convolutional Neural Network (CNN)
- Support Vector Machine (SVM)

The image classifications consist of:
- Healthy
- Blight
- Common Rust
- Gray Leaf Spot

The commands listed below assume a Windows installation.
The dataset was provided for use in the project.

## Setup

First, follow the linked instructions install [https://pipx.pypa.io/stable/installation/](Poetry), a dependency manager for Python.

Install Python 3.12 natively, or through Poetry, and create a virtual environment in the project root directory.

Next, open a terminal instance.

- Go to the root (`/`) directory and run:
```
poetry run pip install ipykernel
```
The first command allows Jupyter notebooks to be run with Python in the Poetry environment.

## Convolutional Neural Network (CNN)

The Python notebook for running the CNN may be found in the `/cnn` directory of the project.
- `/cnn/cnn.ipynb` for the CNN proper
- `/cnn/cnn_demo.ipynb` for the CNN demo (but use the web app)

## Support Vector Machine (CNN)

The Python notebook for running the SVM may be found in the `/svm` directory of the project.
- `/svm/svm.ipynb` for the SVM proper
- `/svm/svm_demo.ipynb` for the SVM demo (but use the web app)

## Web Application

An offline web application exists for the demo, although Python notebooks also exist

To run the web app, first open a terminal instance.

- Go to the `/app` directory, and run:
```
npm install
npm run dev
```
- Go to the `/server` directory, and run:
```
uvicorn main:app --reload
```