data <- read.csv('../assets/Total_cases.csv', sep=",")
covid19_VN <- (dplyr::pull(data,Case))/100
covid19_VN_hat_1 <- NULL
covid19_VN_hat_0 <- NULL
covid19_VN_predict_1 <- NULL
covid19_VN_predict_0 <- NULL

covid19_VN_0 <- covid19_VN[1:21] 
m <- length(covid19_VN_0)
AGO <- cumsum(covid19_VN_0)
B <- matrix(nrow = m-1, ncol = 2)

Y <- covid19_VN_0[-1]

# calculate the optimal value of P

q <- sum(AGO[-1]/AGO[-m])^(1/(m-1)) + m - 1
P_optimal <- 1/2 + 1/(2*q)

Z_1 <- matrix(nrow = 1, ncol = m)
gamma <- matrix(nrow = 1, ncol = m-1)

# calculate the optimal value of n

for (i in 2:length(Z_1)) {
  Z_1[i] <- (1 - P_optimal) * AGO[i] + P_optimal * AGO[i-1]
}
for(k in 2:length(gamma)) {
  nominator = (covid19_VN_0[k+1] - covid19_VN_0[k]) * Z_1[k+1] * Z_1[k] * covid19_VN_0[k] - (covid19_VN_0[k] - covid19_VN_0[k-1]) * Z_1[k+1] * Z_1[k] * covid19_VN_0[k+1]
  denominator = (covid19_VN_0[k+1])^2 * Z_1[k] * covid19_VN_0[k] - (covid19_VN_0[k])^2 * Z_1[k+1] * covid19_VN_0[k+1]
  gamma[k] = nominator / denominator
}

n_optimal = 1/(m-2) * sum(gamma[2:length(gamma)])

# apply optimal values of P an n to NGBM(1,1) algorithm

for (i in 1:(m - 1)) {
  B[i, 1] <- - (P_optimal * AGO[i] + (1 - P_optimal) * AGO[i+1])
  B[i, 2] <- (P_optimal * (AGO[i] + (1 - P_optimal) * AGO[i+1])) ^ n_optimal
}

a <- (solve(t(B) %*% B) %*% t(B) %*% Y)[1,1] 
b <- (solve(t(B) %*% B) %*% t(B) %*% Y)[2,1]
for (k in 1: length(covid19_VN)) {
  covid19_VN_hat_1[k] = ((covid19_VN[1]^(1 - n_optimal) - b/a) * exp(-a * (1 - n_optimal) * (k - 1)) + b/a) ^ (1/(1 - n_optimal))
}

covid19_VN_hat_0 <- diff(covid19_VN_hat_1)
covid19_VN_hat_0 <- append(covid19_VN_hat_0, covid19_VN[1], after = 0)

RPE <- (covid19_VN_hat_0 - covid19_VN) / covid19_VN * 100
ARPE <- sum(abs(RPE)) / length(covid19_VN)

print(n_optimal)
print(P_optimal)
print(covid19_VN_hat_0)
print(RPE)
print(ARPE)

for (k in 1: (length(covid19_VN) + 14)) {
  covid19_VN_predict_1[k] = ((covid19_VN[1]^(1 - n_optimal) - b/a) * exp(-a * (1 - n_optimal) * (k - 1)) + b/a) ^ (1/(1 - n_optimal))
}

covid19_VN_predict_0 <- diff(covid19_VN_predict_1)
covid19_VN_predict_0 <- append(covid19_VN_predict_0, covid19_VN[1], after = 0)

print(round(covid19_VN_predict_0))
