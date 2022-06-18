#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char *argv[]) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(0);
  int64_t N, Q;
  std::cin >> N;
  std::cin >> Q;
  std::vector<int64_t> A;
  A.reserve(N);
  for (int i = 0; i < N; i++) {
    int64_t at;
    std::cin >> at;
    A.emplace_back(at);
  }
  for (int i = 0; i < Q; i++) {
    int64_t target;
    std::cin >> target;
    int64_t operations = 0;
    for (int64_t source : A) {
      operations += std::abs(target - source);
    }
    std::cout << operations << "\n";
  }
  return 0;
}