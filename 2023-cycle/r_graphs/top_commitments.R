library("rjson")
library("ggplot2")
library("dplyr")

# 2023 Cycle
data <- fromJSON(file = "2023-cycle/result/result.json")
df <- data.frame(matrix(unlist(data, recursive = F), nrow = length(data), byrow = T))
colnames(df) <- c("tag", "university", "subjects")

df$university <- unlist(df$university)

# All Time
# data <- fromJSON(file = "historical/result/result.json")
#
# temp1 <- unlist(data[["2021"]])
# temp2 <- unlist(data[["2022"]])
# temp3 <- unlist(data[["2023"]])
#
# df <- data.frame("university" = c(temp1[1:(length(temp1)/2)*2], temp2[1:(length(temp2)/2)*2], temp3[1:(length(temp3)/2)*2]))

ggplot(top_n(count(df, university), 17, n), mapping = aes(x = reorder(university, n), y = n)) +
  geom_bar(stat = "identity") +
  geom_text(aes(label = n), position = position_dodge(width = 0.9), hjust = -0.3) +
  coord_flip() +
  ggtitle("University vs Number of Commitments", "in a2c discord #commitments (2023 Cycle)") +
  # ggtitle("University vs Number of Commitments", "in a2c discord #commitments (All Time)") +
  xlab("University") +
  ylab("Numbert of Commitments")


print("Done")