#include "libjson.h"
using namespace std;

///////////////////////////////////////////
// In the test file
#include <gtest/gtest.h>

TEST(libjsonTest, Static) {
  EXPECT_EQ(json_is_valid("{}"), true);
  EXPECT_EQ(json_is_valid("{\"this\": \"is an object\"}"), true);
  EXPECT_EQ(json_is_valid("{INVALID_JSON"), false);
}
