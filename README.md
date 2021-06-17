# Projects of Methods of Scientific Computing

## Authors

* Christian Bernasconi
* Gabriele Ferrario
* Riccardo Pozzi
* Marco Ripamonti

### Project 1: Linear systems with positive definite sparse matrixes
Two sparse, symmetric and postive definite matrices solvers  have been compared with Cholesky method in both Matlab and Octave on Windows and Linux.

### Project 2: Implementation of DCT2 and compression algorithm
The projects has two parts:
- part1: implementation of DCT2
- part2: implementation of a compression algorithm analogue to JPEG


## How to run:
Project 1:

    All the codes are directly executable in Matlab and Octave.

Project 2:

    1. Download and install python at the following link:
        https://www.python.org/downloads/
        
    2. Move into: 
        .\mcs_projects\proj2\python
        
    3. Create a Virtual Environment: 
        python -m venv venv_mcs
        
    4. Activate the virtual environment:
         .\venv_mcs\scripts\activate
        
        N.B.: on Windows the folder is called scripts, meanwhile one Linux it is called bin
        
    5. Install requirements:
        pip install -r requirements.txt
    
    6. Run the files:
    
        - parte 1: python .\part1\src\main.py
        
        - parte 2: python .\part2\src\main.py
        
        
        
            