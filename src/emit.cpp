#include <ecto/ecto.hpp>
#include <boost/format.hpp>
using namespace ecto;

struct Emit
{
  static void declare_params(tendrils& p) 
  {
    p.declare<std::string>("what", "what to print");
  }
  static void declare_io(const tendrils& p, tendrils& i, tendrils& o) 
  {
    o.declare<std::string>("output", "the emitted string");
  }
  void configure(const tendrils& p, const tendrils& i, const tendrils& o)
  {
    what = p.get<std::string>("what");
    j = 0;
  }
  int process(const tendrils& i, const tendrils& o)
  {
    std::string emitted = str(boost::format("Emittance %u: %s") % j % what);
    std::cout << emitted << "\n";
    o.get<std::string>("output") = emitted;
    ++j;
    return OK;
  }
  std::string what;
  unsigned j;
};
ECTO_CELL(ectotalk, Emit, "Emit", "The cell, it emits things");
