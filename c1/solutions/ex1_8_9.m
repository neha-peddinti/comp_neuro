load('c1p8.mat')

% trial duration
T = 20*60;   % 20 mins
r = 500; % Hz
dt = .002;   % interval between sample times

% Exercise 8: find spike-triggered average
% from 0 to 300 ms (150 time steps)

t = dt:dt:T;
sta = [];

% rho is 1 if spike, 0 if no spike
% for every rho value, if spike, find sta value
% only find sta function for t = 0 to 300 ms
for tau = 1: 150
    av = 0;
    spikes = 0;
    for i = 1:(T/dt)
        if rho(i) ==  1
            spikes = spikes + 1;
            if i-tau > 0
                av = av + stim(i-tau);
            end
        end
    end
    av = av / spikes;
    sta = [sta, av];
end

% reverse direction of sta to be conventional
plot(2*(1:150), sta)
xlabel('\tau (ms) before spike')
ylabel('stimulus value')
set(gca, 'XDir', 'reverse')


% Exercise 9: Compare two-spike-triggered-averages
% with the sum of two single-STAs

abs_diff = []

for i = 1:50 % interval = 2 to 100 ms
    % indices of events with 2 spikes with interval 2*i ms
    events = find(conv(rho,[1,zeros(1, i-1),1])==2);
    
    % get two-spike-triggered-average for interval 2*i
    % calculate 2-STA for tau in [0, 300] ms
    sta2 = [];
    spikes = length(events);
    for tau = 1:150
        av = 0;
        for j = 1:length(events)
            if events(j)-tau > 0
                av = av + stim(events(j)-tau);
            end
        end
        av = av / spikes;
        sta2 = [sta2, av];
    end
    
    % get sum of 2 single-STAS separated by 2*i ms
    ssta1 = sta;
    ssta2 = circshift(sta, i);
    ssta2(1:i)=0;
    % ssta2 = circshift(sta, -1*i);
    % ssta2(end-i:end)=0
    ssta = ssta1+ssta2;
    
    % get difference
    diff = sta2 - ssta;
    length(diff)
    abs_diff(end+1) = norm(diff)
end

plot(2*(1:50), abs_diff)
xlabel('interval of \tau (ms) between spikes')
ylabel('magnitude of (2-STA - sum of single STAs separated by \tau)')
%set(gca, 'XDir', 'reverse')

