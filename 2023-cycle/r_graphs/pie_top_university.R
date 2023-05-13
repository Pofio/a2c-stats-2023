library("rjson")
library("ggplot2")

# data <- fromJSON(file = "2023-cycle/result/result.json")
# df <- data.frame(matrix(unlist(data, recursive = F), nrow = length(data), byrow = T))
# colnames(df) <- c("tag", "university", "subjects")
# df$university <- unlist(df$university)
#
# t25 <- read.csv("data/t25.txt", header = F)
# t50 <- read.csv("data/t50.txt", header = F)
#
# print(df$subjects)

# All Time
data <- fromJSON(file = "historical/result/result.json")

temp1 <- unlist(data[["2021"]])
temp2 <- unlist(data[["2022"]])
temp3 <- unlist(data[["2023"]])

df <- data.frame("university" = c(temp1[1:(length(temp1)/2)*2], temp2[1:(length(temp2)/2)*2], temp3[1:(length(temp3)/2)*2]))


total <- length(df$university)
num_t25 <- sum(df$university %in% t25$V1)
num_t50 <- sum(df$university %in% t50$V1) - num_t25


t25_label <- paste("Top 25\n",
                       num_t25, " / ", total, "\n",
                       round(num_t25 / total * 100, 2), "%", sep = "")

t50_label <- paste("Top 50\n",
                       num_t50, " / ", total, "\n",
                       round(num_t50 / total * 100, 2), "%", sep = "")

other_label <- paste("Other\n",
                       (total - num_t25 - num_t50), " / ", total, "\n",
                       round((total - num_t25 - num_t50) / total * 100, 2), "%", sep = "")


df <- data.frame(group = c(t25_label, t50_label, other_label), value = c(num_t25, num_t50, total - num_t25 - num_t50))
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
  scale_fill_manual(values = c("#858585", "#0275d8", "#d9534f")) +
  ggtitle("Number of Students Committed to T25/T50/Other Universities", "in a2c #commitments (All Time)")
print("Done")