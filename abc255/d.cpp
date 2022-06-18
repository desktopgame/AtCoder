// https://atcoder.jp/contests/abc255/tasks/abc255_d
#include <cstdint>
#include <inttypes.h>
#include <sstream>
#include <stdio.h>
#include <string>
#include <vector>

int main(int argc, char *argv[]) {
  int64_t N, Q;
  ::scanf("%" PRId64, &N);
  ::scanf("%" PRId64, &Q);
  std::vector<int64_t> A;
  A.reserve(N);
  for (int i = 0; i < N; i++) {
    int64_t at;
    ::scanf("%" PRId64, &at);
    A.emplace_back(at);
  }
  for (int i = 0; i < Q; i++) {
    int64_t target;
    ::scanf("%" PRId64, &target);
    int64_t operations = 0;
    for (int64_t source : A) {
      operations += std::abs(target - source);
    }
    ::printf("%" PRId64 "\n", operations);
  }
  return 0;
}