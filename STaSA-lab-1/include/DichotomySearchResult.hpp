#ifndef TSISA_DICHOTOMYSEARCHRESULT_HPP
#define TSISA_DICHOTOMYSEARCHRESULT_HPP

#include <iomanip>
#include <iostream>
#include <vector>

class DichotomySearchResult {
public:
  DichotomySearchResult(double ak, double bk, double x1, double x2, double fAk,
                        double fBk);
  bool IsValidInterval(double epsilon) const;
  double CalculateMinimum() const;
  double GetDelta() const;
  static void LogHeader(std::ostream &logger);
  static void LogFooter(std::ostream &logger);
  void LogResult(std::ostream &logger, double epsilon) const;

private:
  double _ak;
  double _bk;
  double _x1;
  double _x2;
  double _f_ak;
  double _f_bk;
  double IntervalLength() const;
};

#endif // TSISA_DICHOTOMYSEARCHRESULT_HPP
