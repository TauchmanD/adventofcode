file = readlines("data.txt");
main(file);

function v = main(file)
    n = length(file)-1;
    m = length(file{1});
    trees = zeros(n,m);
    for line = 1:n
        row = file{line};
        row = strrep(row, newline,'');
        for i = 1:length(row)
            trees(line, i) = str2double(row(i));
        end
    end
    v = 0;
    for i = 2:n-1
        for j = 2:n-1
            row = trees(i, :);
            column = trees(:, j);
            t = trees(i,j);
            r = row(j+1:end);
            l = row(1:j-1);
            d = column(i+1:end);
            u = column(1:i-1);
            if any(t > max(r)) || any(t > max(u)) || any(t > max(d)) || any(t > max(l))
                v = v + 1;
            end
        end
    end
    v = v + length(trees) * 4 - 4;
    disp(v);
end
