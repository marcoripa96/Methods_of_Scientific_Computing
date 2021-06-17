% matrix file path
matrixFileName = "../data/ex15.mat";
usesymamd = 1;
% file in which to save memory
demo_mem_name = "demo_mem.txt";

disp("Run this into shell");
fprintf("'..\\scripts\\mem_monitor.ps1 [MATLAB.exe|octave-gui.exe] [interval in seconds; e.g. 1] | out-file demo_mem.txt -encoding ascii'\n");

i = input("[PRESS ENTER] Proceed with matrix analysis");
disp("analyzing matrix...");

[err, time] = matrixAnalyzer(matrixFileName, usesymamd);

i = input("stop mem_monitor.ps1 then [PRESS ENTER] to visualize results");

meminfo = memoryReadDelta2(demo_mem_name);

max_mem = max(meminfo);

mymat = readMatrix(matrixFileName, usesymamd);
mat_size = whos("mymat").bytes;

disp("")
disp("----------------------------");
disp("results:");
disp("")
fprintf("error: %.10e\n", err);
fprintf("time: %f\n", time);
fprintf("max_memory: %.10e\n", max_mem);
fprintf("size: %.10e\n", mat_size);

plot(meminfo)

