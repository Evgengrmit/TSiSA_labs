#ifndef TSISA_OPTIMALPASSIVESEARCHRESULT_HPP
#define TSISA_OPTIMALPASSIVESEARCHRESULT_HPP

#include <cmath>
#include <exception>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

class OptimalPassiveSearchResult {
public:
  OptimalPassiveSearchResult(size_t n, double x, double fX, double delta);
  static void LogHeader(std::ostream &logger);
  static void LogFooter(std::ostream &logger);
  void LogResult(std::ostream &logger) const;

private:
  size_t N;
  double _x;
  double F_x;
  double delta;
};

#endif // TSISA_OPTIMALPASSIVESEARCHRESULT_HPP
