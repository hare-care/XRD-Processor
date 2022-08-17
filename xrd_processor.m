function [ascii, fullchar, datavector, angles, locs] = xrd_processor(file_name)

% notes on the file format
% fullchar(441) is the last ascii before the data (new line ascii, 10) it seems
% end of the file is ascii value 26, called substitute
% the info befor ethe data seems to follow the same format, ive tried it on
% 4 different scans. so the placement of key information should be the same
% first angle: 344
% range: 365
% width: 385
% hkl: 148
% wavelength: 165



fileID = fopen(file_name);
ascii = fread(fileID);
fclose(fileID);
fullchar = [];


first = ascii_converter(344, ascii);
range = ascii_converter(365, ascii);
width = ascii_converter(385, ascii);
wavelength = ascii_converter(165, ascii);

%creating x-axis
% offset it by 1 setpwidth in order to match with previous data
angles = (first+width):width:(first+width+range);



for i = 1:length(ascii)
     fullchar = [fullchar char(ascii(i))];
end

sample_number = fullchar(52:55);
 
k = 441;
datavector = [];

% start at 441, first value. 26 is last character of file, so end there
while ascii(k) ~= 26
%     value = 0; % reset value
    index = k; % hold place in data set
    
    value = ascii_converter(index, ascii);
    % store into vector
    datavector = [datavector value];
    
    % go onto next data point
    % works with last data point too because it ends with ascii 10 then
    % ascii 26, which is when the big loop ends. 
    while ascii(k) ~= 10
        % look for ascii 10 which is the last character before a number
        % value. add to k until we find that. 
        k = k+1;
    end
    k = k+1; % want k to be index of first value of next data point. so we move 1 past ascii 10
    
end


[peaks, locs] = findpeaks(datavector, angles, 'MinPeakProminence', 5000);
figure;
%semilogy(angles, datavector, locs, peaks, 'o');

% start in middle
% check to the left
% check peak to the right
% should be different
% check peak to the 2nd right
% check peak to the 2nd left
% if 2nd left distance = right distance then this is SL peak
% if 2nd right distance = left distance then this is SL peak

k = ceil(length(locs)/2);
SL_guess = locs(k);
right_guess = locs(k+1);
left_guess = locs(k-1);
right_distance = abs(SL_guess - right_guess);
left_distance = abs(SL_guess - left_guess);

% work with 1% error bc distances cant be the same
if (k+2) <= length(locs)
    sec_right_guess = locs(k+2);
    sec_right_distance = abs(SL_guess - sec_right_guess);
    if error_calc(sec_right_distance, left_distance) <= 0.5
        SL_loc = SL_guess;
        SLn1_loc = left_guess;
        Sub_loc = right_guess;
        SLp1_loc = sec_right_guess;
        SL_peakn1 = peaks(k-1);
        SL_peakp1 = peaks(k+2);
        Sub_peak = peaks(k+1);
    end
end
if (k-2) >= 1
    sec_left_guess = locs(k-2);
    sec_left_distance = abs(SL_guess - sec_left_guess);
    if error_calc(sec_left_distance, right_distance) <= 0.5
        SL_loc = SL_guess;
        SLn1_loc = sec_left_guess;
        Sub_loc = left_guess;
        SLp1_loc = right_guess;
        SL_peakn1 = peaks(k-2);
        SL_peakp1 = peaks(k+1);
        Sub_peak = peaks(k-1);
    end
end

SL_peak = peaks(k);
four_peaks_locs = [SLn1_loc, SL_loc, Sub_loc, SLp1_loc];
four_peaks_height = [SL_peakn1, SL_peak, Sub_peak, SL_peakp1];

semilogy(angles, datavector, SL_loc, SL_peak, 'ko', SLn1_loc, SL_peakn1, 'ko', Sub_loc, Sub_peak, 'ko', SLp1_loc,SL_peakp1, 'ko');
xrd_calc(SLn1_loc, SL_loc, Sub_loc, SLp1_loc, wavelength);



save ('xrd_data.mat', 'angles', 'datavector', 'four_peaks_locs', 'four_peaks_height', 'sample_number');

end









function [error] = error_calc(num1, num2)
    diff = abs(num1 - num2);
    avg = (num1 + num2)/2;
    error = diff/avg;
end

function [ret_num] = ascii_converter(original, ascii)
% converts ascii to real numbers. only works if there is a decimal point
% has to start at first value

    index = original;
    value = 0;
    % check for first digit
    % if number, skip past it
    % continue until decimal point
    while ascii(index) ~= 46
       index = index +1;
    end
    % record decimal point index
    dec_index = index;
    % could check for decimal values, but the data doesnt seem to ever
    % contain decimals 
        
    % move to first number before the decimal
    index = index -1;
    
    % do for each number in front of decimal
    while index >= original
        % convert ascii into actual number
        number = ascii(index) - 48;
        % multiply number by 10^(x-1) where x is difference between current
        % marker and decimal point marker 
        number = number * 10^(dec_index -index -1);
        % add them together
        value = value + number;
        % move back to front
        index = index -1;
    end
    
    % do for each number after decimal point
    index = dec_index;
    index = index+1;
    while (((ascii(index))>= 48) && ((ascii(index)-48)<=57))
        number = ascii(index) -48;
        
        number = number *10^(dec_index - index);
        value = value +number;
        index = index +1; 
    end 
    
    ret_num = value;
end



