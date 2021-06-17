function [memory] = memoryReadDelta2(filename)
% MEMORYREADDELTA read the memory variation values from a '.txt' file.
% M = MEMORYREADDELTA(F) read from the file F a set of memory values and
% and returns them after subtracting the initial value
%
    memory = load(filename);
    memory = memory - memory(1);
    memory(memory < 0) = 0;
    % memory = memory(memory>200000); % not nice
end