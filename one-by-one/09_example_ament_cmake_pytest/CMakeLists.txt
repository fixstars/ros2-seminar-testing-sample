cmake_minimum_required(VERSION 3.8)
project(example_ament_cmake_pytest)

find_package(ament_cmake REQUIRED)


if(BUILD_TESTING)
  find_package(ament_cmake_pytest)

  ament_add_pytest_test(example_pytest
    test
  )
  
endif()

ament_package()
