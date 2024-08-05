function executableFolder = directoryGet()
%Gets the directory which the function is in.
%   it was created by mark golburg and shared on this
%   https://uk.mathworks.com/matlabcentral/answers/1741325-how-can-i-get-the-full-path-of-my-current-mlapp-file
%   forum post. 
		if isdeployed 
			% User is running an executable in standalone mode. 
			[~ , result] = system('set PATH');
			executableFolder = char(regexpi(result, 'Path=(.*?);', 'tokens', 'once'));
		else
			% User is running an m-file from the MATLAB integrated development environment (regular MATLAB).
            tmp_path = mfilename('fullpath');
            [executableFolder , ~ , ~] = fileparts(tmp_path);
		end 
end