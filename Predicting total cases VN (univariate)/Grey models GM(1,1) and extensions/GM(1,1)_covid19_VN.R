data <- read.csv('../assets/Total_cases.csv', sep=",")
covid19_VN <- (dplyr::pull(data, Case))
covid19_VN_hat_0 <- NULL
covid19_VN_hat_1 <- NULL
covid19_VN_predict_0 <- NULL
covid19_VN_predict_1 <- NULL

covid19_VN_0 <- covid19_VN[1:21]
m <- length(covid19_VN_0)
AGO <- cumsum(covid19_VN_0)
B <- matrix(nrow = m - 1, ncol = 2)
Y <- covid19_VN_0[-1]

for (i in 1:(m - 1)) {
  B[i, 1] <- -1/2 * (AGO[i] + AGO[i+1])
  B[i, 2] <- 1
}
a <- (solve(t(B) %*% B) %*% t(B) %*% Y)[1,1] 
b <- (solve(t(B) %*% B) %*% t(B) %*% Y)[2,1]
for (k in 1: length(covid19_VN)) {
  covid19_VN_hat_1[k] = (covid19_VN_0[1] - b/a) * exp(-a* (k - 1)) + b/a 
}

covid19_VN_hat_0 <- diff(covid19_VN_hat_1)
covid19_VN_hat_0 <- append(covid19_VN_hat_0, covid19_VN[1], after = 0)

RPE <- (covid19_VN_hat_0 - covid19_VN) / covid19_VN * 100
ARPE <- sum(abs(RPE)) / length(covid19_VN)

print(covid19_VN_hat_0)
print(RPE)
print(ARPE)

for (k in 1: (length(covid19_VN) + 14)) {
  covid19_VN_predict_1[k] = (covid19_VN_0[1] - b/a) * exp(-a* (k - 1)) + b/a 
}

covid19_VN_predict_0 <- diff(covid19_VN_predict_1)
covid19_VN_predict_0 <- append(covid19_VN_predict_0, covid19_VN[1], after = 0)

print(round(covid19_VN_predict_0), digits = 0)


