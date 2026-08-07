# Task1: expression judgment

library(ggplot2)
library(ggbreak)
library(reshape2)
library(tidyverse)
library(ggridges)
library(readxl)
library(tibble)
library(grid)
library(jpeg)

s1 <- read.csv('task1.csv')
s1 <- s1[-1, ]
rownames(s1) <- 1:nrow(s1)
s1[] <- lapply(s1, function(x) as.numeric(as.character(x)))


# coding: 1 = yes, 2 = unsure, 3 = no

# attention check
fail1 <- which(rowSums(s1[, 182:186] != 3, na.rm = TRUE) > 0)
fail1_id <- s1[fail1, 1] 
s1 <- s1[!rownames(s1) %in% fail1_id, ] 

# calculate proportion of "no"
prop <- sapply(s1[,-1], function(column) mean(column == 3))
result1 <- data.frame(
  Proportion = prop,
  MeetCriteria = ifelse(prop <= 0.2, 1, 0)
  )

print(result1)
print(sum(result1$MeetCriteria)) 


# Task2: duration estimation
s2 <- read.csv('task2.csv') 
task2_translation <- s2[1, ]
task2_translation <- task2_translation[, -1]
s2 <- s2[-1, ]
rownames(s2) <- 1:nrow(s2)
s2[] <- lapply(s2, function(x) as.numeric(as.character(x)))


# attention check
fail2 <- which(s2[, 2] != 2)
fail2_id <- s2[fail2, 1]
s2 <- s2[!(s2[, 1] %in% fail1_id | s2[, 1] %in% fail2_id), ] #47

# summary statistics
summary_stats <- function(x) {
  c(mean = mean(x, na.rm = TRUE),
    sd = sd(x, na.rm = TRUE),
    median = median(x, na.rm = TRUE),
    IQR = IQR(x, na.rm = TRUE),
    CV = sd(x, na.rm = TRUE) / mean(x, na.rm = TRUE)) 
}
result2 <- sapply(s2[, 3:ncol(s2)], summary_stats)
result2 <- data.frame(t(result2))
colnames(result2) <- c("M", "SD", "Median", "IQR", "CV")

print(result2)
result2_sorted <- result2[order(result2$M), ]
print(result2_sorted)

# plots

mean_scores <- colMeans(s2[, 3:86], na.rm = TRUE)

# mean value < 0.001 days
words_less_than_0001 <- names(mean_scores[mean_scores <= 0.001]) # n = 8

# 0.001 < mean value < 0.02
words_0001_to_002 <- names(mean_scores[mean_scores > 0.001 & mean_scores <= 0.02]) # n = 10

# 0.02 < mean value < 1
words_0.02_to_1 <- names(mean_scores[mean_scores > 0.02 & mean_scores <= 1]) # n = 14

# 1 < mean value < 365
words_1_to_365 <- names(mean_scores[mean_scores > 1 & mean_scores <= 365]) # n = 16

# 365 < mean value < 36500
words_365_to_36500 <- names(mean_scores[mean_scores > 365 & mean_scores <= 36500]) # n = 19

# mean value > 36500 
words_above_36500 <- names(mean_scores[mean_scores > 36500]) # n = 17

data_to_plot <- s2[, 3:86]

data_long <- melt(data_to_plot)
data_long <- na.omit(data_long)


task2_translation2 <- data.frame(t(task2_translation))
task2_translation2 <- task2_translation2 %>%
  rownames_to_column(var = "chinese") 
task2_translation2$X1 <- gsub("\\(.*?\\)", "", task2_translation2$X1)


data_long <- data_long %>%
  left_join(task2_translation2, by = c("variable" = "chinese")) 

data_long <- data_long %>%
  mutate(variable_with_translation = paste(variable, X1, sep = " ")) 


data_less_than_0001 <- subset(data_long,data_long$variable %in% words_less_than_0001)
data_0001_to_002 <- subset(data_long,data_long$variable %in% words_0001_to_002)
data_0.02_to_1 <- subset(data_long,data_long$variable %in% words_0.02_to_1)
data_1_to_365 <- subset(data_long,data_long$variable %in% words_1_to_365)
data_365_to_36500 <- subset(data_long,data_long$variable %in% words_365_to_36500)
data_above_36500 <- subset(data_long,data_long$variable %in% words_above_36500)


