# Copyright (c) 2023 Fixstars inc.
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
from py_accum.accumulator import Accumulator


def test_success():
    acc = Accumulator()
    for i in range(10):
        acc.add(i)

    assert acc.get() == 45
