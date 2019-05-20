% This source code is partly unchanged and token from course

function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)


% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));


% 算每一層的activiation, 包括加入bias 
a1 = [ones(m,1) X];
a2 = sigmoid(a1*Theta1');
a2 = [ones(m,1) a2];	
a3 = sigmoid(a2*Theta2');

% 建立output 層, 用repmat函數  http://bime-matlab.blogspot.com/2006/11/11211repmat.html
% 用 == 去建立一個只有對應到有數字才是1其他都是0的vector
y = repmat([1:num_labels], m, 1) == repmat(y, 1, num_labels);

% cost function
J = (-1 / m) * sum(sum(y.*log(a3) + (1 - y).*log(1 - a3)));

% 因為我們沒有要regualized 第一項
regTheta1 =  Theta1(:,2:end);
regTheta2 =  Theta2(:,2:end);

error = (lambda/(2*m)) * (sum(sum(regTheta1.^2)) + sum(sum(regTheta2.^2)));

% regularized cost function
J = J + error;

% init error vector
del1 = zeros(size(Theta1));
del2 = zeros(size(Theta2));

% loop over all training set, 5000
for t = 1:m,
	a1t = a1(t,:);
	a2t = a2(t,:);
	a3t = a3(t,:);
	yt = y(t,:);
	d3 = a3t - yt;  % delta for the output layer
	d2 = Theta2'*d3' .* sigmoidGradient([1;Theta1 * a1t']); % delta for the hidden layer l = 2
	del1 = del1 + d2(2:end)*a1t;   % Accumulate the gradient for theta1
	del2 = del2 + d3' * a2t;       % Accumulate the gradient for theta2
end;

% gradient for the neural network cost function, including the Regularized term
Theta1_grad = 1/m * del1 + (lambda/m)*[zeros(size(Theta1, 1), 1) regTheta1];
Theta2_grad = 1/m * del2 + (lambda/m)*[zeros(size(Theta2, 1), 1) regTheta2];

% Unroll gradients, 再由matrix 轉為 vector
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
