# conan-libjson

[Conan.io](https://conan.io) package for libjson C/C++ library

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload libjson/7.6.1@sobotklp/stable --all

## Reuse the packages

### Basic setup

    $ conan install libjson/7.6.1@sobotklp/stable

### Project setup

If you handle multiple dependencies in your project, it would be better to add a *conanfile.txt*

    [requires]
    libjson/7.6.1@sobotklp/stable

    [generators]
    txt
    cmake


