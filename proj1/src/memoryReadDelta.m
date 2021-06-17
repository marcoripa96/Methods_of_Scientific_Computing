function [memory] = memoryReadDelta(filename)
% MEMORYREADDELTA read the memory variation values from a '.txt' file.
% M = MEMORYREADDELTA(F) read from the file F a set of memory values and
% and returns them after subtracting the initial value
%
    memory = readtable(filename);
    memory = memory.Var1 - memory.Var1(1);
    memory(memory < 0) = 0;
    % memory = memory(memory>200000); % not nice
end