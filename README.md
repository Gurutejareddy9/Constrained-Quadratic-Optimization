# Constrained Quadratic Optimization
 Constrained Quadratic Optimization using the Sequential Least Squares Programming (SLSQP) method

Description:
The code minimizes a simple quadratic objective function, \( f(x) = x_1^2 + x_2^2 \), subject to a set of linear inequality constraints:
1. \( x_1 + x_2 \geq 1 \)
2. \( x_1 \geq 0 \)
3. \( x_2 \geq 0 \)

The SLSQP method is well-suited for problems with both equality and inequality constraints. Here, `scipy.optimize.minimize` is used to find the values of \( x_1 \) and \( x_2 \) that minimize \( f(x) \) while satisfying all constraints.
