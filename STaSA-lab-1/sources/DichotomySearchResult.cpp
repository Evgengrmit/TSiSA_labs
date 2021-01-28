#include "DichotomySearchResult.hpp"

DichotomySearchResult::DichotomySearchResult(double ak, double bk, double x1,
                                             double x2, double fAk, double fBk)
    : _ak(ak), _bk(bk), _x1(x1), _x2(x2), _f_ak(fAk), _f_bk(fBk) {}
bool DichotomySearchResult::IsValidInterval(double epsilon) const {
  return IntervalLength() > epsilon;
}
double DichotomySearchResult::CalculateMinimum() const {
  return (_ak + _bk) / 2.;
}
double DichotomySearchResult::GetDelta() const { return (_bk - _ak) / 2.; }
void DichotomySearchResult::LogHeader(std::ostream &logger) {
  logger << "__________________________________________________________________"
            "_____\n";
  logger << "|    ak   |    bk   |    lk   |    x1   |    x2   |  f(ak)  |  "
            "f(bk)  |\n";
}
void DichotomySearchResult::LogFooter(std::ostream &logger) {
  logger << "|_________|_________|_________|_________|_________|_________|_____"
            "____|"
         << std::endl;
}
void DichotomySearchResult::LogResult(std::ostream &logger,
                                      double epsilon) const {
  LogFooter(logger);
  logger << "|" << std::setw(9) << _ak;
  logger << "|" << std::setw(9) << _bk;
  logger << "|" << std::setw(9) << IntervalLength();
  logger << "|" << std::setw(9) << _x1;
  logger << "|" << std::setw(9) << _x2;

  if (IsValidInterval(epsilon)) {
    logger << "|" << std::setw(9) << _f_ak;
    logger << "|" << std::setw(9) << _f_bk;
  } else {
    logger << "|" << std::setw(19) << "b - a < epsilon";
  }

  logger << "|" << std::endl;
}
double DichotomySearchResult::IntervalLength() const { return _bk - _ak; }
