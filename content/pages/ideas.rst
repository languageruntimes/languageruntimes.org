Ideas
#####

Here are some things that we think might be good topics to cover:

* Calling conventions
   * Function entry points
   * Multiple return values
* Numerical issues
   * Integer overflow
   * Division by zero
   * Floating point errors
   * Numerical towers
   * Accuracy vs performance
* Value Representation
   * Traditional tagging
   * Avoiding boxing / unboxing
   * NaN boxing
* Conditions / exceptions
   * Interaction with SEH on Windows
   * Cross-language integration
* Concurrency and Parallelism
   * Coroutines, green threading
   * Lots more ...
* Stack usage
   * Segmented stacks (like in Go, now in LLVM / GCC)
   * Red zone on x86-64 (Linux and Darwin, not Windows)
   * alloca vs VLA (scope vs lifetime)
* GC integration
   * Finalizers
   * Weak pointers
   * Boehm, MPS, rolling your own
   * Barriers
* Miscellaneous
   * Debug info generation
   * Tracing - dtrace, systemtap, ETW, FeatherTrace
   * Hot code swapping
   * Shared vs static code
   * Symbol visibility and versioning
* Security considerations
   * Non-executable stacks
   * Hash algorithms and attacks
   * Random seeding
* Shared libraries as plugins
   * ELF constructors / destructors
   * Issues with "top level user code"
   * Issues with running code before main() invoked
* gdb / lldb / Visual Studio debugger integration
   * Showing custom types
   * Writing plugins
* Performance analysis
   * Accurate timing
   * Perfcounters
   * CPU cache statistics
   * Profiling implementation methods
