import numpy as np
from scipy.optimize import curve_fit

def curve_fit2d(func1d, x, y, z, lp0, gp0, sigma=None, absolute_sigma=False):

    if callable(lp0):
        lp0 = lp0(z)

    ny, nl = len(y), len(lp0)
    Yi, X = np.meshgrid(np.arange(ny), x)
    X_Yi = np.vstack((X.flatten(), Yi.flatten()))

    if sigma is not None:
        sigma = sigma.flatten()

    def func2d(x_yi, *p):
        x, yi = x_yi[0], x_yi[1].astype(int)
        lp, gp = np.array(p[:ny*nl]).reshape(nl, ny), np.array(p[ny*nl:])
        return func1d(x, y[yi], *lp[:,yi], *gp)

    popt,cov = curve_fit(func2d, X_Yi, z.flatten(),
                         p0=np.concatenate((lp0.flatten(), gp0)),
                         sigma=sigma, absolute_sigma=absolute_sigma)
    cov = np.sqrt(np.diag(cov))
    return (popt[:ny*nl].reshape(nl, ny), popt[ny*nl:],
            cov[:ny*nl].reshape(nl, ny), cov[ny*nl:],
            func2d(X_Yi, *popt).reshape(-1, ny))