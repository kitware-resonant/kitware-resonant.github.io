# girder-4

Girder 4 documentation materials.

## Build instructions

You can use `poetry` to build and view the documentation locally. There are two
ways to do it.


### Static build

1. Run `poetry install` to build the dependencies.
2. Run `poetry run task build` to build the documentation.
3. Run `poetry run task serve` to serve the docs on port 8000 (or `poetry run
   task serve 8001` to use a different port of your choice).

### Watch mode build.

1. Run `poetry install` to build the dependencies.
2. Run `poetry run task watch` to build and serve the docs on port 8000 (or
   `poetry run task watch PORT=8001` to use a different port of your choice).
   Changes to the documentation source code will cause an automatic rebuild.
