# ROS2 Seminar - Testing Sample

[日本語README](./README_ja.md)

This repository contains sample code of items presented in the seminar [Autonomous driving realization by ROS2 test framework](https://speakerdeck.com/fixstars/autonomous-driving-realization-by-ros2-test-framework).

## Folders.

- [one-by-one](./one-by-one/) : Samples of each test framework. Corresponds to the tests in the seminar material "Available tests and lint".
- [lint](./lint/) : Samples of lint. Corresponds to the lints in the seminar material "Available tests and lint".
- [sample](./sample/) : Sample of package development including test implementation. Corresponds to "test implementation in a sample app" in the seminar material.

By default, all tests pass. Test cases that fail are commented out, so uncomment them if you want to check the behavior.

## Prerequisites

- ROS2 Humble (ros-humble-desktop)
- ros-humble-ament-cmake-google-benchmark
- ros-humble-launch-pytest
- bats (used in one of the samples)

## Setup

Assuming that ROS2 Humble is already set up, install the above additional packages and mixin. Mixin is used to run performance tests.

```shell
# Install additional packages
sudo apt install ros-humble-ament-cmake-google-benchmark ros-humble-launch-pytest bats

# Install mixin
colcon mixin add default https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml
colcon mixin update
```

Also, set the following environment variables to suppress `SetuptoolsDeprecationWarning` warnings, if necessary.

```shell
export PYTHONWARNINGS=ignore:::setuptools.command.install,ignore:::setuptools.command.easy_install
```

## Build

```shell
colcon build --symlink-install
```

## Test

```shell
# Add `--event-handers` option to print test results to stdout.
colcon test --event-handlers console_direct+ 
```

## Benchmark

Run performance tests. Although not explained in the seminar, performance tests using [Google Benchmark](https://github.com/google/benchmark) are also available and can be run using [one-by-one/06_example_ament_cmake_google_benchmark](./one-by-one/06_example_ament_cmake_google_benchmark/).

```shell
# Create another directory for release build
mkdir -p release

# Release build. `--mixin release` will set the necessary options.
# Set `-DAMENT_RUN_PERFORMANCE_TESTS=ON` to build performance test code.
colcon --log-base release/log build --build-base release/build --install-base release/intall --ament-cmake-args -DAMENT_RUN_PERFORMANCE_TESTS=ON --mixin release --symlink-install


# Run performance tests. Specify `--executor sequential` since parallel execution will affect the measurement.
colcon --log-base release/log test --build-base release/build --install-base release/intall --event-handlers console_direct+ --ctest-args ' -L performance --no-tests=ignore' --executor sequential
```


## License

This project is under MIT License.
