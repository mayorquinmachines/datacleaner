# DataCleaner

An image sequence editor for curating image datasets. This tool was generalized from the [donkeycar](https://github.com/autorope/donkeycar) tubcleaner contribution made by [Kenneth Jiang](https://www.linkedin.com/in/kennethjiang/).

DataCleaner currently supports png images. Other image extensions coming soon!

## Requirements
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

Make sure your image file names are formatted sequentially and numbered, i.e:
```
001.png
002.png
003.png

``` 

This tool also works best with this directory structure:
```
image_dirs/
    foo_images/
        001.png
        002.png
        003.png
        ...
    bar_images/
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

