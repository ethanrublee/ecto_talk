#include <ecto/ecto.hpp>

using namespace ecto;

struct Printy
{
  static void declare_params(tendrils& p) 
  {
    p.declare<std::string>("what", "what to print");
  }
  void configure(const tendrils& p, const tendrils& i, const tendrils& o)
  {
    what = p.get<std::string>("what");
  }
  int process(const tendrils& i, const tendrils& o)
  {
    std::cout << what << "\n";
    return OK;
  }
  std::string what;
};
ECTO_CELL(ectotalk, Printy, "Printy", "The cell, it prints something");
