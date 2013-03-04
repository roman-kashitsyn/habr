#include "gtest/gtest.h"
#include "miniregex.hpp"

using namespace miniregex;

TEST(MiniRegexTest, simple_test)
{
    ASSERT_TRUE(match("a*b", "aaabb"));
    ASSERT_TRUE(match("Hel*o", "Helllllllo"));
}
