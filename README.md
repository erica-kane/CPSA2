# Planning For Drunks 

## Introduction 

This practical will run a model that will produce a heat map representing the paths 25 
drunks. These paths show movements made by the drunks whilst navigating their way home from a pub in a village. 

## Contents 

The project requires the user to download the following files:

### drunk.plan.txt

- A 300 x 300 town plan 


### buildingclass.py

- Defines the building super class 
- Defines the pub and house sub classes 


### drunkclass.py 

- Defines the drunk class 


### drunkmodel.py 

- Sets up and runs the model:

    1. Loads the town plan and visualises it
    2. Simulates the movements of the drunks 
    3. Visualises the paths taken in a heat map
    4. Writes out the the map to a file as text



## Running the model 


### How to run 

```
python drunkmodel.py
```

Ensure you have the numpy and matplotlib libraries installed



### What to expect 

When you run the model 3 figures should pop out:

1. A visualisation of the town plan 
2. A graph used to test coordinates of houses have been read correctly
3. The final heat map 

A file will be saved in the working directory titled 'townmapfile.csv'.
This is the information which forms the heat map as text. 

_Please note that the figures can only be viewed one by one, and you must close one for the next to open_ 


## Tests


Tests are provided as doctests 


### How to test 

```
python -m doctest buildingclass.py
```


## License

This project is licensed under MIT license.
See license in files.
