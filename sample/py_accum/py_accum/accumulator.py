# Copyright (c) 2023 Fixstars inc.
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.


class Accumulator:
    def __init__(self):
        self._data = 0

    def add(self, v):
        self._data += v

    def get(self):
        return self._data
