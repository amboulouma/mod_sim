function run()
    x0 = 4000;
    y0 = 1000;
    alpha = 1e-5;
    beta = 2e-5;
    gamma = 5e-9;
    delta = 5e-6;
    M = 20000;
    T = 120;

    function [x, y] = add_next_damped(x, y, alpha, beta, gamma, delta, M)
        xt = x(end);
        yt = y(end);
        xnext = xt + xt * alpha * (M - xt - yt) - xt * yt * beta;
        ynext = yt + yt * (delta * xt - gamma);
        x = [x, xnext];
        y = [y, ynext];
    end
        
    function [x,y] = damped(x0, y0, alpha, beta, gamma, delta, M, T)
        x = [x0];
        y = [y0];
        for t = 1:T
            [x, y] = add_next_damped(x, y, alpha, beta, gamma, delta, M);
        end
        x = floor(x);
        y = floor(y);
    end

    [x, y] = damped(x0, y0, alpha, beta, gamma, delta, M, T);
    disp('x')    
    x(end)
    disp('y')
    y(end)

    plot(0:T, x)
    hold on;
    ylim([0 inf])
    plot(0:T, y)
end
