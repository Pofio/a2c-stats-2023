library("rjson")
library("ggplot2")
library("dplyr")


data <- fromJSON(file = "2023-cycle/result/result.json")
df <- data.frame(matrix(unlist(data, recursive = F), nrow = length(data), byrow = T))
colnames(df) <- c("tag", "university", "subjects")

df$university <- unlist(df$university)


ggplot(top_n(count(df, university), 17, n), mapping = aes(x = reorder(university, n), y = n)) +
  geom_bar(stat = "identity") +
  geom_text(aes(label = n), position = position_dodge(width = 0.9), hjust = -0.3) +
  coord_flip() +
  ggtitle("University vs Number of Commitments", "in a2c #commitments") +
  xlab("University") +
  ylab("Numbert of Commitments")


print("Done")