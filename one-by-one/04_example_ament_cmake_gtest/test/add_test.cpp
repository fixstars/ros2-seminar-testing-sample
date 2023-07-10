#include <example_ament_cmake_gtest/add.hpp>
#include <gtest/gtest.h>

TEST(add, success) { ASSERT_EQ(add(1, 2), 3); }

// TEST(add, failure) { ASSERT_EQ(add(1, 2), 4); }
