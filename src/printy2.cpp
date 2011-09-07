#include <ecto/ecto.hpp>

using namespace ecto;

struct PrintInput
{
  static void declare_io(const tendrils& p, tendrils& i, tendrils& o) 
  {
    i.declare<std::string>("input");
  }

  int process(const tendrils& i, const tendrils& o)
  {
    std::cout << "Rec'd:" << i.get<std::string>("input") << "\n";
    return OK;
  }
};
ECTO_CELL(ectotalk, PrintInput, "PrintInput", "The input, it is printed");