process_time_data <- function(df) {
  avg_df <- df %>%
    group_by(variable) %>%
    summarise(mean_value = mean(value), .groups = 'drop') %>%
    arrange(mean_value)
  
  df$variable <- factor(df$variable, levels = avg_df$variable)
  
  quantiles_df <- df %>%
    group_by(variable) %>%
    summarise(q95 = quantile(value, 0.95), .groups = 'drop')
  
  filtered_df <- df %>%
    left_join(quantiles_df, by = "variable") %>%
    filter(value <= q95)
  
  list(avg = avg_df, filtered = filtered_df)
}


data_list <- list(
  data_less_than_0001 = data_less_than_0001,
  data_0001_to_002 = data_0001_to_002,
  data_0.02_to_1 = data_0.02_to_1,
  data_1_to_365 = data_1_to_365,
  data_365_to_36500 = data_365_to_36500,
  data_above_36500 = data_above_36500
)

results <- lapply(data_list, process_time_data)

for (name in names(results)) {
  assign(paste0(name, "_avg"), results[[name]]$avg)
  assign(paste0(name, "_filtered"), results[[name]]$filtered)
}

var_names_created <- unlist(lapply(names(results), function(name) {
  c(paste0(name, "_avg"), paste0(name, "_filtered"))
}))

print(var_names_created)

#[1] "data_less_than_0001_avg"      "data_less_than_0001_filtered" "data_0001_to_002_avg"        
#[4] "data_0001_to_002_filtered"    "data_0.02_to_1_avg"           "data_0.02_to_1_filtered"     
#[7] "data_1_to_365_avg"            "data_1_to_365_filtered"       "data_365_to_36500_avg"       
#[10] "data_365_to_36500_filtered"   "data_above_36500_avg"         "data_above_36500_filtered"   


# ============================= less_than_0001 =================================

data_less_than_0001_filtered$variable_with_translation <- factor(
  data_less_than_0001_filtered$variable_with_translation,
  levels = unique(data_less_than_0001_filtered$variable_with_translation[match(levels(data_less_than_0001_filtered$variable),
                                                                               data_less_than_0001_filtered$variable)])
)

# change time unit to minutes
data_less_than_0001_filtered$value_min <- data_less_than_0001_filtered$value*24*60

ggplot(data_less_than_0001_filtered, aes(x = value_min, y = variable_with_translation, fill = variable_with_translation)) +
  geom_density_ridges(alpha = 0.7, scale = 3) +
  scale_x_continuous(breaks = c(0, 0.25, 0.5, 0.75, 1, 5)) +
  labs(
    x = "Time estimate (in minutes)",
    y = " ",
    fill = "Duration expressions"
  ) +
  scale_y_discrete(expand = expansion(mult = c(0.01, 0.25))) +
  theme_ridges() +
  theme(text=element_text(family="sans"),
        axis.text.y = element_text(size = 11),
        axis.text.x = element_text(size = 11),
        axis.title.x = element_text(size = 13, hjust = 0.78),
        axis.text.x.top = element_blank(),
        axis.ticks.x.top = element_blank(),
        axis.line.x.top = element_blank())+
  guides(fill = "none") +
  scale_x_break(c(1, 4.9)) 


ggsave("Fig2a.jpg", width = 3200, height = 1800, units = "px", dpi = 300, bg = "white")


# =============================== 0001_to_002 ==================================

data_0001_to_002_filtered$variable_with_translation <- factor(
  data_0001_to_002_filtered$variable_with_translation,
  levels = unique(data_0001_to_002_filtered$variable_with_translation[match(levels(data_0001_to_002_filtered$variable),
                                                                            data_0001_to_002_filtered$variable)])
)

# change time unit to minutes
data_0001_to_002_filtered$value_min <- data_0001_to_002_filtered$value*24*60

