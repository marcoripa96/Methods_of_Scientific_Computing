function singlePlotter(table, filterField, filterValue, compareField, compareValue)
% SINGLEPLOTTER plots a graph with the matrix size on the X axis and error,
% time and memory on the Y axis.
%
% SINGLEPLOTTER(table, filterField, filterValue, compareField,
% compareValue) takes a table, filters it according to parameters (keeping 
% rows with values filterValue/compareValue for the columns 
% filterField/compareField) and plots a graph with the matrix size on 
% the X axis and error, time and memory on the Y axis in logaritmic scale
   

    filtered = table(strcmp(table2cell(table(:, filterField)), filterValue), :);
    filtered1 = filtered(strcmp(table2cell(filtered(:, compareField)), compareValue), :);
    hold on
    set(gca, 'YScale', 'log');
    plot(filtered1.size, filtered1.time, 'xg', ...
     filtered1.size, filtered1.err, 'xr', ...
     filtered1.size, filtered1.mem, 'xb', 'LineStyle', 'none');
    xlabel('Matrix size')
    title(filterValue + ": " +  compareValue)
    ylabel('Error, Time, PeakMemory')
    legend(compareValue + " time", compareValue + " error", compareValue + " memory")
    hold off
end