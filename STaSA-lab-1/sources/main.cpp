#include <iostream>

#include "DichotomySearchResult.hpp"
#include "OptimalPassiveSearchResult.hpp"

double func(const double &x) { return cos(x) * tanh(x); }
std::vector<OptimalPassiveSearchResult> PassiveSearch(double a, double b,
                                                      double epsilon) {
  if (a >= b) {
    throw std::runtime_error("Errorr!!! a > b");
  }
  std::vector<OptimalPassiveSearchResult> results;

  size_t N = 2 * (b - a) / epsilon;
  for (size_t i = 1; i < N; ++i) {
    double delta = (b - a) / (i + 1.);
    std::pair<double, double> min{a + delta, func(a + delta)};

    for (int k = 1; k <= i; ++k) {
      double xk = a + k * delta;
      double F_xk = func(xk);
      if (F_xk <= min.second) {
        min = {xk, F_xk};
      } else {
        break;
      }
    }
    results.emplace_back(i, min.first, min.second, delta);
  }

  return results;
}
std::vector<DichotomySearchResult>
DichotomySearch(double a, double b, double epsilon, double delta) {

  if (2 * delta >= epsilon)
    throw std::invalid_argument{"2*delta must be less than epsilon"};

  std::vector<DichotomySearchResult> results;

  while (true) {
    double x1 = (a + b) / 2. - delta;
    double x2 = (a + b) / 2. + delta;

    double f_ak = func(x1);
    double f_bk = func(x2);

    DichotomySearchResult result{a, b, x1, x2, f_ak, f_bk};
    results.push_back(result);

    if (!result.IsValidInterval(epsilon)) {
      return results;
    }

    if (f_ak < f_bk) {
      b = x2;
    } else {
      a = x1;
    }
  }
};

int main() {
  const double epsilon = 0.1;
  auto results = PassiveSearch(-2, 0, epsilon);

  OptimalPassiveSearchResult::LogHeader(std::cout);
  for (const auto &result : results) {
    result.LogResult(std::cout);
  }
  OptimalPassiveSearchResult::LogFooter(std::cout);
  auto dResults = DichotomySearch(-2, 0, 0.1, 0.001);

  DichotomySearchResult::LogHeader(std::cout);
  for (const auto &result : dResults) {
    result.LogResult(std::cout, epsilon);
  }
  DichotomySearchResult::LogFooter(std::cout);
  std::cout << "Minimum : " << func(dResults.back().CalculateMinimum()) << " ± "
            << dResults.back().GetDelta();

  return 0;
}