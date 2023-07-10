// Copyright (c) 2023 Fixstars inc.
//
// Use of this source code is governed by an MIT-style
// license that can be found in the LICENSE file or at
// https://opensource.org/licenses/MIT.
#include <cpp_calc/twice.hpp>
#include <gtest/gtest.h>


TEST(do_twice, two_sohuld_be_four) {
  ASSERT_EQ(cpp_calc::do_twice(2), 4);
}
