cmake_minimum_required(VERSION 3.8)
project(example_ament_ctest)

find_package(ament_cmake REQUIRED)

if(BUILD_TESTING)

  add_test(
    NAME test_success
    COMMAND bash -c "exit 0"
  )

  # add_test(
  #   NAME test_failure
  #   COMMAND bash -c "exit 1"
  # )

endif()

ament_package()
