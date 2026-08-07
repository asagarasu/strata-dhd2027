# import data
lexicon <- read.csv('lexicon.csv')

# process data
process_data <- function(data){
  data_filtered <- subset(data, num_duration >= 1 & num_duration <= 365) 
  
  # calculate rank
  df <- aggregate(adjusted_freq ~ num_duration, data = data_filtered, sum) 
  df$rank <- sapply(df$num_duration, function(x) {
    sum(df$adjusted_freq[df$num_duration >= x])
  }) 
  
  # calculate relative rank
  N <- sum(df$adjusted_freq) 
  df$rr <- (df$rank - 1) / (N-1) 
  
  names(df)[names(df) == "num_duration"] <- "delay"
  return(df)
}

# numeric data
lexicon_num <- subset(lexicon, Type == 'numeric')
df_num <- process_data(lexicon_num) 

# numeric + verbal data
df_all <- process_data(lexicon)


# model fitting

# define models

# f1 <- power function
f1 <- function(time, parms){
  (parms[1]*time^(1-parms[2]))/(1-parms[2])
}

# f2 <- hyperbola-like function
f2 <- function(time, parms){
  (1 + parms[1]*time)^(-parms[2])
} 

# f3 <- exponential function
f3 <- function(time, parms){
  exp(-parms[1]*time)
} 

# f4 <- simple hyperbolic function
f4 <- function(time, parms){
  (1 + parms[1]*time)^(-1)
}

# f5 <- hyperboloid function
f5 <- function(time, parms){
  (1 + parms[1]*time^parms[2])^(-1)
} 

# f6 <- constant sensitivity function
f6 <- function(time, parms){
  exp(-(parms[1]*time)^parms[2])
} 

# f7 <- quasi-hyperbolic function
f7 <- function(time, parms){
  parms[1]*exp(-parms[2]*time)
} 

# f8 <- double exponential function
f8 <- function(time, parms){
  parms[1]*exp(-parms[2]*time)+(1-parms[1])*exp(-parms[3]*time)
} 


# calculate AIC & BIC
AIC <- function(y_test,y_pred,k,n){
  resid <- y_test-y_pred
  SSE <- sum(resid ** 2) 
  return(2*k+n*log(SSE/n))
} 

BIC <- function(y_test,y_pred,k,n){
  resid <- y_test-y_pred
  SSE <- sum(resid ** 2)
  return(k*log(n)+n*log(SSE/n))
}

