function [A] = randomMForChol(n, density)
    A = sprand(n,n,density);
    A = A + A';
    A = sparse(A + eye(n)*n);
end