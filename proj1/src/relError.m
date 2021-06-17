function [err] = relError(xEs, xApp)
% RELERROR computes the relative error.
%   E = RELERROR(XE,XA) return the relative error given the exact solution 
%   XE and the approximated solution XA.
    err = norm(xEs - xApp)/norm(xEs);
end