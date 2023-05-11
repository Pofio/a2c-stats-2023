library("rjson")
library("ggplot2")
library("dplyr")


data <- fromJSON(file = "2023-cycle/result/result.json")
df <- data.frame(matrix(unlist(data, recursive = F), nrow = length(data), byrow = T))
colnames(df) <- c("tag", "university", "subjects")

why_df_bruh <- data.frame(subjects = unlist(df$subjects))

ggplot(top_n(count(why_df_bruh, subjects), 17, n), mapping = aes(x = reorder(subjects, n), y = n)) +
  geom_bar(stat = "identity") +
  geom_text(aes(label = n), position = position_dodge(width = 0.9), hjust = -0.3) +
  coord_flip() +
  ggtitle("Interested Subjects vs Number of Students", "in a2c #commitments") +
  xlab("Subject") +
  ylab("Numbert of Students")

print("Done")