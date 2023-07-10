cmake_minimum_required(VERSION 3.8)
project(example_ament_cmake_test)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

if(BUILD_TESTING)

  # shell test with bats
  ament_add_test(test_bats
    COMMAND bats test.bats
    WORKING_DIRECTORY $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/test>
    GENERATE_RESULT_FOR_RETURN_CODE_ZERO
  )
  ament_add_test_label(test_bats bats)

endif()

ament_package()
