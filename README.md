# Bench

This repository contains `bench`, PyVRP's benchmarking tool.

## Installation

`bench` requires Python 3.10 or higher. To install with `pip`, run

```bash
pip install git+https://github.com/PyVRP/Bench.git
```

## Usage

For an overview of commands, run `bench --help`.

```
usage: bench [-h] {solve,install,uninstall} ...

Bench: PyVRP's benchmarking tool.

options:
  -h, --help            show this help message and exit

subcommands:
  {solve,install,uninstall}
    solve               Solve one or more VRPLIB instances.
    install             Install PyVRP from Github.
    uninstall           Uninstall PyVRP.
```

### Solving instances

The main functionality of `bench` is to solve [VRPLIB](https://pyvrp.org/dev/supported_vrplib_fields.html) instances with PyVRP through its `solve` subcommand:

```bash
bench solve path/to/instances/*.vrp --seed 1 --max_runtime 60
```

List all available options with `bench solve --help`. Key options include:
- `--solutions`: Paths to existing solutions to compare against
- `--seed`: Random seed for reproducibility
- `--max_runtime`: Maximum solving time in seconds
- `--round_func`: Data rounding function
- `--num_procs`: Number of processes for solving multiple instances in parallel

### Managing PyVRP installations

You can also easily install specific versions of PyVRP through `bench`:

```bash
bench install # installs main
bench install --revision f57ff85
```

To uninstall PyVRP, run

```bash
bench uninstall
```
