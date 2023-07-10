cmake_minimum_required(VERSION 3.8)
project(integration)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake_auto REQUIRED)

if(BUILD_TESTING)
  ament_auto_find_test_dependencies()
  find_package(ament_cmake_pytest)

  ament_add_pytest_test(pytest
    test
  )

endif()

ament_auto_package(
  INSTALL_TO_SHARE launch
)
