function memoryPlotter(matrixName)
% MEMORYPLOTTER plots a graph of the memory variations in the time.
%   MEMORYPLOTTER(M) reads with memoryReadDelta the memory variations 
%   related to the decomposition and resolution of M in all the
%   windows/linux-octave/matlab combinations; reports files must be in the
%   folder '../reports/', their names have to follow the pattern 
%   'M_[windows,linux]_[octave,matlab]_sym.txt' and they
%   have to contain only numeric values.
%   
%   See also MEMORYREADDELTA

    windowsMat = memoryReadDelta("..\reports\" + matrixName + "_windows_matlab_sym.txt");
    windowsOct = memoryReadDelta("..\reports\" + matrixName + "_windows_octave_sym.txt");
    linuxMat = memoryReadDelta("..\reports\" + matrixName + "_linux_matlab_sym.txt");
    linuxOct = memoryReadDelta("..\reports\" + matrixName + "_linux_octave_sym.txt");
    clf
    hold on;
    plot(windowsMat);
    plot(windowsOct);
    plot(linuxMat);
    plot(linuxOct);
    legend("windows-matlab", "windows-octave", "linux-matlab", "linux-octave");
    hold off;
end

