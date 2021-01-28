#include "OptimalPassiveSearchResult.hpp"

OptimalPassiveSearchResult::OptimalPassiveSearchResult(size_t n, double x,
                                                       double fX, double delta)
    : N(n), _x(x), F_x(fX), delta(delta) {}

void OptimalPassiveSearchResult::LogHeader(std::ostream &logger) {
  logger << " ________________________________\n";
  logger << "| N |        xk       |    F(x)  |\n";
}
void OptimalPassiveSearchResult::LogFooter(std::ostream &logger) {
  logger << "|___|_________________|__________|\n";
}
void OptimalPassiveSearchResult::LogResult(std::ostream &logger) const {
  LogFooter(logger);
  logger << "|" << std::right << std::setw(3) << N;
  logger << "|" << std::setw(8) << _x << " ± " << std::left
         << std::setprecision(3) << std::setw(6) << delta;
  logger << "|" << std::right << std::setw(10) << std::setprecision(5) << F_x;
  logger << "|\n";
}
