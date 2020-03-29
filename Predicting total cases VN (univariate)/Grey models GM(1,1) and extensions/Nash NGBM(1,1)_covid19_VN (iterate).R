data <- read.csv('../assets/Total_cases.csv', sep=",")
covid19_VN <- (dplyr::pull(data, Case))
covid19_VN_hat_1 <- NULL
covid19_VN_hat_0 <- NULL
covid19_VN_predict_0 <- NULL
covid19_VN_predict_1 <- NULL

covid19_VN_0 <- covid19_VN[1:21]
m <- length(covid19_VN_0)
AGO <- cumsum(covid19_VN_0)
B <- matrix(nrow = m-1, ncol = 2)
Y <- covid19_VN_0[-1]

range_n <- seq(-1, 0.99, 0.005)
range_P <- seq(0, 1, 0.005)

matri_err <- matrix(nrow = length(range_n), ncol = length(range_P))

for (i in 1:length(range_n)) {
  for (j in 1:length(range_P)) {
    for (k in 1:(m - 1)) {
      B[k, 1] = -( range_P[j] * AGO[k] + (1 - range_P[j]) * AGO[k+1])
      B[k, 2] = ( range_P[j] * AGO[k] + (1 - range_P[j]) * AGO[k+1]) ^ (range_n[i])
    }
    a <- (solve(t(B) %*% B) %*% t(B) %*% Y)[1,1] 
    b <- (solve(t(B) %*% B) %*% t(B) %*% Y)[2,1] 
    covid19_VN_hat_1 <- NULL
    for (l in 1:m) {
      covid19_VN_hat_1[l] = ((covid19_VN[1]^(1 - range_n[i]) - b/a) * exp(-a * (1 - range_n[i]) * (l - 1)) + b/a) ^ (1/(1 - range_n[i]))
    }
    err <- sum(abs(diff(covid19_VN_hat_1) - covid19_VN_0[-1])/covid19_VN_0[-1])
    matri_err[i, j] <- err
  }
}

matri_err[is.na(matri_err)] <- max(matri_err, na.rm = TRUE)
dimo <- which(matri_err == min(matri_err), arr.ind=TRUE)

n_optimal = range_n[dimo[1]]
P_optimal = range_P[dimo[2]]

for (i in 1:(m - 1)) {
  B[i, 1] <- -( P_optimal * AGO[i] + (1 - P_optimal) * AGO[i+1])
  B[i, 2] <- ( P_optimal * AGO[i] + (1 - P_optimal) * AGO[i+1]) ^ n_optimal
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



