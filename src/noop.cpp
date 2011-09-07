#include <ecto/ecto.hpp>

using namespace ecto;

struct NoOp 
{
  int process(const tendrils& i, const tendrils& o)
  {
    std::cout << "process!\n";
    return OK;
  }
};

ECTO_CELL(ectotalk, NoOp, "NoOp", "The cell, it does nothing");
