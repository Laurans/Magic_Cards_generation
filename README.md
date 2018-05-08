# Magic_Cards_generation

## Project overview
The idea is to genererate Magic The Gathering cards with Deep Convolutional Generative Adversarial Network (and Tensorflow).
For now the cards generated look like this:

## Installation
### With Docker
#### Requirements
* Docker 18.03 and up
* [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) 2.0 and up

#### Building docker image
```
git clone https://github.com/Laurans/Magic_Cards_generation.git
cd Magic_Cards_generation
docker build -t workspace_magic_gan .
```

#### Running image
```
cd Magic_Cards_generation
nvidia-docker run -it -p 8888:8888 -v `pwd`:/workspace/ --name magic_gan workspace_magic_gan
```

It will run a jupyter server.

## Usage

### Extract data
If you want to extract data you can find the scripts in `src/extract_data`.

```
cd src/extract_data
python get_images_links.py
python extract_images.py
python check_images.py
``` 

> Beware to check your dataset for consistency

### Training or using model
There is a jupyter notebook to train and use the model : `src/models/Game Generation.ipynb`
