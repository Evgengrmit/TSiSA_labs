cmake_minimum_required(VERSION 3.17)
project(TSISA)

set(CMAKE_CXX_STANDARD 14)

add_executable(TSISA
        ${CMAKE_CURRENT_SOURCE_DIR}/sources/main.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/sources/OptimalPassiveSearchResult.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/sources/DichotomySearchResult.cpp
        )
target_include_directories(TSISA PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)