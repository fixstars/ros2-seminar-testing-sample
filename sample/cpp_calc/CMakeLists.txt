cmake_minimum_required(VERSION 3.8)
project(cpp_calc)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

ament_auto_add_library(twice_lib
  SHARED
  src/twice.cpp
  src/twice_node.cpp
)

ament_auto_add_executable(twice
  src/main.cpp
)

if(BUILD_TESTING)
  ament_auto_find_test_dependencies()

  ament_auto_add_gtest(twice_test
    test/unittest/twice_test.cpp
  )

  add_launch_test(test/launch/twice_node_test.py
    RUNNER "${ament_cmake_ros_DIR}/run_test_isolated.py"
  )
endif()

ament_auto_package()
