cmake_minimum_required(VERSION 2.8)
project(ecto_talk)

find_package(ecto REQUIRED)

add_subdirectory(src)
ecto_python_env_gen("")