# define functions for model fitting and evaluation
fit_model <- function(df){
  delay <- df$delay
  rr <- df$rr
  num <- c(length(rr)) 
  
  # model fitting
  nls.est1 <- function(parms1, time, rank){
    preds1 <- f1(time, parms1)
    sum((rank - preds1)^2)
  }
  parms1.start <- c(2, 1.5)
  pout1 <- optim(parms1.start, nls.est1, time = delay, rank = rr)
  
  nls.est2 <- function(parms2, time, rank){
    preds2 <- f2(time, parms2)
    sum((rank - preds2)^2)
  }
  parms2.start <- c(1, 1)
  pout2 <- optim(parms2.start, nls.est2, time = delay, rank = rr) 
  
  nls.est3 <- function(parms3, time, rank){
    preds3 <- f3(time, parms3)
    sum((rank - preds3)^2)
  }
  parms3.start <- c(1)
  pout3 <- optim(parms3.start, nls.est3, time = delay, rank = rr, method = "Brent", lower = -1, upper = 1)
  
  
  nls.est4 <- function(parms4, time, rank){
    preds4 <- f4(time, parms4)
    sum((rank - preds4)^2)
  }
  parms4.start <- c(1)
  pout4 <- optim(parms4.start, nls.est4, time = delay, rank = rr, method = "Brent", lower = -10, upper = 10) 
  
  nls.est5 <- function(parms5, time, rank){
    preds5 <- f5(time, parms5)
    sum((rank - preds5)^2)
  }
  parms5.start <- c(1, 1)
  pout5 <- optim(parms5.start, nls.est5, time = delay, rank = rr) 
  
  nls.est6 <- function(parms6, time, rank){
    preds6 <- f6(time, parms6)
    sum((rank - preds6)^2)
  }
  parms6.start <- c(0, 0)
  pout6 <- optim(parms6.start, nls.est6, time = delay, rank = rr) 
  
  nls.est7 <- function(parms7, time, rank){
    preds7 <- f7(time, parms7)
    sum((rank - preds7)^2)
  }
  parms7.start <- c(0, 0)
  pout7 <- optim(parms7.start, nls.est7, time = delay, rank = rr)
  
  nls.est8 <- function(parms8, time, rank){
    preds8 <- f8(time, parms8)
    sum((rank - preds8)^2)
  }
  parms8.start <- c(1, 1, 1)
  pout8 <- optim(parms8.start, nls.est8, time = delay, rank = rr) 
  
  
  
  # estimation
  p1 <- (pout1$par[1]*delay^(1-pout1$par[2]))/(1-pout1$par[2])
  p2 <- (1 + pout2$par[1]*delay)^(-pout2$par[2])
  p3 <- exp(-pout3$par[1]*delay)
  p4 <- (1 + pout4$par[1]*delay)^(-1)
  p5 <- (1 + pout5$par[1]*delay^pout5$par[2])^(-1)
  p6 <- exp(-(pout6$par[1]*delay)^pout6$par[2])
  p7 <- pout7$par[1]*exp(-pout7$par[2]*delay)
  p8 <- pout8$par[1]*exp(-pout8$par[2]*delay)+(1-pout8$par[1])*exp(-pout8$par[3]*delay)
  
  
  # summary
  result.sum <- data.frame(
    Model = c("power", "hyperbola-like", "exponential", "simple hyperbolic",
              "hyperboloid", "constant sensitivity", "quasi-hyperbolic", 
              "double exponential"),
    par = c(paste(pout1$par, collapse = ", "),
            paste(pout2$par, collapse = ", "),
            paste(pout3$par, collapse = ", "),
            paste(pout4$par, collapse = ", "),
            paste(pout5$par, collapse = ", "),
            paste(pout6$par, collapse = ", "),
            paste(pout7$par, collapse = ", "),
            paste(pout8$par, collapse = ", ")),
    AIC = c(AIC(rr, p1, 2, num),
            AIC(rr, p2, 2, num),
            AIC(rr, p3, 1, num),
            AIC(rr, p4, 1, num),
            AIC(rr, p5, 2, num),
            AIC(rr, p6, 2, num),
            AIC(rr, p7, 2, num),
            AIC(rr, p8, 3, num)),
    BIC = c(BIC(rr, p1, 2, num),
            BIC(rr, p2, 2, num),
            BIC(rr, p3, 1, num),
            BIC(rr, p4, 1, num),
            BIC(rr, p5, 2, num),
            BIC(rr, p6, 2, num),
            BIC(rr, p7, 2, num),
            BIC(rr, p8, 3, num)))
  cat("Summary for", deparse(substitute(df)), "\n")
  print(result.sum)
  
  # return the values of p1-8
  return(list(p1 = p1, p2 = p2, p3 = p3, p4 = p4, p5 = p5, p6 = p6, p7 = p7, p8 = p8))

}

# results for numeric
numer <- fit_model(df_num) 
numer$p1

# results for numeric + verbal
all <- fit_model(df_all) 
all$p1

