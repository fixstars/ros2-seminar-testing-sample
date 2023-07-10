#include <example_ament_cmake_gmock/foo.hpp>
#include <gmock/gmock.h>

class MockFoo : public Foo
{
public:
  MOCK_METHOD1(func, bool(int));
};

TEST(bar, success) {
  using namespace testing;
  MockFoo mock_foo;              // mock_fooの使われ方の想定は、
  EXPECT_CALL(mock_foo, func(0)) // 0を引数としてfuncが呼び出されること
  .Times(1)                      // 1度だけ呼ばれること
  .WillOnce(Return(true));       // funcはtrueを返す

  EXPECT_EQ(bar(&mock_foo), true); // funcの返り値はtrueであること
}

// TEST(bar, failure) {
//   using namespace testing;
//   MockFoo mock_foo;
//   EXPECT_CALL(mock_foo, func(0))
//   .Times(2)
//   .WillRepeatedly(Return(true));

//   EXPECT_EQ(bar(&mock_foo), true);
// }
