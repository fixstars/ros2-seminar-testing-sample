cmake_minimum_required(VERSION 3.8)
project(example_ament_cmake_gtest)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

add_library(myadd SHARED
  src/add.cpp
)

target_include_directories(myadd
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

install(TARGETS myadd
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

if(BUILD_TESTING)
  find_package(ament_cmake_gtest REQUIRED)

  ament_add_gtest(myadd_gtest
    test/add_test.cpp
  )
  target_link_libraries(myadd_gtest
    myadd
  )
endif()

ament_package()
