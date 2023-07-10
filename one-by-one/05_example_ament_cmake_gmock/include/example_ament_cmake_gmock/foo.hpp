#pragma once

class Foo {
public:
  virtual bool func(int a) = 0;
};

bool bar(Foo *foo);
