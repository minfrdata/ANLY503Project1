library(ggplot2)
# Change outlier, color, shape and size
p<-ggplot(dt_truecar, aes(x=State, y=Price)) + 
  geom_boxplot(outlier.colour="grey", 
               outlier.size=1,fill='red4', color="black")+
  coord_cartesian(ylim = c(0, 40000))+
  xlab("State") + ylab("Cars' Price")+ggtitle("Price distribution in all states")+
  theme_bw()+
  theme(plot.title = element_text(size = 18, face = "bold",hjust = 0.5),text = element_text(size=12))
#theme_bw()
p

#one-way anova
# Compute the analysis of variance
res.aov <- aov(Price ~ State, data = dt_truecar)
# Summary of the analysis
summary(res.aov)
