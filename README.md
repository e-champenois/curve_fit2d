# curve_fit2d
Wrapper around scipy.optimize.curve_fit for 2D fits with local and global parameters.

Fits a 2D data with a 2D parametrized function f_2D(x, y ;lp, gp).
The slice at y1 is fit using the local parameters lp1, the global parameters gp, and the function f_1D(x; y1, lp1, gp).
