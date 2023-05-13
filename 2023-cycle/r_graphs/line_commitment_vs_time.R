library("rjson")
library("ggplot2")

data <- fromJSON(file = "historical/result/result.json")

temp1 <- unlist(data[["2021"]])
temp2 <- unlist(data[["2022"]])
temp3 <- unlist(data[["2023"]])

df <- data.frame(years=2021:2023, num_commitments=c(length(temp1) / 2, length(temp2) / 2, length(temp3) / 2))

ggplot(df, aes(x=years, y=num_commitments)) +
  geom_line() +
  geom_point() +
  ggtitle("Number of Commitments vs Time", "in a2c #commitments (All Time)") +
  xlab("Year") +
  ylab("Number of Commitments") +
  scale_x_continuous(breaks = 2021:2023) +
  geom_text(aes(label = num_commitments, size = NULL), nudge_y=7)