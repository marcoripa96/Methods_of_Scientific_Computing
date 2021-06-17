function [A, x, b] = readMatrix(filename, usesymamd)
% READMATRIX  read a matrix from a '.mat' file.
%   M = READMATRIX(F, FLAG) return the matrix read from F. If FLAG is set
%   to 0 the function returns the original matrix; if FLAG is set to 1 the
%   function returns the matrix permutation based on symamd.
%
%   [M, S] = ADDME(___) also returns the solution vector of ones.
%
%   [M, S, B] = ADDME(___) also returns the vector B=MS.

    A = load(filename).Problem.A;
    x = ones(size(A,1),1);
    if usesymamd == 1
        d = symamd(A);
        A = A(d,d);
    end
    b = A*x;
end