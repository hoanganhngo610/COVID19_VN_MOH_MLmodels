data <- read.csv('../assets/Total_cases.csv', sep=",")
covid19_VN <- (dplyr::pull(data, gdp))[-(1:19)] / 1000000000
covid19_VN_hat_1 <- NULL
covid19_VN_hat_0 <- NULL
cocid19_VN_predict_0 <- NULL
covid19_VN_predict_1 <- NULL

covid19_VN_0 <- covid19_VN[1:21] 
m <- length(covid19_VN_0)
AGO <- cumsum(covid19_VN_0)
B <- matrix(nrow = m-1, ncol = 2)

Y <- covid19_VN_0[-1]

range_n <- seq(-1, 0.999, 0.001)
range_ARPE <- NULL

for (i in 1:length(range_n)) {
  for (j in 1:(m - 1)) {
    B[j, 1] = -1/2 * (AGO[j] + AGO[j+1])
    B[j, 2] = (1/2 * (AGO[j] + AGO[j+1])) ^ (range_n[i])
  }
  a <- (solve(t(B) %*% B) %*% t(B) %*% Y)[1,1] 
  b <- (solve(t(B) %*% B) %*% t(B) %*% Y)[2,1]
  covid19_VN_hat_1 <- NULL
  for (k in 1:m) {
    covid19_VN_hat_1[k] = ((covid19_VN[1]^(1 - range_n[i]) - b/a) * exp(-a * (1 - range_n[i]) * (k - 1)) + b/a) ^ (1/(1 - range_n[i]))
  }
  covid19_VN_hat_0 <- diff(covid19_VN_hat_1, lag = 1, differences = 1)
  range_ARPE[i] = sum(abs((covid19_VN_hat_0 - Y) / Y)) * 100
}

n_optimal <- range_n[which.min(range_ARPE)]

for (i in 1:(m - 1)) {
  B[i, 1] <- -1/2 * (AGO[i] + AGO[i+1])
  B[i, 2] <- (1/2 * (AGO[i] + AGO[i+1])) ^ n_optimal
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

print(covid19_VN_hat_0)
print(n_optimal)
print(RPE)
print(ARPE)


for (k in 1: (length(covid19_VN) + 14)) {
  covid19_VN_predict_1[k] = ((covid19_VN[1]^(1 - n_optimal) - b/a) * exp(-a * (1 - n_optimal) * (k - 1)) + b/a) ^ (1/(1 - n_optimal))
}

covid19_VN_predict_0 <- diff(covid19_VN_predict_1)
covid19_VN_predict_0 <- append(covid19_VN_predict_0, covid19_VN[1], after = 0)

print(round(covid19_VN_predict_0), digits = 0)
