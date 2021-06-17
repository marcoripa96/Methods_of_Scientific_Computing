function [time, peakMem] = getStats(profile, functionName)
    time = 0;
    peakMem = 0;
    for i = 1:size(profile.FunctionTable)
        if profile.FunctionTable(i).FunctionName == functionName
            time = profile.FunctionTable(i).TotalTime;
            peakMem = profile.FunctionTable(i).PeakMem;
        end
    end

end