# plot
library(ggplot2)
ggplot(df_num) +
  geom_point(aes(x=delay, y=rr), size = 3) + 
  xlab("Delay/Days") + ylab("Relative Rank") +
  scale_x_continuous(expand = c(0, 0)) +
  scale_y_continuous(expand = c(0, 0)) +
  geom_line(aes(delay, numer$p1, col = "1"), lwd = 3) +
  geom_line(aes(delay, numer$p3, col = "2"), lwd = 3) +
  geom_line(aes(delay, numer$p4, col = "3"), lwd = 3) +
  scale_colour_manual(name = "Function", 
                      values = c("1" = "red", "2" = "green", "3" = "blue"),
                      labels = c(expression(italic(f)(italic(D)) == frac(italic(c) * italic(D)^(1-italic(tau)),1-italic(tau))),
                      expression(italic(f)(italic(D)) == italic(e)^(-italic(k) * italic(D))),
                      expression(italic(f)(italic(D)) == frac(1,1 + italic(k) * italic(D)))
                      )) +
  theme_classic() +
  theme(text=element_text(size=36, family="sans"), 
        legend.position.inside = c(0.8, 0.8),
        legend.spacing.y = unit(3.0, 'cm'),
        axis.title.y = element_text(margin = margin(t = 0, r = 20, b = 0, l = 0)),
        axis.title.x = element_text(margin = margin(t = 20, r = 0, b = 0, l = 0)),
        axis.text = element_text(colour = "black"),
        axis.line = element_line(linewidth = 1.5),
        plot.margin=unit(rep(1,4), 'cm'))
  
  
ggsave("Fig3_num.jpg", width = 20, height = 15, dpi = 300)


ggplot(df_all) +
  geom_point(aes(x=delay, y=rr), size = 3) + 
  xlab("Delay/Days") + ylab("Relative Rank") +
  scale_x_continuous(expand = c(0, 0)) +
  scale_y_continuous(expand = c(0, 0)) +
  geom_line(aes(delay, all$p2, col = "1"), lwd = 3) +
  geom_line(aes(delay, all$p3, col = "2"), lwd = 3) +
  geom_line(aes(delay, all$p4, col = "3"), lwd = 3) +
  scale_colour_manual(name = "Function", 
                      values = c("1" = "red", "2" = "green", "3" = "blue"),
                      labels = c(expression(italic(f)(italic(D)) == frac(1,(1 + italic(k) * italic(D))^italic(s))),
                                 expression(italic(f)(italic(D)) == italic(e)^(-italic(k) * italic(D))),
                                 expression(italic(f)(italic(D)) == frac(1,1 + italic(k) * italic(D)))
                      )) +
  theme_classic() +
  theme(text=element_text(size=36, family="sans"), 
        legend.position.inside = c(0.8, 0.8),
        legend.spacing.y = unit(3.0, 'cm'),
        axis.title.y = element_text(margin = margin(t = 0, r = 20, b = 0, l = 0)),
        axis.title.x = element_text(margin = margin(t = 20, r = 0, b = 0, l = 0)),
        axis.text = element_text(colour = "black"),
        axis.line = element_line(linewidth = 1.5),
        plot.margin=unit(rep(1,4), 'cm'))


ggsave("Fig3_all.jpg", width = 20, height = 15, dpi = 300)

#=============================== Combine figures ===============================

imgnum <- readJPEG("Fig3_num.jpg") 
imgall <- readJPEG("Fig3_all.jpg")  

jpeg("Fig3_300dpi.jpg", width = 42, height = 15, units = 'cm', res = 300)

grid.newpage()
pushViewport(viewport(layout = grid.layout(1, 2)))  

grid.raster(imgnum, vp = viewport(layout.pos.row = 1, layout.pos.col = 1))  
grid.raster(imgall, vp = viewport(layout.pos.row = 1, layout.pos.col = 2))  

grid.text("a", vp = viewport(layout.pos.row = 1, layout.pos.col = 1), 
          x = unit(0, "npc"), y = unit(1, "npc"), just = c("left", "top"),
          gp = gpar(fontsize = 28))
grid.text("b", vp = viewport(layout.pos.row = 1, layout.pos.col = 2), 
          x = unit(0, "npc"), y = unit(1, "npc"), just = c("left", "top"),
          gp = gpar(fontsize = 28))

dev.off()

