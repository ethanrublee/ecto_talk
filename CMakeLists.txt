cmake_minimum_required(VERSION 2.8)
project(ecto_talk)
find_package(ecto REQUIRED)

ectomodule(ectotalk
  module.cpp
  )


add_subdirectory(latex)

