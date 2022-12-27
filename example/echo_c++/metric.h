#include <bvar/bvar.h>

namespace other_metric {
    bvar::Adder<int> time;
    bvar::Window<bvar::Adder<int> > time_minitue("metric", "time", &time, 60);
}