cmake_minimum_required(VERSION 3.8)
project(example_launch_testing_ament_cmake)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

ament_auto_add_executable(twice src/twice.cpp)

if(BUILD_TESTING)
  find_package(launch_testing_ament_cmake REQUIRED)
  find_package(ament_cmake_ros REQUIRED)

  add_launch_test(test/test_twice_launch.py
    RUNNER "${ament_cmake_ros_DIR}/run_test_isolated.py"
  )
endif()

ament_auto_package(
  INSTALL_TO_SHARE launch
)
