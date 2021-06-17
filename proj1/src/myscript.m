mytable = readtable("../reports.csv");
oktable = mytable(strcmp(mytable.comment, "ok"),:);
symtable = oktable(strcmp(oktable.sym, "true"), :);
matlabtable = oktable(strcmp(oktable.sw, "matlab"), :);

clf;
close all;

% symamd true vs false

figure(1)
comparePlotter(matlabtable, "os", "windows", "sym", "true", "false");
title("symamd vs not symamd (matlab on windows)")
legend("symamd time", "symamd error", "symamd memory", ...
        "not symamd time", "not symamd error", "not symamd memory")
text(6e7, 1e-6, "\leftarrow from here cannot solve without symamd")
xline(6e7, "--")
i = input("[PRESS ENTER] Proceed with the single plots");

% single plotter
figure(2)
singlePlotter(symtable, "os", "windows", "sw", "matlab");

figure(3)
singlePlotter(symtable, "os", "windows", "sw", "octave");

figure(4)
singlePlotter(symtable, "os", "linux", "sw", "matlab");

figure(5)
singlePlotter(symtable, "os", "linux", "sw", "octave");

i = input("[PRESS ENTER] Proceed with the comparison plots");

% compare plotter

% windows matlab vs octave
figure(6);
comparePlotter(symtable, "os", "windows", "sw", "matlab", "octave");

% linux matlab vs octave
figure(7);
comparePlotter(symtable, "os", "linux", "sw", "matlab", "octave");

% matlab windows vs linux
figure(8);
comparePlotter(symtable, "sw", "matlab", "os", "windows", "linux");

% octave windows vs linux
figure(9);
comparePlotter(symtable, "sw", "octave", "os", "windows", "linux");


% we also plotted the memory history
% a = readtable('..\reports\apache2_circuit_win_octave_nosym.txt')
% plot(a.Var1)
