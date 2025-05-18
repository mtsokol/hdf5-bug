import juliapkg
import juliacall as jc  # noqa

juliapkg.resolve()

from juliacall import Main as jl  # noqa

jl.seval("using HDF5")
