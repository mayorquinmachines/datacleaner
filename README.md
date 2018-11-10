# DataCleaner

An image sequence editor for curating image datasets. This tool was generalized from the [donkeycar](https://github.com/autorope/donkeycar) tubcleaner contribution made by [Kenneth Jiang](https://www.linkedin.com/in/kennethjiang/).

DataCleaner currently supports png images. Other image extensions coming soon!

## Requirements
* python 3
* tornado 4.5.3
* requests
* python-socketio
* flask
* eventlet
* pillow
* docopt
* h5py


## Install

Clone this repo
```
cd ~/
git clone https://github.com/mayorquinmachines/datacleaner.git
```

Install
```
sudo python3 setup.py install
```

## How to Use

You can download youtube videos to sample for image clips using this [gist](https://gist.github.com/smellslikeml/3ab14dcbd4c7961ca9f0e02f6464c6e3). You can split up the videos into png images and store them in directories like shown below.


Make sure your image file names are formatted sequentially and numbered, i.e:
```
001.png
002.png
003.png

``` 

This tool also works best with this directory structure:
```
image_dirs/
    foo/
        001.png
        002.png
        003.png
        ...
    bar/
        001.png
        002.png
        003.png
        ...
    ...
```

To run the cleaner app, run:
```
datacleaner clean /path/to/image_dirs/
```

Once its up and running, navigate to:
```
http://localhost:8886
```

