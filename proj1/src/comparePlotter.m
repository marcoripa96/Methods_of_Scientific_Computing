function comparePlotter(table, filterField, filterValue, compareField, compareValue1, compareValue2)
% COMPAREPLOTTER plots a comparison graph with the matrix size on the X axis and error,
% time and memory on the Y axis.
%
% COMPAREPLOTTER(table, filterField, filterValue, compareField, 
% compareValue1, compareValue2) takes a table, filters it according to 
% parameters (keeping rows with values filterValue/compareValue1-compareValue2 
% for the columns filterField/compareField) and plots a graph with the matrix size on 
% the X axis and error, time and memory on the Y axis in logaritmic scale
   
    filtered = table(strcmp(table2cell(table(:, filterField)), filterValue), :);
    filtered1 = filtered(strcmp(table2cell(filtered(:, compareField)), compareValue1), :);
    filtered2 = filtered(strcmp(table2cell(filtered(:, compareField)), compareValue2), :);
    hold on
    set(gca, 'YScale', 'log');
    plot(filtered1.size, filtered1.time, 'xg', ...
     filtered1.size, filtered1.err, 'xr', ...
     filtered1.size, filtered1.mem, 'xb', ...
     filtered2.size, filtered2.time, 'og', ...
     filtered2.size, filtered2.err, 'or', ...
     filtered2.size, filtered2.mem, 'ob', 'LineStyle', 'none');
    xlabel('Matrix size')
    title(filterValue + ": " +  compareValue1 + " vs " + compareValue2)
    ylabel('Error, Time, PeakMemory')
    legend(compareValue1 + " time", compareValue1 + " error", compareValue1 + " memory", ...
        compareValue2 + " time", compareValue2 + " error", compareValue2 +  " memory")
    hold off
end