ggplot(data_0001_to_002_filtered, aes(x = value_min, y = variable_with_translation, fill = variable_with_translation)) +
  geom_density_ridges(alpha = 0.7, scale = 3) +
  labs(
    x = "Time estimate (in minutes)",
    y = " ",
    fill = "Duration expressions"
  ) +
  scale_y_discrete(expand = expansion(mult = c(0.01, 0.25))) +
  theme_ridges() +
  theme(text=element_text(family="sans"),
        axis.text.y = element_text(size = 11),
        axis.text.x = element_text(size = 11),
        axis.title.x = element_text(size = 13, hjust = 0.5))+
  guides(fill = "none")

ggsave("Fig2b.jpg", width = 3200, height = 1800, units = "px", dpi = 300, bg = "white")


# ================================ 0.02_to_1 ===================================

data_0.02_to_1_filtered$variable_with_translation <- factor(
  data_0.02_to_1_filtered$variable_with_translation,
  levels = unique(data_0.02_to_1_filtered$variable_with_translation[match(levels(data_0.02_to_1_filtered$variable),
                                                                          data_0.02_to_1_filtered$variable)])
)

ggplot(data_0.02_to_1_filtered, aes(x = value, y = variable_with_translation, fill = variable_with_translation)) +
  geom_density_ridges(alpha = 0.7, scale = 3) +
  labs(
    x = "Time estimate (in days)",
    y = " ",
    fill = "Duration expressions"
  ) +
  scale_y_discrete(expand = expansion(mult = c(0.01, 0.25))) +
  theme_ridges() +
  theme(text=element_text(family="sans"),
        axis.text.y = element_text(size = 11),
        axis.text.x = element_text(size = 11),
        axis.title.x = element_text(size = 13, hjust = 0.5))+
  guides(fill = "none")

ggsave("Fig2c.jpg", width = 3200, height = 1800, units = "px", dpi = 300, bg = "white")


# ================================= 1_to_365 ===================================

data_1_to_365_filtered$variable_with_translation <- factor(
  data_1_to_365_filtered$variable_with_translation,
  levels = unique(data_1_to_365_filtered$variable_with_translation[match(levels(data_1_to_365_filtered$variable),
                                                                         data_1_to_365_filtered$variable)])
)

ggplot(data_1_to_365_filtered, aes(x = value, y = variable_with_translation, fill = variable_with_translation)) +
  geom_density_ridges(alpha = 0.7, scale = 3) +
  scale_x_continuous(breaks = c(0, 50, 100, 150, 200, 365, 730)) +
  labs(
    x = "Time estimate (in days)",
    y = " ",
    fill = "Duration expressions"
  ) +
  scale_y_discrete(expand = expansion(mult = c(0.01, 0.25))) +
  theme_ridges() +
  theme(text=element_text(family="sans"),
        axis.text.y = element_text(size = 11),
        axis.text.x = element_text(size = 11),
        axis.title.x = element_text(size = 13, hjust = 0.67),
        axis.text.x.top = element_blank(),
        axis.ticks.x.top = element_blank(),
        axis.line.x.top = element_blank())+
  guides(fill = "none") +
  scale_x_break(c(200, 360)) +
  scale_x_break(c(370, 725))

ggsave("Fig2d.jpg", width = 3200, height = 1800, units = "px", dpi = 300, bg = "white")


# =============================== 365_to_36500 =================================

data_365_to_36500_filtered$variable_with_translation <- factor(
  data_365_to_36500_filtered$variable_with_translation,
  levels = unique(data_365_to_36500_filtered$variable_with_translation[match(levels(data_365_to_36500_filtered$variable),
                                                                             data_365_to_36500_filtered$variable)])
)

# change time unit to years
data_365_to_36500_filtered$value_yrs <- data_365_to_36500_filtered$value/365

