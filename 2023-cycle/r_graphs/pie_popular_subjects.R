library("rjson")
library("ggplot2")

data <- fromJSON(file = "2023-cycle/result/result.json")
df <- data.frame(matrix(unlist(data, recursive = F), nrow = length(data), byrow = T))
colnames(df) <- c("tag", "university", "subjects")

# Top 3:
#   Computer Science
#   Economics
#   Mathematics

subject <- "Economics"

total <- length(df$subjects)
num <- sum(unlist(df$subjects) == subject)

subject_label <- paste(subject, "\n",
                       num, " / ", total, "\n",
                       round(num / total * 100, 2), "%", sep = "")
other_label <- paste("Other\n",
                       total - num, " / ", total, "\n",
                       round((total - num) / total * 100, 2), "%", sep = "")

df <- data.frame(group = c(subject_label, other_label), value = c(num, total - num))
df <- df %>%
  arrange(desc(group)) %>%
  mutate(prop = value / sum(df$value) * 100) %>%
  mutate(ypos = cumsum(prop) - 0.5 * prop)

ggplot(df, aes(x = "", y = prop, fill = group)) +
  geom_bar(stat = "identity", width = 1, color = "white") +
  coord_polar("y", start = 0) +
  theme_void() +
  theme(legend.position = "none") +
  geom_text(aes(y = ypos, label = group), color = "white", size = 6) +
  scale_fill_manual(values = c("#0275d8", "#858585")) +
  ggtitle(paste("Proportion of Students Interested in", subject), "in a2c #commitments (2023)")
