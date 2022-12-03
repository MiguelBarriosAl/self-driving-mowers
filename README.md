# Self Driving Mowers

Application that helps in controlling new mowers that are able to cut the grass and to inspect the terrain with their cameras to identify problems in the green areas.


# Installation and Run
- Install python==3.10.7

        sudo apt update

        sudo apt install python3.9.7

        python --version

- Clone the repository

        git clone https://github.com/MiguelBarriosAl/self-driving-mowers.git

- Install virtual enviroment: 

        sudo apt-get install python3-pip

        sudo pip3 install virtualenv

        virtualenv venv

        source venv/bin/activate

- Install requirements

        pip install -r requirements.txt

- Local Running (no production environment)

    `cd \api_v1`

    `uvicorn main:app --reload`

# Services


## HealthCheck

`curl --location --request GET 'http://127.0.0.1:8000/'`

## /Mower
For the following requests it is mandatory to include in the first request the field "top".
Subsequently, for those that are in the same plane, it is not necessary to include it.

### Request

    curl --location --request POST 'http://127.0.0.1:8000/mower/' \
    --header 'Content-Type: application/json' \
    --data-raw '{"top": [5,5],
    "position": [1,2,"N"],
    "instructions": "LMLMLMLMM"
    }

### Output
`[1, 3,"N"]`

### Request

    curl --location --request POST 'http://127.0.0.1:8000/mower/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    "position": [3,3,"E"],
    "instructions": "MMRMMRMRRM"
    }'

#### Output
`[5,1,"E"]`