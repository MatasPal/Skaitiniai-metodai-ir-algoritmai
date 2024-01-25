import numpy as np


def f(x):
    """
    Function given by task
    :param x: x value
    :return: y value
    """
    return (np.log(x) / (np.sin(2 * x) + 1.5)) - (x / 7)


def chebyshev_range(count, start, end):
    """
    Calculates x range values using chebyshev polynomial formula
    :param count: Points count
    :param start: x range start
    :param end: x range end
    :return: Calculated x values array
    """
    range_x = []
    for i in range(count):
        temp = (end + start) / 2 + (end - start) / 2 * np.cos((2 * i + 1) * np.pi / (2 * count))
        range_x.append(temp)

    return range_x


def newton_interpolation_coefficients(range_x, range_y):
    """
    Calculates coefficients for newton's interpolation formula
    :param range_x: All x values
    :param range_y: All y values
    :return: Calculated coefficients
    """
    a = [range_y]
    for i in range(len(range_x)):
        a.append([])
        for j in range(1, len(range_x) - i):
            a[i + 1].append((a[i][j] - a[i][j - 1]) / (
                    range_x[np.min([i + j, len(range_x) - 1])] - range_x[np.max([i + j - (i + 1), 0])]))

    return [_a[0] for _a in a[:-1]]


def newton_interpolation_f(range_x, range_y):
    """
    Makes interpolation function
    :param range_x: all x values
    :param range_y: all y values
    :return: Interpolation function
    """
    a_coefficients = newton_interpolation_coefficients(range_x, range_y)

    def interpolation_f(_x):
        """
        Calculates y value from the newton's interpolation function
        :param _x: x value
        :return: y value
        """
        ff = a_coefficients[0]
        tmp = 1
        for ii in range(1, len(a_coefficients)):
            tmp *= (_x - range_x[ii - 1])
            ff += a_coefficients[ii] * tmp

        return ff

    return interpolation_f


def akima_points_derivative(range_x, range_y):
    """
    TODO: not working
    Calculates each point slope
    Source: https://en.wikipedia.org/wiki/Akima_spline
    :param range_x: x range values array
    :param range_y: y range values array
    :return: each point calculated slope values array
    """

    def m(index):
        """
        Slope of the line segment calculation (from wiki source)
        :param index: Point index
        :return: Calculated slope of the line segment
        """
        return (range_y[index + 1] - range_y[index]) / (range_x[index + 1] - range_x[index])

    range_s = []
    for i in range(2, len(range_x) - 2):
        range_s.append((np.abs(m(i + 1) - m(i)) * m(i - 1) + np.abs(m(i - 1) - m(i - 2)) * m(i)) / (
                np.abs(m(i + 1) - m(i)) + np.abs(m(i - 1) - m(i - 2))))

    return range_s


def U(start, end, x):
    """
    Calculates U value for hermite spline
    :param start: Interval start
    :param end: Interval end
    :param x: Current x
    :return: Calculated U for given x
    """
    return (1 - 2 * (1 / (start - end)) * (x - start)) * ((x - end) / (start - end)) ** 2


def V(start, end, x):
    """
    Calculates V value for hermite spline
    :param start: Interval start
    :param end: Interval end
    :param x: Current x
    :return: Calculated V for given x
    """
    return (x - start) * ((x - end) / (start - end)) ** 2


def hermite_interpolation_spline(range_x, range_y):
    """
    Calculates hermite interpolation spline function
    :param range_x: All x values
    :param range_y: All y values
    :return: Hermite interpolation spline function
    """
    range_dy = points_slopes(range_x, range_y)

    def spline_function(x):
        index = np.searchsorted(range_x, x)
        try:
            result = U(range_x[index - 1], range_x[index], x) * range_y[index - 1] + V(range_x[index - 1],
                                                                                       range_x[index],
                                                                                       x) * range_dy[index - 1] \
                     + U(range_x[index], range_x[index - 1], x) * range_y[index] \
                     + V(range_x[index], range_x[index - 1], x) * range_dy[index]
        except TypeError:
            # Handles None data from given country's data
            return None
        return result

    return spline_function


def slope(x1, y1, x2, y2):
    """
    Gets given interval slope
    :param x1: Interval start x
    :param y1: Interval start y
    :param x2: Interval end x
    :param y2: Interval end y
    :return: Calculated slope
    """

    return (y2 - y1) / (x2 - x1)


def points_slopes(range_x, range_y):
    """
    Calculates slopes for each interval between given points
    :param range_x: x values
    :param range_y: y values
    :return: Slopes array
    """

    slopes = []
    for i in range(len(range_x) - 1):
        if range_x[i] is None or range_x[i + 1] is None or range_y[i] is None or range_y[i + 1] is None:
            slopes.append(None)
        else:
            slopes.append(slope(range_x[i], range_y[i], range_x[i + 1], range_y[i + 1]))

    slopes.append(slopes[-1])
    return slopes


def parametric_interpolation(fx, fy, range_t):
    """
    Combines fx and fx to result in parametric function
    :param fx: FX
    :param fy: FY
    :param range_t: time range
    :return: x values array, y values array
    """
    x_results = []
    y_results = []
    for t in range_t:
        x_results.append(fx(t))
        y_results.append(fy(t))

    return x_results, y_results
