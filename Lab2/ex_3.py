#!/usr/bin/env python3
import collections
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3
print(sorted(data, key=lambda v: -v if v < 0 else v))
