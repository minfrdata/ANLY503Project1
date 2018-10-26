library(ggplot2)
library(dplyr)
library(maps)
# map sales amount by state:
us <- map_data("state")
amount_state=read.csv("Amount_state.csv",colClasses = c("numeric","character","numeric","character"))
colnames(amount_state) <- c('ID', 'State_Abbreviation', 'Sales_Volume', 'State')

gg <- ggplot()
gg <- gg + geom_map(data=us, map=us,
                    aes(x=long, y=lat, map_id=region),
                    fill="#ffffff", color="#ffffff", size=0.15)
gg <- gg + geom_map(data=amount_state, map=us,
                    aes(fill=Sales_Volume, map_id=State),
                    color="#ffffff", size=0.15)
gg <- gg + scale_fill_continuous(low='thistle2', high='darkred', 
                                 guide='colorbar')
gg <- gg + labs(x=NULL, y=NULL)
gg <- gg + coord_map("albers", lat0 = 39, lat1 = 45) +ggtitle("Sales Volume Distribution by States")+theme(plot.title = element_text(hjust = 0.5))+ theme(plot.title = element_text(size=16))
gg <- gg + theme(panel.border = element_blank())
gg <- gg + theme(panel.background = element_blank())
gg <- gg + theme(axis.ticks = element_blank())
gg <- gg + theme(axis.text = element_blank())
## Save the image
#ggsave("../project_web_1.0/img/coropleth.png", width = 8, height = 6, dpi = 200)
gg