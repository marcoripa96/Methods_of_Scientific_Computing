function [xApp] = solveWithCholesky(A, b)
% SOLVEWITHCHOLESKY solve a system of equation after the Cholesky
% decomposition
%   X = SOLVEWITHCHOLESKY(A, B) computes the Cholesky decomposition of the
%   matrix A, uses B to solve the system of linear equations with a
%   backward substitution and return in X the solution vector
%
% See also CHOL, MLDIVIDE
      R = chol(A);
      xApp = R\(R.'\b);
end