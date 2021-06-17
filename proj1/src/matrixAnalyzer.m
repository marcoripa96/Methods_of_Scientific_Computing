function [err, time] =  matrixAnalyzer(filename, usesymamd)  
% MATRIXANALYZER reads a matrix and solve the related system of linear
% equations.
% E = MATRIXANALYZER(F, FLAG) reads the matrix F, solve
% the related system of linear equations after a Cholesky decomposition and then
% returns the relative error; FLAG is used in readMatrix to specify if the
% matrix needs a permutation
%
% [E, T] = MATRIXANALYZER(___) returns also the time of the decomposition
% and resolution
%
% See also READMATRIX, RELERROR, SOLVEWITHCHOLESKY
    [A, x, b] = readMatrix(filename, usesymamd);
    pause(3)
    tic
        [xApp] = solveWithCholesky(A, b);
    time = toc;
    err = relError(x, xApp);
end