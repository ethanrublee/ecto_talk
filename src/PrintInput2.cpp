#include <ecto/ecto.hpp>

using namespace ecto;

struct PrintInput2
{
  static void declare_io(const tendrils& p, tendrils& i, tendrils& o) 
  {
    i.declare<std::string>("input");
  }
  void configure(const tendrils& p, const tendrils& i, const tendrils& o)
  {
    in = i["input"];
  }
  int process(const tendrils& i, const tendrils& o)
  {
    std::cout << "Rec'd:    " << *in << "\n";
    return OK;
  }
  spore<std::string> in;
};
ECTO_CELL(ectotalk, PrintInput2, "PrintInput2", "The input, it is printed");