ggplot(data_365_to_36500_filtered, aes(x = value_yrs, y = variable_with_translation, fill = variable_with_translation)) +
  geom_density_ridges(alpha = 0.7, scale = 3) +
  labs(
    x = "Time estimate (in years)",
    y = " ",
    fill = "Duration expressions"
  ) +
  scale_y_discrete(expand = expansion(mult = c(0.01, 0.25))) +
  theme_ridges() +
  theme(text=element_text(family="sans"),
        axis.text.y = element_text(size = 11),
        axis.text.x = element_text(size = 11),
        axis.title.x = element_text(size = 13, hjust = 0.5))+
  guides(fill = "none")

ggsave("Fig2e.jpg", width = 3200, height = 1800, units = "px", dpi = 300, bg = "white")


# =============================== above_36500 ==================================

data_above_36500_filtered$variable_with_translation <- factor(
  data_above_36500_filtered$variable_with_translation,
  levels = unique(data_above_36500_filtered$variable_with_translation[match(levels(data_above_36500_filtered$variable),
                                                                            data_above_36500_filtered$variable)])
)

# change time unit to years
data_above_36500_filtered$value_yrs <- data_above_36500_filtered$value/365

# log transform
data_above_36500_filtered$log_value_yrs <- log10(data_above_36500_filtered$value_yrs)

ggplot(data_above_36500_filtered, aes(x = log_value_yrs, y = variable_with_translation, fill = variable_with_translation)) +
  geom_density_ridges(alpha = 0.7, scale = 3) +
  labs(
    x = "log10-transformed time estimate (in years)",
    y = " ",
    fill = "Duration expressions"
  ) +
  scale_y_discrete(expand = expansion(mult = c(0.01, 0.25))) +
  theme_ridges() +
  theme(text=element_text(family="sans"),
        axis.text.y = element_text(size = 11),
        axis.text.x = element_text(size = 11),
        axis.title.x = element_text(size = 13, hjust = 0.5))+
  guides(fill = "none")


ggsave("Fig2f.jpg", width = 3200, height = 1800, units = "px", dpi = 300, bg = "white")

#=============================== Combine figures ===============================

img1 <- readJPEG("Fig2a.jpg")
img2 <- readJPEG("Fig2b.jpg")
img3 <- readJPEG("Fig2c.jpg")
img4 <- readJPEG("Fig2d.jpg")
img5 <- readJPEG("Fig2e.jpg")
img6 <- readJPEG("Fig2f.jpg")

jpeg("Fig2_600dpi.jpg", width = 3800, height = 3400, units = "px", res = 600)

grid.newpage()
pushViewport(viewport(layout = grid.layout(3, 2)))

grid.raster(img1, vp = viewport(layout.pos.row = 1, layout.pos.col = 1))
grid.raster(img2, vp = viewport(layout.pos.row = 1, layout.pos.col = 2))
grid.raster(img3, vp = viewport(layout.pos.row = 2, layout.pos.col = 1))
grid.raster(img4, vp = viewport(layout.pos.row = 2, layout.pos.col = 2))
grid.raster(img5, vp = viewport(layout.pos.row = 3, layout.pos.col = 1))
grid.raster(img6, vp = viewport(layout.pos.row = 3, layout.pos.col = 2))

grid.text("a", vp = viewport(layout.pos.row = 1, layout.pos.col = 1), x = unit(0, "npc"), y = unit(1, "npc"), just = c("left", "top"))
grid.text("b", vp = viewport(layout.pos.row = 1, layout.pos.col = 2), x = unit(0, "npc"), y = unit(1, "npc"), just = c("left", "top"))
grid.text("c", vp = viewport(layout.pos.row = 2, layout.pos.col = 1), x = unit(0, "npc"), y = unit(1, "npc"), just = c("left", "top"))
grid.text("d", vp = viewport(layout.pos.row = 2, layout.pos.col = 2), x = unit(0, "npc"), y = unit(1, "npc"), just = c("left", "top"))
grid.text("e", vp = viewport(layout.pos.row = 3, layout.pos.col = 1), x = unit(0, "npc"), y = unit(1, "npc"), just = c("left", "top"))
grid.text("f", vp = viewport(layout.pos.row = 3, layout.pos.col = 2), x = unit(0, "npc"), y = unit(1, "npc"), just = c("left", "top"))

dev.off()

