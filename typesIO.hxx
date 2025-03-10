#include <functional>
#ifndef NETSIM_TYPES_HPP
#define NETSIM_TYPES_HPP
#include <cstdint>

using ElementID = int;
using Time = int;
using TimeOffset = int;
using ProbabilityGenerator = std::function<double()>;
