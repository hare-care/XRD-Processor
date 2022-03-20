function [mismatch, suba, SLa, thickness] = xrd_calc(sl1n, sl0, sub, sl1p, lambda, n, h, k, l)
% calculate mismatch, lattice constants, and thickness. Requires theta
% values for SL-0, Substrate, SL-1, SL+1 peaks. 
% Lambda, n, h, k, l have standard values of 1.54, 1, 0, 0, 4. Can be changed
% by inputting them in the order above. 

% setting up standard arguments
theta = sl0;
if nargin < 5
    lambda = 1.54; 
    n = 1;
    h = 0;
    k = 0;
    l = 4;
end


% calc for D of the SL
dSL = (n*lambda)/(2*sind(theta));

% calc for a of the SL using D
SLa = dSL*(sqrt(h^2+k^2+l^2));

% same thing as above but for the substrate
theta = sub;
dsuba = (n*lambda)/(2*sind(theta));
suba = dsuba*(sqrt(h^2+k^2+l^2));

% Calc for mismatch using the values found above
mismatch = abs((suba-SLa)/suba);


% thickness is found by using one of the n=1 peaks. Here I just chose n=+1,
% but n=-1 shoudl be equivalent
thickness = abs(-lambda/(2*(sind(sl1p)-sind(sl0))));

% print out useful values for easy access
fprintf('mismatch = %f\nSubstrate constant = %f\nSubstrate D = %f\nSL constant = %f\nSL D = %f\nSL thickness %f', mismatch,  suba, dsuba, SLa, dSL, thickness);






