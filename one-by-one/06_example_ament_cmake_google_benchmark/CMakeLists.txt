cmake_minimum_required(VERSION 3.8)
project(example_ament_cmake_google_benchmark)

find_package(ament_cmake REQUIRED)


if(BUILD_TESTING)
  find_package(ament_cmake_google_benchmark REQUIRED)
  #  --ament-cmake-args -DAMENT_RUN_PERFORMANCE_TESTS=ON が必要
  ament_add_google_benchmark(my_ament_cmake_google_benchmark
    benchmark/benchmark.cpp
  )

endif()

ament_package()
