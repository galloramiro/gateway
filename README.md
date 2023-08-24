# Gateway


## Index
- [Description](#description)
- [How tu run the project](#how-tu-run-the-project)
- [Documentation](/docs/gateway.md)

## Description
This project is an example on how to use a gateway class to interact with 3d party services.  
Here you would find:  
- Base class example using an async framework 
- Implementation of a custom class
- Contract testing for the service
- Documentation with theory around this topics

## How tu run the project
In order to build this project you would need to:
- Install [docker](https://docs.docker.com/engine/install/) on you machine
- Copy the `.env.template` into a `.env` and fill the env variables
- Run the following commands
```shell
make build
make debug
```