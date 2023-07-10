cmake_minimum_required(VERSION 3.8)
project(example_ament_cmake_gmock)

find_package(ament_cmake REQUIRED)

add_library(mylib SHARED
  src/foo.cpp
)

target_include_directories(mylib
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

install(TARGETS
  mylib
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

if(BUILD_TESTING)
  find_package(ament_cmake_gmock REQUIRED)

  ament_add_gmock(my_ament_cmake_gmock
    test/foo_mock.cpp
  )
  target_link_libraries(my_ament_cmake_gmock
    mylib
  )

endif()

ament_package()
